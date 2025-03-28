# This module handles the admin menu

from tabulate import tabulate
from models.user import User
from models.stock import Stock
from models.portfolio import Portfolio
from models.transaction import Transaction

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Stock Price")
        print("4. View All Stocks")
        print("5. View User Portfolios")
        print("6. Remove User")
        print("7. View All Transactions")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_name = input("Enter stock name: ")
            price = float(input("Enter stock price: "))
            stocks = Stock.load_stocks()
            stocks[stock_name] = Stock(stock_name, price)
            Stock.save_stocks(stocks)
            print(f"Stock {stock_name} added.")

        elif choice == "2":
            stocks = Stock.load_stocks()
            if not stocks:
                print("No stocks available to remove.")
                continue
            print("\nAvailable Stocks:")
            stock_table = [[stock.name, f"₹{stock.price}"] for stock in stocks.values()]
            print(tabulate(stock_table, headers=["Stock Name", "Price"], tablefmt="pretty"))
            stock_name = input("Enter stock name to remove: ")
            if stock_name in stocks:
                del stocks[stock_name]
                Stock.save_stocks(stocks)
                print(f"Stock {stock_name} removed.")
            else:
                print("Stock not found.")

        elif choice == "3":
            stocks = Stock.load_stocks()
            if not stocks:
                print("No stocks available to update.")
                continue
            print("\nAvailable Stocks:")
            stock_table = [[stock.name, f"₹{stock.price}"] for stock in stocks.values()]
            print(tabulate(stock_table, headers=["Stock Name", "Price"], tablefmt="pretty"))
            stock_name = input("Enter stock name to update: ")
            new_price = float(input("Enter new price: "))
            if stock_name in stocks:
                stocks[stock_name].price = new_price
                Stock.save_stocks(stocks)
                print(f"Stock {stock_name} price updated to ₹{new_price}.")
            else:
                print("Stock not found.")

        elif choice == "4":
            stocks = Stock.load_stocks()
            print("\nAll Stocks:")
            stock_table = [[stock.name, f"₹{stock.price}"] for stock in stocks.values()]
            print(tabulate(stock_table, headers=["Stock Name", "Price"], tablefmt="pretty"))

        elif choice == "5":
            portfolios = Portfolio.load_portfolios()
            print("\nUser Portfolios:")
            portfolio_table = []
            for username, stocks in portfolios.items():
                for stock_name, portfolio in stocks.items():
                    portfolio_table.append([username, portfolio.stock_name, portfolio.quantity])
            print(tabulate(portfolio_table, headers=["Username", "Stock Name", "Quantity"], tablefmt="pretty"))

        elif choice == "6":
            username = input("Enter username to remove: ")
            users = User.load_users()
            if username in users:
                del users[username]
                User.save_users(users)
                print(f"User {username} removed.")
            else:
                print("User not found.")

        elif choice == "7":
            transactions = Transaction.load_transactions()
            print("\nAll Transactions:")
            transaction_table = [[transaction.timestamp, transaction.username, transaction.action, transaction.stock_name, transaction.quantity] for transaction in transactions]
            print(tabulate(transaction_table, headers=["Timestamp", "Username", "Action", "Stock Name", "Quantity"], tablefmt="pretty"))

        elif choice == "8":
            break

        else:
            print("Invalid choice. Try again.")