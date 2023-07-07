
from unittest.mock import patch   

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Patch the nycitytaxi_path, source_table_format and read_options
@patch("workloads.sample_etl_job.nycitytaxi_path", "data/nytaxi-with-zipcodes.csv") 
@patch("workloads.sample_etl_job.source_table_format", "CSV") 
@patch("workloads.sample_etl_job.read_options", {"header": True})
def test_task_sample_etl_job(spark: SparkSession):
    from workloads.sample_etl_job import main
    main(spark=spark)
    assert spark.sql("show tables").where(col("tableName") == "nytaxi_bronze").count() == 1
    assert spark.sql("show tables").where(col("tableName") == "nytaxi_silver").count() == 1