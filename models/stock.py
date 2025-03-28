# This module defines the stock class and handles stock-related transactions

from utils.file_utils import STOCKS_FILE

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def load_stocks():
        stocks = {}
        with open(STOCKS_FILE, "r") as f:
            for line in f:
                name, price = line.strip().split(",")
                stocks[name] = Stock(name, float(price))
        return stocks

    @staticmethod
    def save_stocks(stocks):
        with open(STOCKS_FILE, "w") as f:
            for name, stock in stocks.items():
                f.write(f"{stock.name},{stock.price}\n")