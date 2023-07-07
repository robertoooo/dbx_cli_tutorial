from setuptools import find_packages, setup

PACKAGE_REQUIREMENTS = ["pyyaml"]

LOCAL_REQUIREMENTS = ["pyspark==3.4.1", "delta-spark==2.4.0", "dbx", "pytest"]
REMOTE_SPARK_REQUIREMENTS = ["pyspark==3.4.1", "delta-spark==2.4.0", "dbx", "pytest", "databricks-connect"]

setup(
    name="workloads",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["setuptools", "wheel"],
    install_requires=PACKAGE_REQUIREMENTS,
    extras_require={"local": LOCAL_REQUIREMENTS, "remote": REMOTE_SPARK_REQUIREMENTS},
    entry_points={"console_scripts": ["etl_job = workloads.sample_etl_job:main"]},
    version="0.0.1",
    description="",
    author="Robert Yousif <robertyousif1@gmail.com>",
)

# To install environment for local testing pip install -e .[local]
# To install environment for remote testing -e .[remote]

