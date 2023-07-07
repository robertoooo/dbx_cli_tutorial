"""test"""
from pyspark.sql import DataFrame, SparkSession


def test_write_managed_table(spark: SparkSession):
    """
    Integration test the write managed table Utils method
    """
    from workloads.sample_etl_job import Utils

    data = [
        {"Category": "A", "ID": 1, "Value": 121.44, "Truth": True},
        {"Category": "B", "ID": 2, "Value": 300.01, "Truth": False},
        {"Category": "C", "ID": 3, "Value": 10.99, "Truth": None},
        {"Category": "E", "ID": 4, "Value": 33.87, "Truth": True},
    ]

    df = spark.createDataFrame(data)
    Utils.write_managed_table(
        df=df, table_name="default.categories", mode="OVERWRITE"
    )

    list_tables = spark.sql("SHOW TABLES FROM default").collect()
    print("Current available tables are: \n", list_tables)
    
    # Assert if the table default.categories exists
    assert len(list_tables) == 1 and list_tables[0]["tableName"] == "categories"

    # Assert if the table default.categories has the correct schema
    df_schema = spark.sql("DESCRIBE TABLE default.categories").collect()
    assert df_schema[0]["col_name"] == "Category"



def test_filter_zipcode(spark: SparkSession):
    from workloads.sample_etl_job import Utils


    df = spark.read.csv("data/nytaxi-with-zipcodes.csv", header=True)
    df_filter = Utils.filter_zipcode(df, "10027")
    list_assert = df_filter.select("pickup_zip").distinct().collect()
    
    # Assert if the df only has one disticnt zipcode and that the zipcode is 10027
    assert len(list_assert) == 1 and list_assert[0]["pickup_zip"] == "10027"


def test_read_table_with_storage_path(spark: SparkSession):
    """Test the read delta table Utils method"""
    from workloads.sample_etl_job import Utils

    df = Utils.read_table_with_storage_path(
        spark=spark, frmt="csv", path="data/nytaxi-with-zipcodes.csv", opt={"header": True}
    )

    # Assert that df is a DataFrame
    assert(isinstance(df, DataFrame))
    
    # Assert that df contains data
    assert df.count() > 0