#Query 5 Method 2 Implementaiton, linear scan


#Import all the libraries here
import csv
import datetime
from math import radians, cos, sin, asin, sqrt
import os, psutil
import numpy as np
from scipy.spatial import KDTree
import math


def Query5Method2(longitude_value,latitude_value,distance_range):
    query_Start_time = datetime.datetime.now()
    ids = []
    longtitude_list = []
    latitude_list = []

    #This with open statement will extract all the required informaiton and store them into the corresponding list
    with open('US_Accidents_Dec21_updated.csv') as traffic:
        reader = csv.reader(traffic)
        next(reader)

        for line in reader:
            id = line[0]
            long = line[5]
            lat = line[4]
            ids.append(id)
            longtitude_list.append(long)
            latitude_list.append(lat)
    #This step will divide the provided distance_range to sub-region
    range_One = distance_range/3
    range_Two = distance_range/3*2
    range_Three =distance_range


    #First calculate points that is within  range_One from the given longittude and latittude
    first_result =[]
    tracking1 = 0
    for x in ids:
        long_val1 = longtitude_list[tracking1]
        lat_val1 =  latitude_list[tracking1]

        # Calculation of distance starts here
        # Declaration: The distance calculation method is extracted from online resources.
        # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1 = radians(longitude_value)
        lon2 = radians(float(long_val1))
        lat1 = radians(latitude_value)
        lat2 = radians(float(lat_val1))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis / 111
        if dis_In_Degree <= range_One:
            first_result.append(x)
        tracking1 =tracking1 +1

    print(len(first_result))
    #print(first_result)
    print('-----------------------------------------------------Query 5 Method 2 Implementation (linear scan)-------------------------------------------------------------------------')
    print('######################The following is the query execution results############################################')
    print('For the given longitude and latitude, it has ' + str(len(first_result)) + ' accident  between the given point and its ' + str(math.ceil(range_One * 111)) + ' KM range.')






    #Second calculate point that is between range_one and range_two from the given longitude and latitude
    second_Result = []
    tracking2 = 0
    for xx in ids:
        long_val2 = longtitude_list[tracking2]
        lat_val2 =  latitude_list[tracking2]

        # Calculation of distance starts here
        # Declaration: The distance calculation method is extracted from online resources.
        # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1 = radians(longitude_value)
        lon2 = radians(float(long_val2))
        lat1 = radians(latitude_value)
        lat2 = radians(float(lat_val2))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis / 111

        if dis_In_Degree>range_One and dis_In_Degree<=range_Two:
            second_Result.append(xx)
        tracking2 =tracking2 + 1

    print('For the given longitutde and latitude, it has ' + str(len(second_Result)) + ' accident between ' + str(math.ceil(range_One * 111)) + ' and ' + str(math.ceil(range_Two * 111)) + ' KM range from the giveen longitutde and latitude point')






    #Third calculate point that is between range_two and range_three from the given longitude and latitude
    third_result =[]
    tracking3 = 0
    for yy in ids:
        long_val3 = longtitude_list[tracking3]
        lat_val3 = latitude_list[tracking3]

        # Calculation of distance starts here
        # Declaration: The distance calculation method is extracted from online resources.
        # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1 = radians(longitude_value)
        lon2 = radians(float(long_val3))
        lat1 = radians(latitude_value)
        lat2 = radians(float(lat_val3))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis / 111
        if dis_In_Degree>range_Two and dis_In_Degree<=range_Three:
            third_result.append(yy)
        tracking3 = tracking3 +1
    print('For the given longitude and latitude, it has ' + str(len(third_result)) + ' accident between ' + str(math.ceil(range_Two * 111)) + ' and ' + str(math.ceil(range_Three * 111)) + ' KM range from the given longitude and latitude point')
    query_End_Time =(datetime.datetime.now()-query_Start_time).total_seconds()
    process1 =psutil.Process()
    query_Memory = process1.memory_info().rss
    print('#################################################The performance information is shown as following###########################################################################')
    print('Linear scan does not involve indexing procedures, so indexing performance information is not available here')
    print('The time it takes to query is:'+str(query_End_Time)+'seconds')
    print('The memory cost it takes to query is:'+str(query_Memory)+'bytes')



#case 1
Query5Method2(-111.909060,33.429259,0.05405405)



