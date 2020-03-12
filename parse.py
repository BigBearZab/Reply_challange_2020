"""
#1  first line has two integers, W and H

#2 Floor office itself, devs are _, Managers are M, unavilible are #

#3 an int containing the number of developers

#4 describing the developers themselves

#5 an int describing number of managers 

#6 decribing the managers themselves

"""

from typing import List
import numpy as np


def parse(file_name: str):
    """
    overall function for parsing the input file
    Returns
        devs - co-ords of developers, list of [(x,y), (x,y)...]
        managers - same as devs but for managers
        dev_meta - [company: str, bonus: int, skill_number: int, skills: set]
        manager_meta - [company: str, bonus: int]
        all_pairs - []
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
    
    # figure out pairs
    all_pairs = pairs(file_lines[1:H+1])

    return devs, managers, dev_meta, manager_meta, [tuple(p) for p in all_pairs]


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


def pairs(file_lines: List[str]):
    """
    Given the floor, calculate what pairs there are
    """
    new_floor = []

    dev_num = 0
    manager_num = 0

    # first label them one to n
    for y in range(len(file_lines)):
        
        new_floor.append([])

        row = file_lines[y]

        for x in range(len(row)):
            
            char = file_lines[y][x]

            if char == "#":
                new_floor[y].append(0)
            elif char == "_":
                dev_num += 1
                new_floor[y].append(f"D{dev_num}")
            elif char == "M":
                manager_num += 1
                new_floor[y].append(f"M{manager_num}")
    
    # now we have the floor, work out the pairs
    pairs = []

    for y in range(len(new_floor)):

        row = new_floor[y]

        for x in range(len(row)):
            
            char = new_floor[y][x]
            
            if char != 0:
                #check left
                try:
                    left = new_floor[y][x-1]
                    if left != 0:
                        pairs.append(frozenset([char,left]))
                except:
                    pass

                # check right
                try:
                    right = new_floor[y][x+1]
                    if right != 0:
                        pairs.append(frozenset([char,right]))
                except:
                    pass

                # check up
                try:
                    up = new_floor[y-1][x]
                    if up != 0:
                        pairs.append(frozenset([char,up]))
                except:
                    pass

                # check down
                try:
                    down = new_floor[y+1][x]
                    if down != 0:
                        pairs.append(frozenset([char,down]))
                except:
                    pass
    
    return set(pairs)



if __name__ == "__main__":
    devs, managers, dev_meta, manager_meta, all_pairs = parse("input/a_solar.txt")