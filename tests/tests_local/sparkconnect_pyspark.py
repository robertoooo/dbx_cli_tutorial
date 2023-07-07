from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df_catalogs = spark.sql("show catalogs")

df_catalogs.show()


df = spark.sql("SELECT * FROM main.default.silvertable")

df.show()



