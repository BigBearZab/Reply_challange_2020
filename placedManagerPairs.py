# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:43:50 2020

@author: elanche1
"""

placed_people = {}


#input dictionary of manager-manager pair - locations, and highest scoring pairs
#Manager Dict - Location of Manager-manager pairs
#Manager Pairs - Highest scoring manager-manager pairs
def placeMPairs(ManagerDict, ManagerPairs, locations):

    #keep track of which managers have been placed on the board (you can't add them twice!)
    managers_placed = []



    for key in ManagerDict.keys():
        i =0
        location = locations[key]
        if key not in placed_people:
            if ManagerPairs[i][0] in managers_placed or ManagerPairs[i][1]:
                pass
            else:
                placed_people.update({key: ManagerPairs[i]})
                #add them to the list of added managers
                managers_placed.append(ManagerPairs[i][0])
                managers_placed.append(ManagerPairs[i][0])

        i +=1

    return managers_placed, placed_people