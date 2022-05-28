from pyspark.sql import SparkSession




# spark = SparkSession\
#    .builder\
#    .appName("RDD Practice")\
#    .getOrCreate()

#pList = [2.5, 5.6, 78.0]
#pRDD = spark.sparkContext.parallelize(pList,2)

#textRDD = spark.sparkContext.textFile("D:\\Data\\MBA.txt")


#print(pRDD.count())
#print(textRDD.first())

spark:SparkSession = SparkSession\
    .builder\
    .master("local[*]")\
    .appName("RDD Practice 2")\
    .getOrCreate()
#data = [1,2,3,4,5,6,7,8,9,10,11,12]
#dataRDD = spark.sparkContext.parallelize(data)
#print("The number of elements in the list: " + str(dataRDD.count()))
#print("The number of partitions is: " + str(dataRDD.getNumPartitions()))

# Empty DF without partition
#dataRDD = spark.sparkContext.emptyRDD()

# Empty DF with 10 partition
#dataRDD = spark.sparkContext.parallelize([],10)


rdd = spark.sparkContext.textFile("D:\\Data\\MBA.txt")
rdd2 = rdd.flatMap(lambda x: x.split(" "))

rdd3 = rdd2.map(lambda x: (x, 1))
rdd4 = rdd3.reduceByKey(lambda a, b: a+b)
rdd5 = rdd4.map(lambda x: (x[1], x[0])).sortByKey()

#print("The flatten text file: ")
#print(rdd2.collect())

#print("The mapped text file: ")
#print(rdd3.collect())

#print("The summarized text file: ")
#print(rdd4.collect())

#print("The sorted text file: ")
#print(rdd5.collect())

print("count: " + str(rdd5.count()))
first_record = rdd5.first()
print("First Record: " + str(first_record[0]) + " " + first_record[1])
max_record = rdd5.max()
print("Max Record: " + str(max_record[0]) + " " + max_record[1])
min_record = rdd5.min()
print("Minimum: " + str(min_record[0]) + " " + min_record[1])

totalWordCount = rdd5.reduce(lambda a, b:((a[0] + b[0]), a[1]))
print("Reduce text file: " + str(totalWordCount[0]))

data3 = rdd5.take(20)
#for data in data3:
#    print("Data Key: " + str(data[0]) + "  ,Value: " + data[1])

#rdd5.saveAsTextFile("D:\\Data\\Output\\text")
#display(rdd5)
#rdd5.show()

df = rdd5.toDF()
df.show()