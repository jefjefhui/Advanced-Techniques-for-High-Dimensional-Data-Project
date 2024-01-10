#Query 2 method 2 implementation starts here
#Query 2: Given an accident id, find the K nearest neighbors. The K nearst neighbors need to have the same
#severity level with the chosen accident

#Import all the required libraries here
import csv
import datetime
from math import radians, cos, sin, asin, sqrt
import os, psutil
import quads
import numpy as np
from scipy.spatial import KDTree
import operator


def Query2Method2(idNumber,K_Value):
    start_here = datetime.datetime.now()
    target_long =0
    target_lat =0
    target_severity =0

    with open('US_Accidents_Dec21_updated.csv') as USTrafficAccident:
        reader = csv.reader(USTrafficAccident)

        next(reader)
        for line in reader:
            if(line[0]==idNumber):
                target_long = line[5]
                target_lat =line[4]
                target_severity=line[1]
                break



    matched_severity_ID =[]
    matched_long =[]
    matched_lat =[]

    #Filter all the values that doesn't match the severity values
    with open('US_Accidents_Dec21_updated.csv') as USTrafficAccident2:
        reader2 = csv.reader(USTrafficAccident2)

        next(reader2)

        for line in reader2:
            if(line[1]==target_severity):
                matched_severity_ID.append(line[0])
                matched_lat.append(line[4])
                matched_long.append(line[5])

    print(len(matched_severity_ID))
    print(len(matched_long))
    print(len(matched_lat))
    print(type(matched_lat))
    print(type(matched_long))
    print(type(matched_long[0]))
    print(type(matched_lat[0]))

    checker = True
    tracking_Number = 0
    distance_Dict ={}
    while checker:
        # Calculation of distance starts here
        # Declaration: The distance calculation method is extracted from online resources.
        # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1 = radians(float(target_long))
        lon2 = radians(float(matched_long[tracking_Number]))
        lat1 = radians(float(target_lat))
        lat2 = radians(float(matched_lat[tracking_Number]))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis / 111
        distance_Dict[matched_severity_ID[tracking_Number]] = dis_In_Degree
        if(tracking_Number==len(matched_lat)-1):
            checker =False
        else:
            tracking_Number = tracking_Number+1
    print(len(distance_Dict))
    values = sorted(distance_Dict.items(),key=operator.itemgetter(1))
    print(len(values))
    End_Time = (datetime.datetime.now()-start_here).total_seconds()
    processing = psutil.Process()
    query_Memory = processing.memory_info().rss
    print('-------------------------------------------------Query 2 Method 2 Implementation Result---------------------------------------------')
    print('Linear scan does not involve indexing procedures, so indexing performance information are not available')
    print('The total query time is'+str(End_Time)+'seconds')
    print('The total query memory cost is'+str(query_Memory)+'bytes')

    print('#############################These are the obtained results######################################')
    tracking2=0
    for x in values:
        if(tracking2==K_Value):
            break
        print(x)
        tracking2 = tracking2+1











#case 1
#Query2Method2('A-1',6)

#case 2
#Query2Method2('A-1000',3)

#case3
Query2Method2('A-50',4)




