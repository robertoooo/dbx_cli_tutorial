from setuptools import find_packages, setup

PACKAGE_REQUIREMENTS = ["pyyaml"]

LOCAL_REQUIREMENTS = ["pyspark==3.3.0", "delta-spark==2.1.0", "dbx", "pytest"]

setup(
    name="workloads",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["setuptools", "wheel"],
    install_requires=PACKAGE_REQUIREMENTS,
    extras_require={"local": LOCAL_REQUIREMENTS},
    entry_points={"console_scripts": ["etl_job = workloads.sample_etl_job:main"]},
    version="0.0.1",
    description="",
    author="Robert Yousif <robertyousif1@gmail.com>",
)
