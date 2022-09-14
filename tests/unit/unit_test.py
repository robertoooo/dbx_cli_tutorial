"""test"""
import logging

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

from tests.conftest import DBUtilsFixture  # Needed to run dbutils functionality
from pathlib import Path

def test_dbutils(tmp_path: Path):
    """Basic test of dbutils conftest
    Creates a directory in root called spark-warehouse and then checks if the directory is there.
    This directory is needed for the spark session to function properly.
    """
    logging.info("Testing the sample dbutils job")
    dbu = DBUtilsFixture()
    dbu.mkdirs("spark-warehouse")
    result = (dbu.ls("."))
    path_list_name = [row.name for row in result]
    assert "spark-warehouse" in path_list_name, "Your project does not contain a folder called spark-warehouse"

def test_delta_table(spark: SparkSession, tmp_path: Path):
    data = [{"Category": 'A', "ID": 1, "Value": 121.44, "Truth": True},
        {"Category": 'B', "ID": 2, "Value": 300.01, "Truth": False},
        {"Category": 'C', "ID": 3, "Value": 10.99, "Truth": None},
        {"Category": 'E', "ID": 4, "Value": 33.87, "Truth": True}
        ]
    
    df = spark.createDataFrame(data)
    type(df)
    logging.info(f"Testing the sample dbutils job \n {df}")

    target_table_path = "default.categories"
    target_storage_path = "spark-warehouse/categories"