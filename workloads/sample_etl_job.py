from pyspark.shell import spark

def main():
    demo_table_sourcepath = "dbfs:/databricks-datasets/nyctaxi-with-zipcodes/subsampled"
    database = "default"
    tablename_transformed = "nytaxi_OH"

    # Read table from databricks sample data
    df = read_table_path(demo_table_sourcepath)
        
    # Filter the dataframe on zipcode
    df_filter = filter_zipcode(df, "10027")

    # Write the table to the hive metastore
    write_managed_table(df_filter, database, tablename_transformed)

    # Print data for fun
    df_read = spark.sql("SELECT * FROM default.nytaxi_OH")
    print(df_read.head())


def filter_zipcode(df, zipcode):
    df_filter_zip = df.filter(df.pickup_zip == zipcode)
    return df_filter_zip

def read_table_path(path):
    df = spark.sql(f"SELECT * FROM delta.`{path}`")
    return df


def write_managed_table(df, database, tablename):
    storage_path = "spark-warehouse/test"
    # df.write.mode("overwrite").option("path", f"{storage_path}").saveAsTable(f"{database}.{tablename}")
    df.write.mode("overwrite").option("path", f"{storage_path}").saveAsTable(f"{database}.{tablename}")

def write_unmanaged_table(df, database, tablename, storage_path):
    df.write.mode("overwrite").option("path", f"{storage_path}").saveAsTable(f"{database}.{tablename}")

if __name__ == "__main__":
    main()