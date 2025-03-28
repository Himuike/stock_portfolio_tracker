# This module defines the portfolio class and handles portfolio-related operations

from utils.file_utils import PORTFOLIOS_FILE

class Portfolio:
    def __init__(self, username, stock_name, quantity):
        self.username = username
        self.stock_name = stock_name
        self.quantity = quantity

    @staticmethod
    def load_portfolios():
        portfolios = {}
        with open(PORTFOLIOS_FILE, "r") as f:
            for line in f:
                username, stock_name, quantity = line.strip().split(",")
                if username not in portfolios:
                    portfolios[username] = {}
                portfolios[username][stock_name] = Portfolio(username, stock_name, int(quantity))
        return portfolios

    @staticmethod
    def save_portfolios(portfolios):
        with open(PORTFOLIOS_FILE, "w") as f:
            for username, stocks in portfolios.items():
                for stock_name, portfolio in stocks.items():
                    f.write(f"{portfolio.username},{portfolio.stock_name},{portfolio.quantity}\n")