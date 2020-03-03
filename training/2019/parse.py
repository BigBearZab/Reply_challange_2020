"""
Desc:
    Convert the text files into useful python datastructures

From the problem statement:
    Input data will be provided in plain ASCII textfile.
    On the first line you will find four integers separated by a whitespace character:

    - N: the width of the map
    - M: the height of the map
    - C: the number of Customer Headquarters
    - R: representing the maximumnumber of Reply Offices that can be built

    C lines follow, each one built of three integers describing the X coordinate, 
    the Y coordinate, and the reward associated with Customer Headquarter.

    Then, M lines follow, describing a row of N terrain cells. 
    The top-left cell is the origin of the map and is thus assigned “(0,0)” coordinates.
    In the world map columns are represented by the X coordinate, while rows by the Y coordinate.

"""

from typing import List



def parse(file_name: str):
    """
    PARTIAL

    main function to parse the Customer headquarter locations and terrain map
    """

    # read the file into a list ['line1','line2', ..]
    with open(file_name) as text_file:
        text_lines = text_file.read().splitlines()
    
    # parse the header line
    N, M, C, R = parse_header(text_lines[0])

    # parse the office information [[X Y POINTS], [X Y POINTS], ..]
    offices = parse_offices(text_lines[1:C])

    # parse the terrain map
    terrain = []

    return offices, terrain



def parse_header(file_line: str):
    """
    WORKING

    parse the first line of the text file
    
    for the first line:
        N: width of the map
        M: the heigh of the map
        C: the number of customer headquarters
        R: maximum number of offices that can be built
    
    returns each as an int
    """

    file_line_split = file_line.split(" ")
    N = int(file_line_split[0])
    M = int(file_line_split[1])
    C = int(file_line_split[2])
    R = int(file_line_split[3])
    return N, M, C, R



def parse_offices(file_lines: List[str]) -> List[List[int]]:
    """
    WORKING 

    parse customer headquarter locations. 
    Only given the relevant lines
    for each line:
        X Y POINTS
    
    returns [[X, Y, POINTS], [X, Y, POINTS], ..]
    """

    split_lines = [l.split(" ") for l in file_lines]
    return [[int(l[0]), int(l[1]), int(l[2])] for l in split_lines]



def parse_terrain(file_lines: List[str]):
    """
    UNIMPLIMENTED

    parse the terrain information
    #   Mountains               Non-walkable cell
    ~   Water                   800 points
    *   Traffic jam             200 points
    +   Dirt                    150 points
    X   Railway level crossing  100 points
    _   Standard terrain        70 points
    T   Railway                 50 points
    """

    raise NotImplementedError()
