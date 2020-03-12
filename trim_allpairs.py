# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:47:10 2020

@author: GavinOC
"""

def manager_pairs(all_pairs):
    mpairs_list =[pair for pair in all_pairs if pair[0][0]=='M' and pair[1][0]=='M']
    return mpairs_list