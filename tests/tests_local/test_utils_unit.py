"""test"""
import logging
from tests.tests_local.conftest import DBUtilsFixture

def test_write_managed_table(mocker):
    """
    Integration test the write managed table Utils method
    """
    spark = mocker.Mock()
    df = mocker.Mock()

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
    
    # Assert that spark.sql was called with the correct arguments
    spark.sql.assert_called_with("SHOW TABLES FROM default")

    # Assert that df.write.mode was called with the correct arguments
    df.write.mode.assert_called_with("OVERWRITE")

    # Assert that the mock_calls call.write.mode().saveAsTable was called with the correct arguments
    df.write.mode().saveAsTable.assert_called_with("default.categories")


def test_read_table_with_storage_path(mocker):
    """Test the read delta table Utils method"""
    spark = mocker.Mock()

    from workloads.sample_etl_job import Utils

    df = Utils.read_table_with_storage_path(
        spark=spark, frmt="csv", path="data/nytaxi-with-zipcodes.csv", opt={"header": True}
    )

    # Assert that spark.read.load has been called with the correct arguments
    spark.read.load.assert_called_with( format="csv", path="data/nytaxi-with-zipcodes.csv", header=True)



def test_dbutils():
    """Basic test of dbutils conftest
    Creates a directory in root called spark-warehouse and then checks if the directory is there.
    This directory is needed for the spark session to function properly.
    """

    logging.info("Testing the sample dbutils job")
    dbu = DBUtilsFixture()
    dbu.mkdirs("spark-warehouse")
    result = dbu.ls(".")
    path_list_name = [row.name for row in result]
    assert (
        "spark-warehouse" in path_list_name
    ), "Your project does not contain a folder called spark-warehouse"
