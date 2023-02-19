"""test"""
import logging
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import to_timestamp, col
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from tests.conftest import DBUtilsFixture
from unittest.mock import patch   

@patch("workloads.sample_etl_job.nycitytaxi_path", "data/nytaxi-with-zipcodes.csv") 
@patch("workloads.sample_etl_job.source_table_format", "CSV") 
@patch("workloads.sample_etl_job.read_options", {"header": True}) 
def test_task_sample_etl_job(spark: SparkSession):
    from workloads.sample_etl_job import main
    main()
    assert spark.sql("show tables").where(col("tableName") == "bronze_nytaxi").count() == 1
    assert spark.sql("show tables").where(col("tableName") == "silver_nytaxi").count() == 1