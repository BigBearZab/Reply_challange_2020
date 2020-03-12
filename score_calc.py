# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:16:04 2020

@author: denis
"""

#import numpy as np

def score_calc(a,b):
    if len(a) == 2 and len(b)==2:
        if a[0] == b[0]:
            return a[1]*b[1]
        else:
            return 0
    elif len(a) == 2 or len(b)==2:
        if a[0] == b[0]:
            return a[1]*b[1]
        else:
            return 0
    else:
        s_union = len(a[3].union(b[3]))
        s_inter = len(a[3].intersection(b[3]))
        if a[0] == b[0]:
            return a[1]*b[1] + s_inter*(s_union - s_inter)
        else:
            return s_inter*(s_union - s_inter)        
        
        

        

        