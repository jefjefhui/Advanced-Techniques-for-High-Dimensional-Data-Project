#Query 3 method 2 implementation, liner scan
#Query 3 statements: Given a region(bounding rectangle), find the accident that last the longest and the accident that last the least amount of time
import csv
import datetime

import psutil


#Import all the libraries here




def Query3Method2(minLon,minLat,maxLon,maxLat):
    query_Start_time = datetime.datetime.now()
    ids = []
    start_lat =[]
    start_lon =[]
    start_Time = []
    end_time = []
    track_Index =0
    track_Index_List = []
    within_Region_Results = []
    distance_Calculation  = {}
    track_Index2 = 0

    #Step one: Find all the accidents that are within the bounding box region
    #Extract all the relevant information from the dataset
    with open('US_Accidents_Dec21_updated.csv') as accidents:
        reader = csv.reader(accidents)
        next(reader)
        for row in reader:
            ids.append(row[0])
            start_lat.append(row[4])
            start_lon.append(row[5])
            start_Time.append(row[2])
            end_time.append(row[3])
            track_Index_List.append(track_Index)
            track_Index = track_Index +1

    #This for loop for filer all the accident that is not in the stated region
    for x in track_Index_List:
        current_long =float(start_lon[x])
        current_lat = float(start_lat[x])
        if(current_long<=maxLon and current_long>=minLon):
            if(current_lat<=maxLat and current_lat>=minLat):
                within_Region_Results.append(x)


    print(len(within_Region_Results))
    #This for loop will do couple things
    #Firsly, it will loop through the accidents that is within the qualified region
    #Secondly, for each within region accident, it will do string slicing on the start time and end time, so that it can identify the time compoents in each timestamp
    #Thirdly, using the sliced compoenents to create the timestamps objects for both start and end time
    #Then, you can find out the duration or the difference between the start and end time
    #Pair it with the corresponding id and insert it into the dictionary
    for x in within_Region_Results:
        current_start_time = start_Time[x]
        current_end_time = end_time[x]

        #As current_start_time is just a string, we need to extract the elements in the string and place it into the datetime class to create as a datetime object
        start_Year = int(current_start_time[0:4])
        start_month = int(current_start_time[5:7])
        start_day = int(current_start_time[8:10])
        start_hour = int(current_start_time[11:13])
        start_min = int(current_start_time[14:16])
        start_sec = int(current_start_time[17:19])
        start_after_sec =0
        if(len(current_start_time)>19):
            start_after_sec = int(current_start_time[20:])

        end_year = int(current_end_time[0:4])
        end_month =int(current_end_time[5:7])
        end_day = int(current_end_time[8:10])
        end_hour =int(current_end_time[11:13])
        end_min = int(current_end_time[14:16])
        end_sec  = int(current_end_time[17:19])
        end_after_sec =0
        if(len(current_end_time)>19):
            end_after_sec = int(current_end_time[20:])

        starting =0
        if(start_after_sec!=0):
            starting = datetime.datetime(start_Year,start_month,start_day,start_hour,start_min,start_sec,start_after_sec)
        else:
            starting =datetime.datetime(start_Year,start_month,start_day,start_hour,start_min,start_sec)

        ending = 0
        if(end_after_sec!=0):
            ending =datetime.datetime(end_year,end_month,end_day,end_hour,end_min,end_sec,end_after_sec)
        else:
            ending = datetime.datetime(end_year,end_month,end_day,end_hour,end_min,end_sec)

        timeDifference = (ending-starting).total_seconds()


        id = ids[x]

        distance_Calculation[id] = timeDifference
    #This part sort the dictionary, so that the first item is the accident that takes the shortest time and the last item in the dictionary is the accident that take the longest time
    sorted_dict = sorted(distance_Calculation.items(), key=lambda x: x[1])

    query_End_time =(datetime.datetime.now()-query_Start_time).total_seconds()
    process1 = psutil.Process()
    query_Memory = process1.memory_info().rss

    print('-----------------------------------------------------Query3 Method 2 Implementation---------------------------------------------------')
    print('Indexing does not involve indexing procedures, so indexing information are not available for this method')
    print('The time it takes to query is:'+str(query_End_time)+'seconds')
    print('The memory cost it takes for query is:'+str(query_Memory)+'bytes')
    print('The following is the accident ID that take the least amount of time:')
    print(sorted_dict[0])
    print('The following is the accident ID that take the largest amount of time:')
    print(sorted_dict[-1])





    #Step two: After getting all the accidents that are within the bounding box region, start calculating
    # the time difference and find out which has the largest different and which has the smallest difference.



# case 1
#Query3Method2(-121.517834,38.556757,-121.474902,38.588344)

#case 2
Query3Method2(-121.935904,37.242877,-121.840773,37.356559)
