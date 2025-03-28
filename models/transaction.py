# This module defines the Transaction class and handles transaction-related operations.

from datetime import datetime
from utils.file_utils import TRANSACTIONS_FILE, PURCHASE_PRICES_FILE

class Transaction:
    def __init__(self, username, action, stock_name, quantity, timestamp):
        self.username = username
        self.action = action
        self.stock_name = stock_name
        self.quantity = quantity
        self.timestamp = timestamp

    @staticmethod
    def load_transactions():
        transactions = []
        with open(TRANSACTIONS_FILE, "r") as f:
            for line in f:
                username, action, stock_name, quantity, timestamp = line.strip().split(",")
                transactions.append(Transaction(username, action, stock_name, int(quantity), timestamp))
        return transactions

    @staticmethod
    def save_transaction(username, action, stock_name, quantity):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(TRANSACTIONS_FILE, "a") as f:
            f.write(f"{username},{action},{stock_name},{quantity},{timestamp}\n")

    @staticmethod
    def load_purchase_prices():
        purchase_prices = {}
        with open(PURCHASE_PRICES_FILE, "r") as f:
            for line in f:
                username, stock_name, purchase_price, quantity = line.strip().split(",")
                if username not in purchase_prices:
                    purchase_prices[username] = {}
                if stock_name not in purchase_prices[username]:
                    purchase_prices[username][stock_name] = []
                purchase_prices[username][stock_name].append((float(purchase_price), int(quantity)))
        return purchase_prices

    @staticmethod
    def save_purchase_price(username, stock_name, purchase_price, quantity):
        with open(PURCHASE_PRICES_FILE, "a") as f:
            f.write(f"{username},{stock_name},{purchase_price},{quantity}\n")