import requests
import json
import pandas as pd
import os

from env import credentials
from library import method_helper
from library import cmc_api

##########################
#### CONFIG VARIABLES ####
##########################
# General Utility
helper = method_helper.MethodHelper()

# API Information
cmc_api_key = credentials.coinmarketcap_api_key
cmc = cmc_api.CmcApi(cmc_api_key)

# Data export path
json_export_path = 'json/coinmarketcap'
helper.check_and_create_directory(json_export_path)

###################
#### FUNCTIONS ####
###################
def export_json(dataset: dict, endpoint: str):
    # Always export to location defined in config, using combination of endpoint and current time
    export_time = helper.get_current_datetime(utc=True)
    folder_path = os.path.join(json_export_path, endpoint)
    file_name = f'{os.path.basename(folder_path)}_{export_time}.json'

    # Make sure export folder exists
    helper.check_and_create_directory(folder_path)

    # Write formatted JSON to file
    with open(f'{os.path.join(json_export_path,file_name)}', 'w') as f:
        f.write(json.dumps(dataset, indent=4))

#####################
#### SCRIPT BODY ####
#####################
latest_data = cmc.get_latest_listings()

# Loop through all the different coins in the dataset and print some of their info
for crypto in latest_data['data']:
    coin_name = crypto['name']
    usd_quote = crypto['quote']['USD']['price']
    quote_time = crypto['quote']['USD']['last_updated']

    #print(f'{coin_name} @ ${usd_quote} (Last updated: {quote_time})')

#export_json(latest_data, '/cryptocurrency/listings/latest')
btc_info = {}
try:
    btc_info = cmc.get_info('BTC,ETH', formatting='str')
    print(type(btc_info))
except Exception as e:
    print(str(e))

#print(json.dumps(btc_info, indent=4))