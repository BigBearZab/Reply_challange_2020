"""

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

import pandas as pd
from typing import List


def parse(file_name: str):
    """
    main function to parse the Customer headquarter locations and terrain map
    """
    raise NotImplementedError()


def parse_offices(file_lines: List[str]) -> dict:
    """
    parse customer headquarter locations. 
    Only given the relevant lines
    """
    raise NotImplementedError()


def parse_terrain(file_lines: List[str]):
    """
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
