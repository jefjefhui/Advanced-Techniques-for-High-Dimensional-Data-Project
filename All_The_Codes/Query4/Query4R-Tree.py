#This is Query 4 Implementation, Method 1 R-Tree
#Query statement of Query 4: Given a region, find all the accident points within the region.
#For each point, find how many accidents are within its 5 km distance range
#Compare the results, so you can find the traffic accident hotspots within the specific region

#Import all the libraries here
import utm
import csv
import datetime
from rtree import index
from math import radians, cos, sin, asin, sqrt
import os, psutil
import pyproj as proj


def Query4Method1(minLon,minLat,maxLon,maxLat):
    ids = []
    severity_value =[]
    tracking_Num =0
    severity_One = 0
    severity_Two = 0
    severity_Three = 0
    severity_Four = 0



    index_Start_time =datetime.datetime.now()
    idx1 = index.Index()
    #Open the dataset and insert data into the index to create the index
    with open('US_Accidents_Dec21_updated.csv') as accident_CSV:
        reader = csv.reader(accident_CSV)

        next(reader)

        for row in reader:
            severity_value.append(row[1])
            ids.append(row[0])
            idx1.insert(tracking_Num,(float(row[5]), float(row[4]), float(row[5]), float(row[4])))
            tracking_Num = tracking_Num + 1
    index_End_Time = (datetime.datetime.now()-index_Start_time).total_seconds()
    process1 = psutil.Process()
    index_Memory = process1.memory_info().rss
    query_start_time = datetime.datetime.now()
    #R-Tree intersection function to obtain the qualified results
    intersection_Reuslt = list(idx1.intersection((minLon,minLat,maxLon,maxLat)))

    print('The length is'+str(len(intersection_Reuslt)))

    print(intersection_Reuslt[0:5])
    print('hello')
    #Loop through the intersection_result(which are the qualified, within region items).
    #For each qualified items, check its severity value.
    # If the severity value is 1, add 1 to severity_One
    #If the severity value is 2, add 1 to severity_Two
    #If the severity value is 3, add 1 to severity_Three
    #If the severity value is 4, add 1 to severity_four
    #This will count the how many accidents in each severity level
    for x in intersection_Reuslt:
        print(type(severity_value[x]))
        print(severity_value[x])
        if severity_value[x]==str(1):
            severity_One =severity_One +1
        elif severity_value[x]==str(2):
            severity_Two =severity_Two + 1
        elif severity_value[x]==str(3):
            severity_Three = severity_Three +1
        else:
            severity_Four = severity_Four +1





    #The follow 4 lines of codes will calculate the percentage of number of accidents in each severity level to the entire search region's total amount of accidents
    ratioOne = severity_One/len(intersection_Reuslt)*100
    ratioTwo  = severity_Two/len(intersection_Reuslt)*100
    ratioThree = severity_Three/len(intersection_Reuslt)*100
    ratioFour = severity_Four/len(intersection_Reuslt)*100

    query_end_time = (datetime.datetime.now()-query_start_time).total_seconds()
    process2 = psutil.Process()
    query_Memory = process2.memory_info().rss


    print('-------------------------------------------------------Query 4 Method 1 R-Tree-----------------------------------------------------------------------------')
    print('The total time it takes to index is: '+str(index_End_Time)+' seconds')
    print('The total memory cost it takes for index is: '+str(index_Memory)+' bytes')
    print('The total time it takes to query is: '+str(query_end_time)+' seconds')
    print('The memory cost it takes to query is:'+str(query_Memory)+'bytes')

    print('######These are the query output results##############')
    print('Severity 1 has'+str(severity_One)+'values. And the percentage is'+str(ratioOne)+'%')
    print('Severity 2 has'+str(severity_Two)+'values. and the percentage is'+str(ratioTwo)+'%')
    print('Severity 3 has'+str(severity_Three)+'values and the percentage is'+str(ratioThree)+'%')
    print('Severity 4 has'+str(severity_Four)+'values and the percentage is'+str(ratioFour)+'%')




#top left: 33.462049, -112.107335
#top right: 33.462049  -112.051760
#




            #Preprocessing of longtitude and latitude before starts creting the index
            #x, y =utm.from_latlon(row[4],row[5])

   # x, y,z,c = utm.from_latlon(	33.448376, -112.074036)
    #print('These are the first sets of outcome:')
    #print(x)
    #print(y)


    #print('These are the second set of outcome')
    # setup your projections
    #crs_wgs = proj.Proj(init='epsg:4326')  # assuming you're using WGS84 geographic
    #crs_bng = proj.Proj(init='epsg:27700')  # use a locally appropriate projected CRS
    #a, b = proj.transform(crs_wgs, crs_bng, -112.074036, 33.448376)
    #print(a)
    #print(b)
    #x = 6371 * cos(33.448376) * cos(-112.074036)
    #y = 6731 * cos(33.448376) * sin(-112.074036)
    #print(x)
    #print(y)

#Case 1
Query4Method1(-112.107335,33.367202,-112.051760,33.462049)








