# Wrapper class for Coin Market Cap API
import requests
import json
import os

# Custom formatting exception
class IllegalReturnFormat(Exception):
    def __init__(self, msg=f'Error: Invalid value supplied for "formatting" parameter.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


################################
#### MAIN API WRAPPER CLASS ####
################################
class Crypto():
    def __init__(self, api_key, api_version='v1'):
        assert(api_key is not None and api_key != ''), 'Error: api_key cannot be null or empty'
        
        # Request config
        self.base_url = f'https://pro-api.coinmarketcap.com/{api_version}'
        self.api_key = api_key
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key
        }

        # Possible return types for API calls
        self.return_formats = {'dict', 'response', 'str'}
    
    ####################
    # PUBLIC FUNCTIONS #
    ####################
    ###
    # GET /cryptocurrency/map
    ###
    def get_map(self, symbol: str, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        
        # Query params
        params = {'symbol':symbol.upper()}

        r = requests.get(self.base_url + '/cryptocurrency/map', params=params, headers=self.headers)

        return self.__apply_formatting(r, formatting)

    ###
    # GET /cryptocurrency/info
    ###
    def get_info(self, symbol: str, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        
        # Query params
        params = {'symbol':symbol.upper()}

        r = requests.get(self.base_url + '/cryptocurrency/info', params=params, headers=self.headers)

        return self.__apply_formatting(r, formatting)

    ###
    # GET /cryptocurrency/listings/latest
    ###
    def get_listings_latest(self, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        r = requests.get(self.base_url + '/cryptocurrency/listings/latest', headers=self.headers)
        
        return self.__apply_formatting(r, formatting)
    
    ###
    # GET /cryptocurrency/listings/historical
    ###
    def get_listings_historical(self, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        r = requests.get(self.base_url + '/cryptocurrency/listings/historical', headers=self.headers)
        
        return self.__apply_formatting(r, formatting)

    ###
    # GET /cryptocurrency/quotes/latest
    ###
    def get_quotes_latest(self, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        r = requests.get(self.base_url + '/cryptocurrency/quotes/latest', headers=self.headers)
        
        return self.__apply_formatting(r, formatting)

    ###
    # GET /cryptocurrency/quotes/historical
    ###
    def get_quotes_historical(self, formatting='dict'):
        self.__is_valid_formatting(formatting)  # Validate the provided format
        r = requests.get(self.base_url + '/cryptocurrency/quotes/historical', headers=self.headers)
        
        return self.__apply_formatting(r, formatting)

    ###
    # GET /cryptocurrency/market-pairs/latest
    ###

    ###
    # GET /cryptocurrency/ohlcv/latest
    ###

    ###
    # GET /cryptocurrency/ohlcv/historical
    ###
    
    ###
    # GET /cryptocurrency/price-performance-stats/latest
    ###

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