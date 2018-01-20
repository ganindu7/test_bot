import ccxt

print(ccxt.exchanges)

exchange = ccxt.gdax()

print(exchange.id, exchange.load_markets())
print(exchange.fetch_order_book(exchange.symbols[0]))
print(exchange.fetch_ticker('LTC/EUR'))
print('key test');