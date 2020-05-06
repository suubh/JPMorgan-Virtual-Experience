#This is where you would manually type the existing code in the client3.py, which is inside the jpm_module_1 folder (disregard copying the useless comments) so that you can avoid the dreaded tab editing issues in REPL particularly for the Python environment only

#After manually copying the useful code in client3.py, you can make your changes here

#Before you test your modified code is working, make sure you have done the initial steps needed to be done before making changes in the instruction slides

#Then, to test, first, delete the client3.py file inside jpm_module_1. Then rename this file to just client3.py. Finally move this file inside the jpm_module_1 folder  

# Delete these comments when you're done...
# Comments are anything that's preceded with '#'
import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
	
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	price = (bid_price+ask_price)/2
	return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
  if(price_b==0):
    return
  return price_a/price_b

# Main
if __name__ == "__main__":
  for _ in iter(range(N)):
    quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
    prices={}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price
      print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print ("Ratio %s" % getRatio(prices['ABC'], prices['DEF']))
