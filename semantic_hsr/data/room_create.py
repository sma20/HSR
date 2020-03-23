#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import numpy
import pandas as pd
M=[[0 for j in range(0,5)] for i in range(0,6)]
M=[['room','xmin','xmax','ymin','ymax'], ['Corridor',-1, 0.5,-3.2,0], ['Kitchen',0.5,5,0,3.5], ['Bathroom',0.5,3.1,-3.2,0], ['Bedroom',3.1,8,-3.2,0], ['Living_room',5,8,0,3.5]]

data=pd.DataFrame(M)
data.to_csv('room.csv', index=False, header=False)