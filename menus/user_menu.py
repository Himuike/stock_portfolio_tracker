# This module handles the user-menu

from tabulate import tabulate
from models.stock import Stock
from models.portfolio import Portfolio
from models.transaction import Transaction
from utils.calculation_utils import calculate_portfolio_performance

def user_menu(username):
    while True:
        print("\nUser Menu:")
        print("1. Buy Stocks")
        print("2. Sell Stocks")
        print("3. View Portfolio")
        print("4. View Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stocks = Stock.load_stocks()
            if not stocks:
                print("No stocks available to buy.")
                continue
            print("\nAvailable Stocks:")
            stock_table = [[stock.name, f"₹{stock.price}"] for stock in stocks.values()]
            print(tabulate(stock_table, headers=["Stock Name", "Price"], tablefmt="pretty"))
            stock_name = input("Enter stock name to buy: ")
            quantity = int(input("Enter quantity: "))
            if stock_name in stocks:
                portfolios = Portfolio.load_portfolios()
                if username not in portfolios:
                    portfolios[username] = {}
                if stock_name in portfolios[username]:
                    portfolios[username][stock_name].quantity += quantity
                else:
                    portfolios[username][stock_name] = Portfolio(username, stock_name, quantity)
                Portfolio.save_portfolios(portfolios)
                Transaction.save_transaction(username, "bought", stock_name, quantity)
                Transaction.save_purchase_price(username, stock_name, stocks[stock_name].price, quantity)
                print(f"Bought {quantity} shares of {stock_name}.")
            else:
                print("Stock not found.")

        elif choice == "2":
            portfolios = Portfolio.load_portfolios()
            if username not in portfolios or not portfolios[username]:
                print("You have no stocks to sell.")
                continue
            print("\nYour Stocks:")
            stock_table = [[portfolio.stock_name, portfolio.quantity] for portfolio in portfolios[username].values()]
            print(tabulate(stock_table, headers=["Stock Name", "Quantity"], tablefmt="pretty"))
            stock_name = input("Enter stock name to sell: ")
            quantity = int(input("Enter quantity: "))
            if stock_name in portfolios[username]:
                if portfolios[username][stock_name].quantity >= quantity:
                    portfolios[username][stock_name].quantity -= quantity
                    if portfolios[username][stock_name].quantity == 0:
                        del portfolios[username][stock_name]
                    Portfolio.save_portfolios(portfolios)
                    Transaction.save_transaction(username, "sold", stock_name, quantity)
                    print(f"Sold {quantity} shares of {stock_name}.")
                else:
                    print("Not enough shares to sell.")
            else:
                print("Stock not found in your portfolio.")

        elif choice == "3":
            portfolios = Portfolio.load_portfolios()
            stocks = Stock.load_stocks()
            purchase_prices = Transaction.load_purchase_prices()
            if username in portfolios:
                print(f"\n{username}'s Portfolio:")
                portfolio_table = []
                total_investment, current_value, overall_profit_loss = calculate_portfolio_performance(portfolios, stocks, purchase_prices, username)
                for stock_name, portfolio in portfolios[username].items():
                    if stock_name in stocks:
                        current_price = stocks[stock_name].price
                        if username in purchase_prices and stock_name in purchase_prices[username]:
                            total_purchase_cost = sum(price * qty for price, qty in purchase_prices[username][stock_name])
                            average_purchase_price = total_purchase_cost / sum(qty for _, qty in purchase_prices[username][stock_name])
                            investment = average_purchase_price * portfolio.quantity
                            profit_loss = (current_price - average_purchase_price) * portfolio.quantity
                        else:
                            investment = 0
                            profit_loss = 0
                        portfolio_table.append([portfolio.stock_name, portfolio.quantity, f"₹{investment:.2f}", f"₹{profit_loss:.2f}"])
                    else:
                        portfolio_table.append([portfolio.stock_name, portfolio.quantity, "N/A", "N/A"])
                print(tabulate(portfolio_table, headers=["Stock Name", "Quantity", "Amount Invested", "Profit/Loss"], tablefmt="pretty"))
                print(f"Total Amount Invested: ₹{total_investment:.2f}")
                print(f"Current Portfolio Value: ₹{current_value:.2f}")
                print(f"Overall Profit/Loss: ₹{overall_profit_loss:.2f}")
            else:
                print("Your portfolio is empty.")

        elif choice == "4":
            transactions = Transaction.load_transactions()
            print(f"\n{username}'s Transaction History:")
            transaction_table = [[transaction.timestamp, transaction.action, transaction.stock_name, transaction.quantity] for transaction in transactions if transaction.username == username]
            print(tabulate(transaction_table, headers=["Timestamp", "Action", "Stock Name", "Quantity"], tablefmt="pretty"))

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")