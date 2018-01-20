import ccxt
import os
import sys

print(ccxt.exchanges)

exchange = ccxt.gdax()

print(exchange.id, exchange.load_markets())
print(exchange.fetch_order_book(exchange.symbols[0]))
print(exchange.fetch_ticker('LTC/EUR'))


this_folder = os.path.dirname(os.path.abspath(__file__))
print(this_folder)
root_folder = os.path.dirname(this_folder)
print(root_folder)
print(sys.path)

