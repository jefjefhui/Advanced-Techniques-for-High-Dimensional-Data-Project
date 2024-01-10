#Import all the packages or libraries here
import csv
import datetime
from math import radians, cos, sin, asin, sqrt
import os, psutil

#This is the second approch to solve query one. This is using the baseline linear scan
def Q1Linear(longtitude, latitude, dateTime,rangeKM):
    ids = []
    start_position =[]
    withinRangeItems = []
    final_results = []
    begin_Time =0
    endding_Time =0
    total_Time =0
    entire_Program_End =0
    total_Memory =0
    total_Memory2 =0

    #Start making the ids list and the start_position list here, which have similar purpose with indexing in R-Tree
    #Start the timer from here
    begin_Time = datetime.datetime.now()

    #Grab the positions, and id, append to the list
    with open('US_Accidents_Dec21_updated.csv') as accident_CSV:
        reader = csv.reader(accident_CSV)

        next(reader)
        for line in reader:
            position_pair = []
            position_pair.append(float(line[5]))
            position_pair.append(float(line[4]))
            start_position.append(position_pair)
            ids.append(line[0])
    #Timer stops here
    endding_Time = datetime.datetime.now()
    # Get the total time it takes to build both list
    total_Time = (endding_Time-begin_Time).total_seconds()
    #Getting memory cost from here
    process1 = psutil.Process()
    total_Memory = process1.memory_info().rss




    #Find out all the points that are within the required range
    # Calculation of distance for this section
    # Declaration: The distance calculation method is extracted from online resources.
    # Reference/source of method: https://www.geeksforgeeks.org/program-distance-two-points-earth/
    trackIndex = 0
    for x in start_position:
        lon1 = radians(longtitude)
        lon2 = radians(x[0])
        lat1 = radians(latitude)
        lat2 = radians(x[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        radius = 6371
        ans_dis = c * radius
        dis_In_Degree = ans_dis / 111
        # Check if the distance within or equal the specific range value
        # convert_KM_To_Degree0 = 1/111
        convert_KM_To_Degree = (1 / 111) * rangeKM
        if dis_In_Degree<=convert_KM_To_Degree:
            #withinRangeItems[ids[trackIndex]] = x
            withinRangeItems.append(ids[trackIndex])
        trackIndex = trackIndex + 1

    #Start filtering result by dateTime
    with open('US_Accidents_Dec21_updated.csv') as accident:
        reader2 = csv.reader(accident)

        next(reader2)
        for b in withinRangeItems:
            for line in reader2:
                idNumber = line[0]
                start_Time =line[2]
                end_Time =line[3]
                if b == idNumber:
                    if start_Time.startswith(dateTime) and end_Time.startswith(dateTime):
                        final_results.append(idNumber)
                    break
    #This captures the end time for the entire program
    entire_Program_End = datetime.datetime.now()
    #This captures the memory cost for the entire program
    process2=psutil.Process()
    total_Memory2 =process2.memory_info().rss



    print(len(final_results))
    print(final_results)
    print('----------Query 1 Implementation Method 2, Linear Scan----------')
    print('Time it takes to index:'+str(total_Time)+'seconds')
    print('Memory cost it takes to index:'+str(total_Memory)+'bytes')
    print('Time it takes to query:'+str((entire_Program_End-begin_Time).total_seconds()-total_Time)+'seconds')
    print('Memory cost it takes to query:'+str(total_Memory2-total_Memory)+'bytes')
    print('########## These are the result ID##########')
    print(final_results)




#Case 1
#Q1Linear(-112.074036,33.448376,'2021-12-25',10)


#Case 2
#Q1Linear(-122.180358,47.615825,'2020-12-05',15)



#Case 3
#Q1Linear(-122.200676,47.610378,'2021-12-24',15)


#Case4
Q1Linear(-118.243683,34.052235,'2020-01-01',5)










#Need to add information of total time it takes, and memory cost, for querying



        #for line in reader2:
         #   idNumber = line[0]
          #  start_time =line[2]
           # end_time = line[3]
            #for b in withinRangeItems:
             #   if idNumber==b:
              #      if start_time.startswith(dateTime) and end_time.startswith(dateTime):
               #         final_results.append(idNumber)



















