import ccxt
import os
import sys
import asciichart


this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(this_folder)
sys.path.append(root_folder + '/python')
sys.path.append(this_folder)   # append to path 

 
gdax = ccxt.gdax()
symbol = 'LTC/EUR'

# an ohlcv candle has six items-> open, close, high, low prices then volume and timestamp 
# in order [timestamp, open, high, low, close, volume]

def print_chart(exchange, symbol, timeframe):
    
    print("\n" + exchange.name + ' ' + timeframe + 'chart: ' )
    
    # get a list of ohlcv candles
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    
    # get the attribute we are interested in
    index = 2 
    series = [x[index] for x in ohlcv]
    
    # print chart
    print("\n" + asciichart.plot(series[-120:], {'height': 20}))
    
print_chart(gdax,symbol, '1m')


