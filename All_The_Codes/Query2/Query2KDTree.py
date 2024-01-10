# Query 2 Method 1 implementation starts here, using KD Tree to solve the problem


#Import all the required libraries here
import csv
import datetime
from math import radians, cos, sin, asin, sqrt
import os, psutil
import quads
import numpy as np
from scipy.spatial import KDTree



def query2Method1(idNumber,k_Value):
    #Declare all the variables here
    ids =[]
    longtitude_list =[]
    latitude_list =[]
    severity_rate = []



    # This with open will open the Us accident dataset and append longtitude, latitude, id and severity of each line to the correpsonding list
    with open('US_Accidents_Dec21_updated.csv') as accident_CSV:
        reader = csv.reader(accident_CSV)

        next(reader)


        for line in reader:
            id = line[0]
            longtitude = line[5]
            latitude =line[4]
            longtitude_list.append(longtitude)
            latitude_list.append(latitude)
            ids.append(id)
            severity_rate.append(line[1])






    #Turn longtitude_list and latitude_list created above to numpy array format
    numpy_Longtitude = np.array(longtitude_list)
    numpy_Latitude = np.array(latitude_list)

    #Use the converted numpy arrays above to create pairs, which is called all_the_pairs
    all_the_pairs = np.c_[numpy_Longtitude, numpy_Latitude]

    #Substitute all_the_pairs into KDTree to create the KDTree object and call it tree
    tree = KDTree(all_the_pairs)


    #Track index
    track_Index = 0
    #Target longtitude
    target_long =0
    #Target latitude
    target_lat =0
    #Target index
    target_Index =0
    #Target_severity
    target_severity =0
    #This for loop try to finds all the relevant information of the id provodied in the function parameter. Store these information in the variables declare above
    for x in ids:
        if x==idNumber:
            target_Index=track_Index
            break
        track_Index = track_Index+1
    target_long = longtitude_list[target_Index]
    target_lat =latitude_list[target_Index]
    target_severity =severity_rate[target_Index]

    #Declare variables
    newID =[]
    new_long =[]
    new_lat =[]
    new_severity =[]

    #This with open will open the US accident csv. And
    #For each row, it will inspect the severity value and check if it is the same as the target severity we obtained above
    #If a row's severity value matches the target severity we obtained above, it will grab all the relevant information and
    #stores in the lists we created above
    with open('US_Accidents_Dec21_updated.csv') as TrafficAccident:
        reader2 = csv.reader(TrafficAccident)
        next(reader2)

        for row in reader2:
            if row[1]==target_severity:
                newID.append(row[0])
                new_long.append(row[5])
                new_lat.append(row[4])
                new_severity.append(row[1])

    #Convert the new_long and new_lat lists to numpy array format
    new_numpy_long = np.array(new_long)
    new_numpy_lat = np.array(new_lat)
    #Use the numpy arrays above to create pairs
    new_all_pairs = np.c_[new_numpy_long,new_numpy_lat]
    #Substitute the pairs created above into KDTree and created the KDTree object new_Tree
    process1 = psutil.Process()
    index_memory_cost1 = process1.memory_info().rss
    start_index_time = datetime.datetime.now()
    new_Tree = KDTree(new_all_pairs)
    end_index_time =(datetime.datetime.now()-start_index_time).total_seconds()
    process2 = psutil.Process()
    index_memory_cost2 = process2.memory_info().rss
    #Use the target_long and target_lat above as the first parameter of the query, and use the function parameter input k_value as the second input to the query
    query_start_time = datetime.datetime.now()
    dd, ii =new_Tree.query([[target_long,target_lat]],k_Value)
    query_end_time =(datetime.datetime.now()-query_start_time).total_seconds()

    process3 = psutil.Process()
    index_memory_cost3 = process3.memory_info().rss

    print(dd)
    print(ii)
    #We get dd and ii. dd is the distances, and ii is the indicies
    #The indices are related to how we create the KDTree, which can refer to line 102.
    #In line 102, we use new_all_pairs to create the tree.
    #new_all_pairs is created by the converted numpy arrays
    #the converted numpy arrays are created by new_long and new_lat
    #new_long and new_lat depend on the severity values of each row in the dataset
    #loop through the indicies, for each indicies, place it in the newID list to obtain the real ID from the US accident dataset
    print('-------------------------------------------------------Query 2 method 1 Implementation------------------------------------------------------')
    print('The time it takes for indexing is:'+str(end_index_time)+'seconds')
    print('The memory cost it takes for indexing is:'+str(index_memory_cost2)+'bytes')
    #print(index_memory_cost1)
    print('The time it takes to query is:'+str(query_end_time)+'seconds')
    print('The memory cost it takes for querying is:'+str(index_memory_cost3)+'bytes')
    print('#####################These are the obtained results for the query#####################################')
    for x in ii:
        for y in x:
            print(newID[y])
    #process3 = psutil.Process()
    #index_memory_cost3 = process3.memory_info().rss



#Case 1
#query2Method1('A-1',6)

#Case 2
#query2Method1('A-1000',3)


#case 3
query2Method1('A-50',4)







