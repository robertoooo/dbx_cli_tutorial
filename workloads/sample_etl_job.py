from pyspark.shell import spark

def main():
    """The main function specified as an entry point inside the setup.py file"""
    demo_table_sourcepath = "dbfs:/databricks-datasets/nyctaxi-with-zipcodes/subsampled"
    table_full_name = "default.nytaxi_OH"

    utils = Utils()
    # Read table from databricks sample data
    df = utils.read_delta_table_with_storage_path(demo_table_sourcepath)
    
    # Filter the dataframe on zipcode
    df_filter = utils.filter_zipcode(df, "10027")

    # Write the table to the hive metastore
    utils.write_managed_table(df_filter, table_full_name)


class Utils:
    """Simple Utils Class with helper function """
    @staticmethod
    def read_delta_table_with_storage_path(path):
        """"""
        df = spark.sql(f"SELECT * FROM delta.`{path}`")
        return df

    @staticmethod
    def filter_zipcode(df, zipcode):
        df_filter_zip = df.filter(df.pickup_zip == zipcode)
        return df_filter_zip

    @staticmethod
    def write_managed_table(df, table_full_name):
        df.write.mode("overwrite").saveAsTable(table_full_name)

    @staticmethod
    def write_external_table(df, table_full_name, storage_path):
        df.write.mode("overwrite").option("path", f"{storage_path}").saveAsTable(table_full_name)

if __name__ == "__main__":
    main()