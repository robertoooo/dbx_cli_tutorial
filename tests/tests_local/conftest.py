import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime
import pytest
from pyspark.sql import SparkSession
from pathlib import Path
import tempfile
from delta import configure_spark_with_delta_pip
import shutil


@dataclass
class FileInfoFixture:
    """
    This class mocks the DBUtils FileInfo object
    """

    path: str
    name: str
    size: int
    modificationTime: int


class DBUtilsFixture:
    """
    This class is used for mocking the behaviour of DBUtils inside tests.
    """

    def __init__(self):
        self.fs = self

    def cp(self, src: str, dest: str, recurse: bool = False):
        copy_func = shutil.copytree if recurse else shutil.copy
        copy_func(src, dest)

    def ls(self, path: str):
        _paths = Path(path).glob("*")
        _objects = [
            FileInfoFixture(
                str(p.absolute()), p.name, p.stat().st_size, int(p.stat().st_mtime)
            )
            for p in _paths
        ]
        return _objects

    def mkdirs(self, path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    def mv(self, src: str, dest: str, recurse: bool = False):
        copy_func = shutil.copytree if recurse else shutil.copy
        shutil.move(src, dest, copy_function=copy_func)

    def put(self, path: str, content: str, overwrite: bool = False):
        _f = Path(path)

        if _f.exists() and not overwrite:
            raise FileExistsError("File already exists")

        _f.write_text(content, encoding="utf-8")

    def rm(self, path: str, recurse: bool = False):
        deletion_func = shutil.rmtree if recurse else os.remove
        deletion_func(path)


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """
    This fixture provides preconfigured SparkSession with Hive and Delta support.
    After the test session, temporary warehouse directory is deleted.
    :return: SparkSession
    """
    logging.info("Configuring Spark session for testing environment")
    warehouse_dir = tempfile.TemporaryDirectory().name

    if Path(warehouse_dir).exists():
        shutil.rmtree(warehouse_dir)

    if Path("spark-warehouse").exists():
        shutil.rmtree("spark-warehouse")

    if Path("metastore_db").exists():
        shutil.rmtree("metastore_db")

    _builder = (
        SparkSession.builder.master("local[*]")
        .config("spark.hive.metastore.warehouse.dir", Path(warehouse_dir).as_uri())
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.ui.showConsoleProgress", "true")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .enableHiveSupport()
    )
    spark: SparkSession = configure_spark_with_delta_pip(_builder).getOrCreate()
    logging.info("Spark session configured")
    yield spark
    logging.info("Shutting down Spark session")
    spark.stop()
    if Path(warehouse_dir).exists():
        shutil.rmtree(warehouse_dir)
