#Query 4 Method 2, linear scan

# import all theclibraries here
import utm
import csv
import datetime
from rtree import index
from math import radians, cos, sin, asin, sqrt
import os, psutil
import pyproj as proj


def Q4Method2(minLon,minLat,maxLon,maxLat):
    query_start_time  = datetime.datetime.now()

    ids = []
    tracking_num = 0
    start_Position = []
    severity_Value =  []
    result_List = []
    severity_One = 0
    severity_Two = 0
    severity_three = 0
    severity_Four = 0


    #Extract all the information from the dataset
    with open('US_Accidents_Dec21_updated.csv') as accidentCSV:
        reader = csv.reader(accidentCSV)
        next(reader)
        for row in reader:
            ids.append(row[0])
            make_pair =[]
            make_pair.append(row[5])
            make_pair.append(row[4])
            start_Position.append(make_pair)
            severity_Value.append(row[1])
    #This for loop will iterate through the start_Position list, which contains the longtitude and latitude
    #For each pair of values in start_Position, do the checkings on the longitude and latitude values, ensure
    #they are within the stated region
    #If the pair is within the stated region, then append the result_list
    #Iterate through the start_position list  until the entire list is iterated
    for x in start_Position:
        longtitude = float(x[0])
        latitude = float(x[1])
        #print(type(longtitude))
        #print(type(latitude))
        if longtitude>=minLon and longtitude<=maxLon:
            if latitude>=minLat and latitude<=maxLat:
                result_List.append(tracking_num)
        tracking_num = tracking_num +1

    #The reuslt_list stores all the result that are within the stated region
    #The following for  loop will iterate through the result_list, check the severity value for each accident and add 1 to corresponding
    #varables accordingly.
    for y in result_List:
        checking_Value  = severity_Value[y]
        if int(checking_Value) == int(1):
            severity_One = severity_One + 1
        elif int(checking_Value) == int(2):
            severity_Two = severity_Two +1
        elif int(checking_Value) == int(3):
            severity_three =severity_three + 1
        else:
            severity_Four = severity_Four + 1

    #This part will calculate the percentage. The number of accidents in each severity to all the accidents in the stated region
    ratioOne = severity_One / len(result_List) * 100
    ratioTwo =  severity_Two / len(result_List) * 100
    ratioThree = severity_three / len(result_List) * 100
    ratioFour =  severity_Four / len(result_List) * 100

    query_End_time = (datetime.datetime.now()-query_start_time).total_seconds()
    process1 = psutil.Process()
    query_Memory = process1.memory_info().rss

    print('-------------------------------------------------Query 4 Method 2 Implementation (Linear Scan)----------------------------------------------')
    print('Linear scan does not have the indexing procedures, so the indexing information is not available in this step')
    print('The time it takes to query is:'+str(query_End_time)+'seconds')
    print('The memory cost it takes to query is:'+str(query_Memory)+'bytes')
    print('##############The output results are shown below############################')
    print('Severity 1 has'+str(severity_One)+'values. And the percentage is'+str(ratioOne)+'%')
    print('Severity 2 has'+str(severity_Two)+'values. And the percentage is'+str(ratioTwo)+'%')
    print('Severity 3 has'+str(severity_three)+'values. And the percentage is'+str(ratioThree)+'%')
    print('Severity 4 has'+str(severity_Four)+'values. And the percentage is'+str(ratioFour)+'%')



Q4Method2(-112.107335,33.367202,-112.051760,33.462049)




















