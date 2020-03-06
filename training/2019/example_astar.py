class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # total cost of the node
        self.cost = 0
        # terrain cost
        self.terrian_cost = 0
        # distance between the current node and start node
        self.from_start = 0
        # heuristic - estimated distance from the current node to the end node
        self.from_end = 0
    
    def cost_calc(self, current_node, end_node):
        """
        calculate the cost for the new node based on current node position and end node location 
        """
        # keep track of how many moves have been made
        self.from_start = current_node.from_start + 1
        # distance from end node
        self.from_end = ((self.position[0] - end_node.position[0]) ** 2) + ((self.position[1] - end_node.position[1]) ** 2)
        # take into account cost of travelling over terrain
        self.cost = self.terrian_cost + self.from_start + self.from_end
        
        return self.cost

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # loop until end
    while len(open_list) > 0:
        print(len(open_list))

        # Get the current node
        current_node = open_list[0]
        current_index = 0

        # out of the previous selection, find the node with the lowest cost
        for index, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        children = generate_children(maze, current_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.cost_calc(current_node, end_node)

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.from_start > open_node.from_start:
                    continue

            # Add the child to the open list
            open_list.append(child)


def generate_children(maze, current_node) -> list:
    """
    desc
    """
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#, (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure within range
        if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
            continue

        # Make sure walkable terrain
        if maze[node_position[0]][node_position[1]] != 0:
            continue

        # Create new node
        new_node = Node(current_node, node_position)

        # Append
        children.append(new_node)

    return children


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (2, 9)

    path = astar(maze, start, end)
    print(path)