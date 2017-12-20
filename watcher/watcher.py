from time import sleep,time
import os

from bithumb import Bithumb
from bitfinex import Bitfinex


INTERVAL = 30

watch_list = ["ETH","LTC","EOS","XRP","BCH"]

next_execute_time = int(time()) + 0.5


while True:
    current_time = (int(time()))
    sleep(next_execute_time - current_time)
    next_execute_time += INTERVAL
    bitfinex_prices = []
    bithumb_prices = []
    for symbol in watch_list:
        bithumb_prices.append(sum(Bithumb.get_relative_price(symbol,'BTC'))/2)
        bitfinex_prices.append(sum(Bitfinex.get_relative_price(symbol,'BTC'))/2)
    os.system('clear')
    print("{0:<10} | {1:<15} | {2:<15} | {3:<8} ".format("Symbol","Bitfinex","Bithumb","Difference"))
    print("-"*80)
    for symbol,bitfinex_price, bithumb_price in zip(watch_list,bitfinex_prices,bithumb_prices):
        difference = 100.0 * (bithumb_price - bitfinex_price) / bitfinex_price
        print("{0:<10} | {1:<15.8f} | {2:<15.8f} | {3:<8.2f}% ".format(symbol,bitfinex_price,bithumb_price, difference))


