# vars/newrelicCheck.py
import requests

def newrelicCheck(envVars):
    headers = {'X-Api-Key': envVars["newrelicKey"]}
    response = requests.get(envVars["newrelicURL"], headers=headers)
    if response.status_code == 200:
        print("New Relic URL is up and running")
    else:
        raise ValueError("New Relic URL is not running, check your configuration")