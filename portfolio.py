print("📈 Welcome to your Stock Portfolio Tracker!")
print("_" * 40)
stock_prices = {
    "APPLE": 150,
    "GOOGLE": 180,
    "TESLA": 250,
    "MICROSOFT": 300
}
user_portfolio = {}
for stock, price in stock_prices.items():
    print(f"Current price of {stock} is ${price}")
    shares = int(input(f"How many shares of {stock} do you own? (Type 0 if none): "))
    if shares > 0:
        user_portfolio[stock] = shares
print("_" * 40)
print("📊 YOUR PORTFOLIO SUMMARY:")
print("_" * 40)
total_portfolio_value = 0
for stock, shares in user_portfolio.items():
    price_per_share = stock_prices[stock]
    stock_value = shares * price_per_share
    total_portfolio_value += stock_value
    print(f"- {stock}: {shares} shares x ${price_per_share} = ${stock_value}")
print("_" * 40)
print(f"💰 Total Investment Value: ${total_portfolio_value}")
print("_" * 40)