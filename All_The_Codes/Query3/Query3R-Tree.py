#Query 3 Method 1 implementation starts here
#Query 3 statements: Given a region, find the accident that last the least amount of time  and return it
#Implementation starts from here
import csv

#Import all the required libraries here
from rtree import index
import datetime
from collections import OrderedDict
import os, psutil

def Query3Method1Implementation(minLongtitude,minLatitude,maxLongtitude,maxLatitude):
    #declare variables here
    ids =[]
    start_time = []
    end_time =[]
    calculated_answers = []





    #create the index object here
    idx = index.Index()

    track_Index = 0

    index_Start_Time = datetime.datetime.now()
    with open('US_Accidents_Dec21_updated.csv') as USAccident:

        reader = csv.reader(USAccident)
        next(reader)
        for row in reader:
            start_time.append(row[2])
            end_time.append(row[3])
            ids.append(row[0])
            idx.insert(track_Index,(float(row[5]),float(row[4]),float(row[5]),float(row[4])))
            track_Index = track_Index +1
    index_End_Time = (datetime.datetime.now()-index_Start_Time).total_seconds()
    process1 = psutil.Process()
    index_Memory_Cost  = process1.memory_info().rss
    print(len(ids))
    print(len(start_time))
    print(len(end_time))
    print(track_Index)

    query_Start_time = datetime.datetime.now()
    #Use the R-tree index to search for the accidents within the region
    answer = list(idx.intersection((minLongtitude,minLatitude,maxLongtitude,maxLatitude)))

    print(len(answer))

    print(answer[:10])

    print(type(answer))

    keep_Track =0
    the_dict = {}
    #In the first part of the for loop, these codes are working on slicing the string, so that it can identify the timestamp components clearly
    #Slicing the string and assign to corresponding variables, which will be used to create the timestamp object
    #In the second part of the for loop, it according to the variables values to create the start time timestamp object and the end time timestamp object
    # In the third part of the for loop, it calculates the time difference(duration) and pair with the corresponding ID and assign to the dictionary
    for x in answer:
        starting = start_time[x]
        ending = end_time[x]
        starting_year = int(starting[0:4])
        starting_month = int(starting[5:7])
        starting_day = int(starting[8:10])
        starting_hour = int(starting[11:13])
        starting_min = int(starting[14:16])
        starting_sec = int(starting[17:19])
        starting_After_Sec = 0
        if(len(starting)>19):
            starting_After_Sec = int(starting[20:])
        ending_year = int(ending[0:4])
        ending_month = int(ending[5:7])
        ending_day = int(ending[8:10])
        ending_hour = int(ending[11:13])
        ending_min = int(ending[14:16])
        ending_sec = int(ending[17:19])
        ending_after_sec = 0
        if(len(ending)>19):
            ending_after_sec = int(ending[20:])

        startingObj = 0
        if(starting_After_Sec!=0):
            startingObj = datetime.datetime(starting_year,starting_month,starting_day,starting_hour,starting_min,starting_sec,starting_After_Sec)
        else:
            startingObj = datetime.datetime(starting_year, starting_month, starting_day, starting_hour, starting_min,
                                            starting_sec)
        endingObj = 0
        if(ending_after_sec!=0):
            endingObj = datetime.datetime(ending_year,ending_month,ending_day,ending_hour,ending_min,ending_sec,ending_after_sec)
        else:
            endingObj = datetime.datetime(ending_year,ending_month,ending_day,ending_hour,ending_min,ending_sec)

        the_Difference = (endingObj-startingObj).total_seconds()

        the_dict[ids[x]] = the_Difference
    print(len(the_dict))
    print(len(answer))
    #print(the_dict)

    #sorted_Resulted = sorted(the_dict)
    #print(sorted_Resulted)

    #print(type(sorted_Resulted))
    #print(sorted_Resulted[0])
    #print(sorted_Resulted[-1])
    #print(the_dict[sorted_Resulted[0]])
    #print(the_dict[sorted_Resulted[-1]])

    #res =list(sorted_Resulted.keys())[0]
    #print(res)


    #print(the_dict['A-1793700'])


    #Sort the dictionary by the time difference(accident duration), so that the first item is the one with the shortest time and the last item is the item with the longest time
    sorted_theDict = sorted(the_dict.items(), key=lambda x: x[1])

    print(sorted_theDict)
    query_End_time = (datetime.datetime.now()-query_Start_time).total_seconds()
    process2 =psutil.Process()
    query_Memory = process2.memory_info().rss

    print('------------------------------------------------Query 3 Method 1 Implementation--------------------------------------------------')
    print('The indexing time is:'+str(index_End_Time)+'seconds')
    print('The indexing memory cost is'+str(index_Memory_Cost)+'bytes')
    print('The query time is:'+str(query_End_time)+'seconds')
    print('The query memory cost is:'+str(query_Memory)+'bytes')

    print('The following is the accident ID that take the least amount of time and also within the stated region:')
    print(sorted_theDict[0])
    print('The following is the accident ID that take the largest amount of time and also within the stated region:')
    print(sorted_theDict[-1])























        #timeDiff = ending - starting
        #calculated_answers.append(timeDiff)

    #print(type(start_time[0]))






#case 1
#Query3Method1Implementation(-121.517834,38.556757,-121.474902,38.588344)


#case 2
Query3Method1Implementation(-121.935904,37.242877,-121.840773,37.356559)

#-121.935904  37.356559
#-121.840773   37.356559
# -121.935904  37.242877
# -121.840773  37.242877

# -121.517834,38.588344 same y
# -121.474902            38.588344 same y
#-121.517834, 38.556757
#-121.474902,38.556757
#min x=-121.474902      max x =-121.517834
#miny =38.556757   maxy=38.588344









