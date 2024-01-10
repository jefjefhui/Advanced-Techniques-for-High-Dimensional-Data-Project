# Query 5 implementation (KD-Tree)
#Query 5 statements: Given a point, search all accidents that are within x km range of the given point
# In addition, need to dissect the searching region  into 3 intervals, which can benefit for partial range analysis

# Import all the required libraries here
import csv
import datetime
from math import radians, cos, sin, asin, sqrt
import os, psutil
import numpy as np
from scipy.spatial import KDTree
import math


def Query5Method1(longtitude_value, latittude_value,distance_range):

    ids =[]
    longtitude_list = []
    latitude_list =[]

    index_start_time = datetime.datetime.now()
    #This with open block will open the dataset, then it will extract all the relevant information and store them in the corresponding lists, which can be used in following procedures
    with open('US_Accidents_Dec21_updated.csv') as traffic_Accident:
        reader = csv.reader(traffic_Accident)

        next(reader)

        for line in reader:
            id = line[0]
            longtitude = line[5]
            latitude =line[4]
            longtitude_list.append(longtitude)
            latitude_list.append(latitude)
            ids.append(id)


    #Turn longtitude list and latitude list created above to numpy array format
    numpy_Longtitude = np.array(longtitude_list)
    numpy_Latitude = np.array(latitude_list)


    #Use the coverted numpy arrays above to create pairs, which is called all_the_pairs
    all_the_pairs = np.c_[numpy_Longtitude,numpy_Latitude]


    #create the KD tree object
    tree =KDTree(all_the_pairs)

    #Get the indexing time and memory from here
    index_End_time = (datetime.datetime.now()-index_start_time).total_seconds()
    process1 = psutil.Process()
    index_Memory = process1.memory_info().rss


    query_start_Time = datetime.datetime.now()
    #try to divide the region into three areas for more detailed analysis
    first_Upper = distance_range/3
    second_Upper = distance_range/3*2
    third_upper = distance_range





    # longtitude = -111.909060   latitude = 33.429259

    #Call the KDTree within range distance function, which will obtain all the data points within the distance range of a specific point
    x =tree.query_ball_point([[longtitude_value,latittude_value]],first_Upper)

    print(x)
    print(x[0])
    print(len(x[0]))

    first_List = x[0]

    first_Region_Length = len(x[0])
    print('--------------------------------------------------------------------------Query 5 Method 1 Implementation KD-Tree-------------------------------------------------------------------------------------------')
    print('##############################################The following shows the query execution results#####################################################################')
    print('For the given longitude and latitude, it has '+str(first_Region_Length)+ ' accident  between the given point and its '+str(math.ceil(first_Upper*111))+' KM range.')


    #Search for the second region
    y = tree.query_ball_point([[longtitude_value, latittude_value]], second_Upper)

    second_List = y[0]

    #checker = False
    #checker2 = False
    #not_qualified = []
    #qualified = []
    #track_Index = 0

    #for stuff in second_List:
        #if checker==True:
          #  not_qualified.append(second_List[track_Index-1])
         #   checker==False
        #if checker ==False and checker2==True:







        #for things in first_List:
          #  if stuff==things:
         #       checker =True
        #        break


       # track_Index = track_Index + 1

    #This step is very important. You need to minus first_list to get the right results. And it can be explained by a simple example below
    #If first_list stores data points that are within 2km distance range from point A. If you look for the points between 2km to 4km from point A,
    #You should find all points within 4km distance range of point A, then minus all points within 2km distance range rom point A. If you don't minus the points within 2km range of point A
    #you are not finding points between 2km and 4km, you are finding points that are within 4km distance range from point A, which is not what I am looking for, as
    #we are inspecting the sub-region of a given distance range.
    second_Result = list(set(second_List)-set(first_List))


    print('For the given longitutde and latitude, it has '+str(len(second_Result))+' accident between '+str(math.ceil(first_Upper*111))+' and '+str(math.ceil(second_Upper*111))+' KM range from the giveen longitutde and latitude point')

    #search for the third region
    z = tree.query_ball_point([[longtitude_value, latittude_value]], third_upper)
    third_List = z[0]
    #Same as the reason explained above, you should minnus second_list to get the sub-region results
    third_result = list(set(third_List)-set(second_List))
    print('For the given longitude and latitude, it has '+ str(len(third_result))+' accident between '+str(math.ceil(second_Upper*111))+' and '+str(math.ceil(third_upper *111))+' KM range from the given longitude and latitude point')
    query_end_time = (datetime.datetime.now()-query_start_Time).total_seconds()
    process2 =psutil.Process()
    query_Memory = process2.memory_info().rss
    print('##################################################The following shows some performance information of the query execution#######################################################################')
    print('The time it takes to index is:'+str(index_End_time)+'seconds')
    print('The memory cost it takes to index is:'+str(index_Memory)+'bytes')
    print('The time it takes to query is:'+str(query_end_time)+'seconds')
    print('The memory cost it take to query is:'+str(query_Memory)+'bytes')


















#Case 1
Query5Method1(-111.909060,33.429259,0.05405405)
















