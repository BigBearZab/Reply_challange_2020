"""
#1  first line has two integers, W and H

#2 Floor office itself, devs are _, Managers are M, unavilible are #

#3 an int containing the number of developers

#4 describing the developers themselves

#5 an int describing number of managers 

#6 decribing the managers themselves

"""

from typing import List


def parse(file_name: str):
    """
    overall function for parsing the input file
    """
    with open(file_name) as f:
        file_lines = f.read().splitlines()
    
    # step 1
    W, H = parse_header(file_lines[0])
    # step 2
    devs, managers = parse_floor(file_lines[1:H+1])
    # step 3
    dev_num = int(file_lines[H+1])
    # step 4
    dev_meta = parse_developers(file_lines[H+2 : H+2+dev_num])
    # step 5
    manager_num = int(file_lines[H+2+dev_num])
    #step 6
    manager_meta = parse_managers(file_lines[H+3+dev_num:])

    return devs, managers, dev_meta, manager_meta


def parse_header(line: List[str]) -> List[int]:
    """
    step 1
    """
    line = line.split(" ")
    W = int(line[0])
    H = int(line[1])
    return W, H


def parse_floor(file_lines: List[List[str]]):
    """
    step 2
    Two lists, first list of devloper co-ords, second manager co-ords
    """
    devs = []
    managers = []
    for y in range(len(file_lines)):
        row = file_lines[y]

        for x in range(len(row)):
            char = file_lines[y][x]

            if char == "_":
                devs.append((x,y))
            if char == "M":
                managers.append((x,y))
    
    return devs, managers


def parse_developers(file_lines: List[str]):
    """
    step 4
    [company: str, bonus: int, skill_number: int, skills: set]
    """
    meta = []

    for line in file_lines:
        line = line.split(" ")
        company = line[0]
        bonus = int(line[1])
        skill_number = int(line[2])
        skills = set(line[3:])
        meta.append([company, bonus, skill_number, skills])
    
    return meta


def parse_managers(file_lines: List[str]):
    """
    step 6
    [company, bonus]
    """
    meta = []

    for line in file_lines:
        line = line.split(" ")
        company = line[0]
        bonus = int(line[1])
        meta.append([company, bonus])
    
    return meta



if __name__ == "__main__":
    devs, managers, dev_meta, manager_meta = parse("input/b_dream.txt")