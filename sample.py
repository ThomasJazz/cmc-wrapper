import requests
import json
import pandas as pd
import os

from env import credentials
from library import method_helper
from library.cmcw import crypto

##########################
#### CONFIG VARIABLES ####
##########################
# General Utility
helper = method_helper.MethodHelper()

# API Information
cmc_api_key = credentials.coinmarketcap_api_key
crypto = crypto.Crypto(cmc_api_key)

# Data export path
json_export_path = 'json/coinmarketcap'
helper.check_and_create_directory(json_export_path)

###################
#### FUNCTIONS ####
###################
def export_json(dataset: dict, folder_path: str):
    # Always export to location defined in config, using combination of endpoint and current time
    export_time = helper.get_current_datetime(utc=True)
    file_name = f'{os.path.basename(folder_path)}_{export_time}.json'

    # Make sure export folder exists
    helper.check_and_create_directory(folder_path)

    # Write formatted JSON to file
    with open(f'{os.path.join(json_export_path,file_name)}', 'w') as f:
        f.write(json.dumps(dataset, indent=4))

def print_data(dataset: dict, function_name: str):
    print(f'************************ {function_name} ************************')
    print(f'{json.dumps(dataset, indent=4)}')

#####################
#### SCRIPT BODY ####
#####################

#export_json(latest_data, f'{json_export_path}/cryptocurrency/listings/latest')
btc_map = crypto.get_map('BTC', formatting='dict')
print_data(btc_map, 'get_map')

info = crypto.get_info('ETH', formatting='dict')
print_data(info, 'get_info')

data = crypto.get_listings_latest

#print(json.dumps(btc_info, indent=4))