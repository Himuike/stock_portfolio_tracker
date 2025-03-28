# This module handles file operation like reading and writing data

import os

# File paths
USERS_FILE = "data/users.txt"
STOCKS_FILE = "data/stocks.txt"
PORTFOLIOS_FILE = "data/portfolios.txt"
TRANSACTIONS_FILE = "data/transactions.txt"
PURCHASE_PRICES_FILE = "data/purchase_prices.txt"

def initialize_files():
    # Create the data directory and files if they don't exist.
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write("admin,admin\n")  # Default admin user

    if not os.path.exists(STOCKS_FILE):
        with open(STOCKS_FILE, "w") as f:
            f.write("")

    if not os.path.exists(PORTFOLIOS_FILE):
        with open(PORTFOLIOS_FILE, "w") as f:
            f.write("")

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "w") as f:
            f.write("")

    if not os.path.exists(PURCHASE_PRICES_FILE):
        with open(PURCHASE_PRICES_FILE, "w") as f:
            f.write("")