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
* Clean up requirements
* Add pytest to the github pipeline