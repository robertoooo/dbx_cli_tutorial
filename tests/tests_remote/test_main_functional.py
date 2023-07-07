
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

def test_task_sample_etl_job():
    spark = SparkSession.builder.getOrCreate()
    from workloads.sample_etl_job import main
    main(spark=spark)
    assert spark.sql("show tables").where(col("tableName") == "nytaxi_bronze").count() == 1
    assert spark.sql("show tables").where(col("tableName") == "nytaxi_silver").count() == 1