from pyspark.shell import spark
from pyspark.sql.functions import to_timestamp

nycitytaxi_path = "dbfs:/databricks-datasets/nyctaxi-with-zipcodes/subsampled"
source_table_format = "DELTA"
read_options = {}


def main():
    """The main function specified as an entry point inside the setup.py file"""
    utils = Utils()

    # Read table from databricks sample data and stage it in your own hive metastore
    df = utils.read_table_with_storage_path(
        path=nycitytaxi_path, frmt=source_table_format, opt=read_options
    )

    utils.write_managed_table(df, "nytaxi_bronze")  # Bronze Table

    # Augment new column and write it to the hive metastore
    df = df.withColumn(
        "duration_seconds",
        (
            to_timestamp(df.tpep_dropoff_datetime)
            - to_timestamp(df.tpep_pickup_datetime)
        ).astype("int"),
    )

    utils.write_managed_table(df, "nytaxi_silver")  # Silver Table
    print("Successfully transformed and saved table")


class Utils:
    """Simple Utils Class with helper function"""

    @staticmethod
    def read_table_with_storage_path(path: str, frmt: str, opt: dict = {}):
        """Read any kind of table"""
        df = spark.read.load(format=frmt, path=path, **opt)
        return df

    @staticmethod
    def write_managed_table(df, table_name, mode="OVERWRITE"):
        df.write.mode(mode).saveAsTable(table_name)

    @staticmethod
    def write_external_table(df, table_full_name, storage_path, mode):
        df.write.mode(mode).option("path", f"{storage_path}").saveAsTable(
            table_full_name
        )

    @staticmethod
    def filter_zipcode(df, zipcode):
        df_filter_zip = df.filter(df.pickup_zip == zipcode)
        return df_filter_zip


if __name__ == "__main__":
    main()
