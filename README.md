# Steps
* git clone project
* python -m venv venv
* pip install -r requirements.txt
* Open databricks workspace and create a PAT token
* databricks configure --token
  * add the Databricks hostname ex: https://adb-xxxxxxxxxxxxx.x.azuredatabricks.net/
* test that the connection works with databricks fs ls
* The databricks config file is stored in: ~/.databrickscfg



# To do
* Add pytest to the github pipeline


# Commands
Execute a task interactivly agains the workspace cluster
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