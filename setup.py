"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup

setup(
    name="sample_project",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    entry_points = {
        "console_scripts": [
            "etl_job = sample_project.workloads.sample_etl_job:main"
    ]},
    version="0.0.1",
    description="",
    author="Robert Yousif <robertyousif1@gmail.com>",
)
