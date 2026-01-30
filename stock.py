# Simple Stock Portfolio Tracker (with file saving)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print(" Stock Portfolio Tracker")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock symbol.")
        continue
    
    qty = int(input(f"Enter quantity of {stock}: "))
    investment = stock_prices[stock] * qty
    portfolio[stock] = portfolio.get(stock, 0) + investment
    total_investment += investment

print("\n Portfolio Summary:")
for stock, value in portfolio.items():
    print(f"{stock}: ${value}")

print(f"\n Total Investment Value: ${total_investment}")

# Save to text file
save = input("\nSave results to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, value in portfolio.items():
            f.write(f"{stock}: ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Results saved to 'portfolio_summary.txt'")
