import requests


class Securities:

    def __init__(self, name, type, shares, inPrice, curPrice):
        self.name = name
        self.type = type
        self.shares = shares
        self.inPrice = inPrice
        self.curPrice = curPrice
        self.inVal = float(shares) * float(inPrice)
        self.curVal = float(shares) * float(curPrice)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_shares(self):
        return self.shares

    def get_cur_val(self):
        return self.curVal

    def get_in_val(self):
        return self.inVal

    def get_in_price(self):
        return self.inPrice

    def get_growth(self):
        return self.curVal - self.inVal

    def get_perc_growth(self):
        return ((self.curVal - self.inVal) / self.inVal) * 100.0

    def get_cur_price(self):
        return self.curPrice

    def set_cur_price(self, curPrice):
        self.curPrice = float(curPrice)
        self.curVal = float(curPrice) * self.shares


def coin_price(url, query, headers):
    coin = requests.request("GET", url, headers=headers, params=query)
    coin_data = coin.json()
    return coin_data['data']['price']


def stock_price(url, query, headers):
    quote = requests.request("GET", url, headers=headers, params=query)
    quote_data = quote.json()
    return quote_data['price']
