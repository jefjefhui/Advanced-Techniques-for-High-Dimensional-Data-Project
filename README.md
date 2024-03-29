# Advanced-Techniques-for-High-Dimensional-Data-Project


Advanced technique for high dimensional data project 

Multidimensional data indexing project 

The purpose of this project is to help learners understand high-dimensional data indexing  thoroughly through real life applications. Throughout the development of this project, performance data of different high-dimensional data indexing methods will be produced, so learners not only learn from the application side, but also from the statistical values. This project covers different aspects of high-dimensional data indexing, which ensures learners understand the topic completely. 

The US traffic accident dataset is the selected dataset for this project. The dataset contains different attributes, for instance, severity of the accident, start time, end time, accident coordinates, distance, and etc. I chose the US traffic accident dataset, since it contains different types of values, so it gives me plenty of space to develop my project queries in the upcoming phase.

Based on the dataset, I need to create 5 queries. For each query, I need to solve it with  2 different indexing algorithms. An indexing algorithm can be reused in other queries if applicable, but learners need to use at least 3 different algorithms throughout the entire project. In addition, learners need to use different parameter values for every query. Every query result needs to be validated by the ground truth from the PostGIS.

These are the queries I worked on throughout the indexing project. 

Query 1: Given a point, a distance range and a date, find all the traffic accidents that happened within the distance range of the given point which also meet the date requirement.


Query 2: Given an accident point, find its KNN that has the same severity value as the given accident point.”



Query 3: Given a bounding region, find the accidents within the region that last the longest and the accidents that last the shortest amount of time.


Query 4: Given a region, find all accidents within the region and find out the number of accidents in each severity category and the overall percentages.


Query 5: Given a location point, and a distance range. Dissect the distance range to subregions, explore the traffic accident frequencies and patterns within the subregions of a given distance range.


How many value sets I have tested on each query.

For query 1, I worked on 4 different sets of data. 

For query 2, I worked on 3 different sets of data.

For query 3, I worked on 2 different sets of data.

For query 4, I worked on 1 case.

For query 5, I worked on 1 case.


What algorithm I have used on each query.

For query 1, R-Tree, Linear Scan

For query 2, KD-Tree, Linear Scan

For query 3, R-Tree, Linear Scan

For query 4, R-Tree, Linear Scan

For query 5, KD-Tree, Linear Scan

Detailed testing data is shown in the project report 


What are the major takeaways from this project.
1.  The importance of using the right standards and using the same standards when doing comparison. 
2. KD-Tree takes less time when compared with R-Tree indexing, as R-Tree needs to find the minimum bounding rectangle to avoid the overlapped areas, so it will take longer to find the best fit arrangements. KD-Tree is more intuitive, if the current value is smaller than the current node value, it assigns left. Otherwise, it is assigned right. The procedures in R-Tree are more complicated, so it takes longer to process. 
3. Using data indexing algorithms doesn't always give you the best performance, and it really depends on other factors, for instance, data size, the relative position of the data point, and the frequency of using the dataset.
4. Indexing time can be lengthy, and it can even be longer than the query time in some cases. If you will access the dataset many times, indexing is only a one time cost, and you will benefit in the long run. Otherwise, we may not benefit from data indexing. 
5. Performance after data indexing may not be noticeable if the operation is relatively simple, or/and the dataset is relatively small. The performance will be more obvious when the operations are complicated and the dataset is large.


Strategies:

1.Separate the query into smaller tasks. Utilizing indexing algorithms to get the target results in an efficient manner, which can also narrow the searching items in the next tasks. For instance, in query 1, I used R-Tree to find all the within range accident points, which can eliminate many unrelated points from the dataset. Afterwards, I can filter the result by date. This is way more efficient then searching the data row with the qualified date, then find data rows that are within the distance. Data rows that are within a specific range should have less records, while data rows that satisfied the date requirement should have more records. According to the domain knowledge, you should filter by range, which gives you less points, so you will do less search in the date filtering phase. You need to use the domain knowledge.

2.Use domain knowledge, for instance, in linear scan, if a data point is found, you can terminate the loop and avoid unnecessary loops on the remaining data in the dataset. 




Image Gallery

The tables below show how the queries perform in different test cases. The tables contain index time, index memory, query time, and query memory.

![Query1Case1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/2ddcce51-8c85-45ec-991d-6da27baebc17)

![Query1Case2](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/2d86edd8-f581-4e3e-8a08-33315ddc8e7d)

![Query1Case3](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/a8a03049-99c8-41cf-a722-c590594c67c3)

![Query1case4](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/d1bfdec9-a885-4ed9-a0ac-918fb55b3a16)

![Query2case1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/a6c3cd64-16e6-4648-a5a2-13e3c1d1d6a1)

![Query2case2](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/85334df5-d1e7-45cd-b39d-b7a463e66ef6)

![Query2case3](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/70132563-789a-440e-8d31-341b9b6a03e4)

![Query3case1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/63de78e7-d92d-42aa-88c5-7f817bbdeecb)

![Query3case2](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/b66a2d44-2e17-44a8-8611-3d4fd2d1b532)

![Query4case1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/d9ace07b-2f33-48d3-af66-71f15251d93e)

![Query5case1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/55ca194c-e704-4afa-95c4-aa717f355226)

The two images below demonstrate the application of using ST_Transform in postgis. It not only shows us the results geographically,but it also allows us to validate the results and decide the correctness.

![img1](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/3d219bed-e6dd-4cdd-a234-0fcb010a2f95)

![img2](https://github.com/jefjefhui/Advanced-Techniques-for-High-Dimensional-Data-Project/assets/73283123/bfcb1762-725b-4584-9853-3d65cf9baebc)
