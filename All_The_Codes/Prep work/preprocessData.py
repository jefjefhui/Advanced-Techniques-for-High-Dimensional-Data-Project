import csv

with open("US_Accidents_Dec21_updated.csv","r") as source:
    reader = csv.reader(source)

    with open("processed_Data_Final.csv","w") as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[15],r[16],r[18],r[20],r[25],r[27],r[28],r[29],r[43]))



