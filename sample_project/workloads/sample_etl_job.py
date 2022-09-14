from pyspark.shell import spark

def main():
    demo_table_sourcepath = "dbfs:/databricks-datasets/nyctaxi-with-zipcodes/subsampled"

    df = read_table_path(demo_table_sourcepath)
    df_filter_trip = df.filter(df.state == "OH").show(truncate=False)
    
    #Create functions for transformations and then have some test data availble that is just as the normal data.
    
    database = "default"
    tablename_transformed = "nytaxi"
    target_table_path = "had.samples.people10m_woman"

def read_table_path(path):
    df = spark.sql(f"SELECT * FROM delta.`{path}`")
    return df


def write_table(df, database, tablename, storage_path):
    df.write.mode("overwrite").option("path", f"{storage_path}").saveAsTable(f"{database}.{tablename}")

