
import argparse
from binance.client import Client
from config import api_key, api_secret
#user ID
client = Client("api_key", "api_secret")

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--symbol', default='EOSETH', required=True)
args = vars(parser`.parse_args())

def main():

    check_fee()
    #market_depth()
    #

def market_depth():
    depth = client.get_order_book(symbol=args['symbol'])
    print(depth)

def check_fee():
    current_info = client.get_symbol_ticker(symbol=args['symbol'])
    print(current_info)




main()
