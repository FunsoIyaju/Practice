from pyspark.sql.functions import col

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


URL = "jdbc:mysql://localhost/sakila"

spark = SparkSession.builder.appName("DataETL").getOrCreate()
addressDF = spark.read.format("jdbc")\
    .options(url=URL, database='sakila', dbtable='address', user="root", password="olatunbosun123")\
    .load()
# addressDF.show()
# addressDF.select("address", "district").show()
# addressDF.select(addressDF.address, addressDF.district).show()
# addressDF.select(col("*"), expr("case when district = 'Alberta' then 'ALB' else 'BLB' end").alias("DST")).show(truncate=False)
df = addressDF.withColumn("DST", when(addressDF.district == 'Alberta', 'ALB')
                          .when(addressDF.district == 'QLB', 'QLB')
                          .otherwise(addressDF.district))
df.show(truncate=False)
df2 = df.withColumnRenamed('DST', 'DISTT')
df2.filter("DISTT == 'ALB'").show(truncate=False)
# df = addressDF.withColumn('NewAddress', concat_ws(" ", addressDF["address"], addressDF["district"]))
# df.show(truncate=False)
# addressDF.printSchema()
# addressDF2 = addressDF.withColumn('NewAddress', addressDF.address + " " + addressDF.district)
# addressDF2.show()