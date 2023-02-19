# Databricks notebook source
# MAGIC %md
# MAGIC # Simple Notebook Task
# MAGIC
# MAGIC This notebook is triggered by the dbx_cli_tutorial_workflow task called simple_notebook

# COMMAND ----------

from pyspark.sql import SparkSession

spark = (
    SparkSession.getActiveSession()
)  # Setup spark for local testing, not needed when ran as notebook

# COMMAND ----------

df_gold = spark.sql(
    """
    SELECT 
        pickup_zip, 
        SUM(trip_distance) as sum_trip_distance, 
        SUM(fare_amount) as sum_fare_amount, 
        avg(duration_seconds) as avg_duration_seconds 
    FROM 
        pax_demo.nyctaxi.nytaxi_silver 
    GROUP BY 
        pickup_zip 
    ORDER BY 
        sum_fare_amount DESC
    """
)

# COMMAND ----------

df_gold.write.mode("OVERWRITE").saveAsTable("pax_demo.nyctaxi.nytaxi_gold")
