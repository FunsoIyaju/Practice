from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .getOrCreate()

shows = spark.read.json("D:\\Data\\shows-silicon-valley.json")
#shows.show()
#shows.count()
shows.printSchema()