# Wrapper class for Coin Market Cap API
import requests
import json
import os

# Custom formatting exception
class IllegalReturnFormat(Exception):
    def __init__(self, msg=f'Error: Invalid value supplied for "formatting" parameter.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

# Main API Wrapper class
class CmcApi():
    def __init__(self, api_key):
        assert(api_key is not None and api_key != ''), 'Error: api_key cannot be null or empty'
        
        # Request config
        self.base_url = 'https://pro-api.coinmarketcap.com/v1'
        self.api_key = api_key
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key
        }

        # Other
        self.return_formats = {'dict', 'response', 'str'}
    
    ##########################
    #### PUBLIC FUNCTIONS ####
    ##########################
    def get_latest_listings(self, formatting='dict'):
        self.__is_valid_formatting(formatting)
        r = requests.get(self.base_url + '/cryptocurrency/listings/latest', headers=self.headers)
        dataset = json.loads(r.text)
        
        obj = self.__apply_formatting(r, formatting)
        return obj
    
    def get_latest_quotes(self, formatting='dict'):
        self.__is_valid_formatting(formatting)
        r = requests.get(self.base_url + '/cryptocurrency/listings/latest', headers=self.headers)
        dataset = json.loads(r.text)
        
        obj = self.__apply_formatting(r, formatting)
        return obj

    def get_info(self, symbol: str, formatting='dict'):
        self.__is_valid_formatting(formatting)
        # Query params
        params = {'symbol':symbol.upper()}

        r = requests.get(self.base_url + '/cryptocurrency/info', params=params, headers=self.headers)
        dataset = json.loads(r.text)

        obj = self.__apply_formatting(r, formatting)
        return obj

    ###########################
    #### PRIVATE FUNCTIONS ####
    ###########################
    def __is_valid_formatting(self, formatting: str):
        if not(formatting in self.return_formats):
            raise IllegalReturnFormat()
    
    def __apply_formatting(self, r, formatting: str):
        if (formatting == 'response'):
            return r
        elif (formatting == 'dict'):
            return json.loads(r.text)
        elif (formatting == 'str'):
            return r.text
        else:
            raise IllegalReturnFormat()