# Databricks notebook source
print("Hej")
from pyspark import spark 

# COMMAND ----------

df_gold = spark.sql(
    "SELECT pickup_zip, SUM(trip_distance) as sum_trip_distance, SUM(fare_amount) as sum_fare_amount, avg(dollar_per_mile) as sum_dollar_per_mileduration_seconds FROM pax_demo.nyctaxi.silver_nytaxi GROUP BY pickup_zip ORDER BY sum_fare_amount DESC"
)
