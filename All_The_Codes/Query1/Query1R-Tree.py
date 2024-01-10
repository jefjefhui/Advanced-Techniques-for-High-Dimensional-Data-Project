#Query 1 implementation
#Query: People usually go out and celebrate on christmas day. For query one,
#please find out all the accidents within 10KM range of Phoenix,AZ on christmas day in 2021.
#You can use longtitude:-112.074036 and latitude:33.448376 as the reference location of Phoenix,AZ
#You can use 2021-12-25 as the date of christmas day

#Import all the required libraries here
import csv
import datetime
import math

from math import radians, cos, sin, asin, sqrt
import os, psutil
import quads


def queryOne(longitude,latitude,dateTime,range_KM):
    from rtree import index

    #Declare some variables from here
    #idx1 is the index object from R-Tree
    idx1 = index.Index()
    #ids will store all the IDs
    ids =[]
    # index is used when inserting records to the index. It starts from 0, and it is parallel with ids.
    # In example, id=0 in the index contains 1st row information within the dataset, ids[0] also contains 1st row ID in the dataset
    index = 0
    #longtitude,latitude pair values are stored within lnlat. For instance, lnglat[0] can retrieve first row longtitude, latitude pair values from the dataset
    lnglat =[]
    #toggle is a condition, it checks if the k value of nearest neighbor needs to increment or not.
    toggle = True
    currentDist=True
    #Record the k value of the nearest neighbor.When the loop is overed, the possible max value of k will be stores in NNVal. It starts from 1
    NNVal=1
    within_Range_Time = []
    #After getting the nearest neighbor results, convert these result values to actual ids in the dataset and store them in NN_Result_ActualID
    NN_Result_ActualID = []
    #time_values store the start_time and end_time pair for each row of data in the dataset
    time_values =[]
    #After getting the NN results, we need to get the corresponding time values(Start time and end time), the corresponding start time and end time for each NN will store in target_time_values
    target_time_values =[]
    # Originally, countingcounting is used to store the positions of the unqualified items in target_time_values, which
    #can be used to remove unqulified items in final_NN_Reuslt, but it doesn't work the way I expect, so countingcounting leave unused at this moment
    countingcounting =[]
    testTest =[]
    loopIDX =[]
    #This number is to track what index it is at when looping through the target_time_values
    indexchecking =0
    # Looping store the position of all the unqualified results during date checking procedures
    looping =[]
    # correct_Results stores the position of all the qualified results during the date checking procedures
    correct_Results = []
    # The values in correct_Results only refer the position(index), we need to loop through correct_results and use
    # the index in correct_Results to find the corresponding r-tree index id in final_NN_Result.
    #After getting the corresponding r-tree index id in final_NN_Result, we can use these values to obain the real id mentioned in the dataset
    filtered_NN_Final =[]
    #indexing_time stores time it takes for creating the index
    indexing_Time=0
    #indexing_Memory_cost  stores the memory cost it takes to create the index
    indexing_Memory_cost=0
    #Total time it takes to run the query
    queying_time =0
    #Total memory cost it takes to run the query
    memory_cost_querying = 0
    #entire_memory_cost stores the total memory cost of the entire program
    entire_memory_cost =0
    #Start time of querying
    query_Start_Time = 0
    #End time of querying
    query_End_Time = 0



    #Open the dataset, start inserting information to the index,append id values and append lnglat values
    #Also, it calculates the total time to prepare the index and appending all the relevant lists
    with open('US_Accidents_Dec21_updated.csv') as accident_CSV:
        reader = csv.reader(accident_CSV)

        next(reader)

        start = datetime.datetime.now()
        for line in reader:
            idx1.insert(index,(float(line[5]),float(line[4]),float(line[5]),float(line[4])))
            ids.append(line[0])
            appVal=[]
            appVal.append(float(line[5]))
            appVal.append(float(line[4]))
            lnglat.append(appVal)

            index=index+1
        indexing_Time =(datetime.datetime.now() - start).total_seconds()
        print('t0:', indexing_Time)
        process1 =psutil.Process()
        indexing_Memory_cost = process1.memory_info().rss
        print(indexing_Memory_cost)

    #This line just test the index by finding the 3 nearest neighbors base on the designated point
    y = list(idx1.nearest((longitude,latitude,longitude,latitude),3))

    #Print the 3 nearest neighbors results
    print(y)
    #Find out what is the data type of the result
    print(type(y))

    # print the 3 NN results coordinates, try to validate the results by the actual coordinate values
    print(lnglat[210601])
    print(lnglat[1226155])
    print(lnglat[1249492])

    #Some testing print statements
    print(toggle)
    print(type(toggle))

    #query time starts counting from here
    #query_Start_Time = datetime.datetime.now()
    # I try to increment the k value of nearest neighbor one by a time.
    #For each k, calcuate the distance between the furthest point and the designated point
    #For instance, when K=5, the distance between the furthest point and the designated point values is within the target range
    #But when k=6, the distance between the furthest point and the designated point value is beyond the target range
    #Then the loop with stopped and the largest possible value of K will be 5
    query_Start_Time = datetime.datetime.now()
    while toggle== True:
        #Get the KNN results. NNVal will increment.
        NNResult = list(idx1.nearest((longitude,latitude,longitude,latitude),NNVal))
        #Get the furthest point
        furthest_Point_id = NNResult[-1]
        #Get the longtitude and latitude values, which will be used to calculate the distance
        furthest_Point_Val = lnglat[furthest_Point_id]
        #Calculation of distance starts here
        # Declaration: The distance calculation method is extracted from online resources.
        # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1 = radians(longitude)
        lon2 = radians(furthest_Point_Val[0])
        lat1 = radians(latitude)
        lat2 = radians(furthest_Point_Val[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1)* cos(lat2) * sin(dlon/2)**2
        c =2* asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis/111
        #Check if the distance beyond the range
        #If it is beyond the target range, then it wil use the previous k value, which can be otained by -1 , and toggle will turn false to end the while loop
        #If it is within the target range, NNVal will add one, and the while loop will continue
        #convert_KM_To_Degree0 = 1/111
        convert_KM_To_Degree = (1/111)*range_KM
        #Correction: Use euclidian distance here
        point_One_Lon = longitude
        point_Two_Lon =furthest_Point_Val[0]
        point_One_Lat = latitude
        point_Two_Lat =furthest_Point_Val[1]
        p1 =[point_One_Lon,point_One_Lat]
        p2 =[point_Two_Lon,point_Two_Lat]
        euclidean_Dist = math.dist(p1,p2)



        if euclidean_Dist>convert_KM_To_Degree:
            NNVal = NNVal-1
            toggle=False
        else:
            NNVal = NNVal+1

    #If NNVal is smaller than one, it means there are no accidents within the target range
    #Otherwise, it means there are accidents within the target range
    #If there are accidents within the target range, we need to proceed the next filtering criteria, which is the date/time criteria, it will process in the else clause
    if NNVal<1:
        print('There are no accidents within the 10KM range distance')
    else:
        #Get all the nearest neighbor results by using the k value we obtained above
        final_NN_Result = list(idx1.nearest((longitude,latitude,longitude,latitude),NNVal))
        # print out the knn results and find out the length of the results
        print(final_NN_Result)
        print(len(final_NN_Result))

        #This for loop will iterate final_NN_Result. For each item, it will get its actual id in the dataset and append to the NN_Result_ActualID list
        for x in final_NN_Result:
            NN_Result_ActualID.append(ids[x])
        # Print the NN_Result_ActualID and find out the length of NN_Result_ActualID
        print(NN_Result_ActualID)
        print(len(NN_Result_ActualID))
        #Open the dataset file, group the start_time and end_time as a pair, then append the pair value to the time_values list
        with open('US_Accidents_Dec21_updated.csv') as USAccident:
            reader2 = csv.reader(USAccident)
            next(reader2)
            for line in reader2:
                timePair =[]
                timePair.append(line[2])
                timePair.append(line[3])
                time_values.append(timePair)
            # print the length of time_values, make sure the process are execute correctly
            print(len(time_values))
        #Append the target_time_values list with the corresponding time values of the items in the final_NN_Result list
        for x in final_NN_Result:
            target_time_values.append(time_values[x])
        #print the length of final_NN_Result and the length of target_time_values. Validate the previous operations by comparing these two length values.
        print(len(final_NN_Result))
        print(len(target_time_values))

        #print the first 10 items of final_NN_Result and the first 10 items of target_time_values. Check the dataset, make sure same index number on both list are refering to the same row of record in the dataset
        print(final_NN_Result[:10])
        print(target_time_values[:10])
        #This for loop iterate all the items in target_time_values, check if these items meet the time/date criteria
        for x in target_time_values:
            start_time = x[0]
            end_time = x[1]

            target_pattern1 = '2021-12-25'
            target_pattern2 = '2021-12-26 00:00:00'
            #This if clause checks the start_time and end_time, it ensures both times are on 2021-12-25
            #if both start_time and end_time starts with 2021-12-25, then append the correct_results list with the current index number, then increment one to index number
            #If it fell to the else clause, it means it doesn't meet the time/date requirement, so it append the list 'looping', which record the invliad results. Then increment one to index number
            if x[0].startswith(dateTime) and x[1].startswith(dateTime):

                correct_Results.append(indexchecking)
                indexchecking= indexchecking+1
                continue
            else:
                remove_IDX = target_time_values.index(x)
                countingcounting.append(remove_IDX)
                looping.append(indexchecking)
                indexchecking=indexchecking+1
        #Print statement for testing purpose
        print(len(countingcounting))
        print(countingcounting[:10])
        #Print statement for testing purpose
        print(len(target_time_values))
        print(target_time_values[:10])
        #Print statement for testing purpose
        print(len(final_NN_Result))
        print(final_NN_Result[:10])
        #Print for testing purpose
        print(len(looping))
        print(looping[:10])
        print(looping[0])
        print(type(looping[0]))

        #Print out length of the target_time_values, length of looping and length of correct_Results. Compare the values, ensure the previous operations are correct
        print(len(target_time_values))
        print(len(looping))
        print(len(correct_Results))
        #Print the index values of the matching items in the target_time_values list
        print(correct_Results)

        #This for loop iterate through the correct_Results list and use the values within correct_Results to obtain the real index id.
        #Afterwards, append the real index id to filtered_NN_Final
        #Print the filtered_NN_Final to verify the results
        for x in correct_Results:
            filtered_NN_Final.append(final_NN_Result[x])
        print(filtered_NN_Final)

        # Iterate the filtered_NN_Final, substitute the real index id to ids and get the real id that appears in the first column of the dataset
        for x in filtered_NN_Final:
            print(ids[x])
        #Couting query time stop here
        query_End_Time =datetime.datetime.now()
        queying_time =(query_End_Time - query_Start_Time).total_seconds()
        process = psutil.Process()
        entire_memory_cost =process.memory_info().rss
        print(entire_memory_cost)

        print('--------------------------------------------------Query 1 Implementation Final Results-----------------------------------------------------')
        print('Time it takes to create the index:'+str(indexing_Time)+'seconds')
        print('Memory cost it takes to create the index is:'+str(indexing_Memory_cost)+'bytes')
        print('Time it takes to query:'+str(queying_time)+'seconds')
        print('Memory cost it takes to query:'+str(entire_memory_cost-indexing_Memory_cost)+'bytes')
        print('#######These are the qualified data rows ID#######')
        for x in filtered_NN_Final:
            print(ids[x])

#Case1
#queryOne(-112.074036,33.448376,'2021-12-25',10)

#case2
#queryOne(-122.180358,47.615825,'2020-12-05',15)


#case 3
#queryOne(-122.200676,47.610378,'2021-12-24',15)

#case 4
#queryOne(-118.243683,34.052235,'2020-01-01',5)