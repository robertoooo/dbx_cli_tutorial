# Setup the environment
* git clone project
* python -m venv venv
* pip install -r requirements.dev.txt
* Open databricks workspace and create a PAT token
* databricks configure --token
  * add the Databricks hostname ex: https://adb-xxxxxxxxxxxxx.x.azuredatabricks.net/
* test that the connection works with databricks fs ls
* The databricks config file is stored in: ~/.databrickscfg



# To do
* Add pytest to the github pipeline


# Commands
Execute a task interactivly against the workspace cluster
NOTE: This is only supported by spark_python_task and python_wheel_task
```sh
dbx execute --cluster-name "Robert Yousif's Cluster" --job "dbx_cli_tutorial_job" --task main
```

Deploy to workspace as a workflow job
```sh
dbx deploy
```

Launch a workflow job
```sh
dbx launch --job "dbx_cli_tutorial_job"
```

Run the tests
```sh
pytest
```


# TO DO
Add the requirements_dev and requirements to the setup.py file.

So, place dependent packages your software needs to run in the install_requires list in setup.py.

Dependencies you the developer want in order to build your software go in requirements.txt.

https://dev.to/bowmanjd/python-dev-environment-part-3-dependencies-with-installrequires-and-requirements-txt-kk3


# This article
* dbx cli including
  * notebooks
  * python code/wheel files
* Local Unity testing with spark
* Interactive integration tests from the CLI.
  * dbx execute dbx_cli_tutorial_job --cluster-name "Robert Yousif's Cluster"  --task "main"
* Configuring the right environment.
* Dependencies with setup.py and dbx cli 
  * Every library in install_requires will be installed when ran in production.
  * Another option is to provide a requirements.txt file in your project, this way all the requirements there will be installed.
* Monitoring the workflows 
