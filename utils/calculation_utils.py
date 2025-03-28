# This module provide utility function for calculations.

def calculate_profit_loss(current_price, average_purchase_price, quantity):
    # calculate profit/loss for a stock
    return (current_price - average_purchase_price) * quantity

def calculate_portfolio_performance(portfolios, stocks, purchase_prices, username):
    # calculate portfolio performance for a user
    
    total_investment = 0
    current_value = 0
    for stock_name, portfolio in portfolios[username].items():
        if stock_name in stocks:
            current_price = stocks[stock_name].price
            if username in purchase_prices and stock_name in purchase_prices[username]:
                total_purchase_cost = sum(price * qty for price, qty in purchase_prices[username][stock_name])
                average_purchase_price = total_purchase_cost / sum(qty for _, qty in purchase_prices[username][stock_name])
                investment = average_purchase_price * portfolio.quantity
                profit_loss = calculate_profit_loss(current_price, average_purchase_price, portfolio.quantity)
            else:
                investment = 0
                profit_loss = 0
            total_investment += investment
            current_value += current_price * portfolio.quantity
    return total_investment, current_value, current_value - total_investment