from Format import *

# query stuff - crypto
b_url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price"
e_url = "https://coinranking1.p.rapidapi.com/coin/razxDUgYGNAdQ/price"

bitcoin_query = {"Qwsogvtv82FCd":"add-here"}
ethereum_query = {"razxDUgYGNAdQ":"add-here"}

crypto_headers = {
	"X-RapidAPI-Key": "NULL",
	"X-RapidAPI-Host": "NULL"
}

# query stuff - stocks
amzn_url = "https://twelve-data1.p.rapidapi.com/price"
amzn_query = {"symbol":"AMZN","format":"json","outputsize":"1"}

stock_headers = {
	"X-RapidAPI-Key": "NULL",
	"X-RapidAPI-Host": "NULL"
}

# vals
bit_buy = 0.00
eth_buy = 0.00
amzn_buy = 0.00
cash = 0.00

# declarations
bitcoin = Securities('Bitcoin', 'crypto', 1, bit_buy, coin_price(b_url, bitcoin_query,
																crypto_headers))
ether = Securities('Ether', 'crypto', 1, eth_buy, coin_price(e_url, ethereum_query, crypto_headers))
amzn = Securities('AMZN', 'stock', 1, amzn_buy, stock_price(amzn_url, amzn_query, stock_headers))
cash = Securities('Cash', 'cash', 1, cash, cash)

holdings = [bitcoin, ether, amzn, cash]

# print
__format = Format(holdings)
__format.print()
