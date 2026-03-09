"""
TASK 2: Stock Portfolio Tracker

Goal: 
    Build a simple stock tracker that calculates total investment based on manually defined stock prices.
    
Simplified Scope:
    ● User inputs stock names and quantity.
    ● Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
    ● Display total investment value and optionally save the result in a .txt or .csv file.
    
Key Concepts Used: 
    dictionary, input/output, basic arithmetic, file handling
(optional).
"""
import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180, "TSLA": 250, "GOGL": 140, "MSFT": 330
}

portfolio = []
total_investment = 0
total_profit_loss = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# SAFE INPUT FUNCTION
def safe_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Number of stocks
num_stocks = int(safe_number_input("\nHow many stocks do you want to add? "))

# STOCK INPUT LOOP
for i in range(num_stocks):

    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:

        quantity = int(safe_number_input("Enter quantity: "))
        buy_price = safe_number_input("Enter purchase price per share: ")

        current_price = stock_prices[stock_name]
        # LOGIC/FORMULAE
        investment = buy_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - investment

        # Profit percentage calculation
        profit_percent = (profit_loss / investment) * 100

        total_investment += investment
        total_profit_loss += profit_loss

        portfolio.append([stock_name, buy_price, current_price, quantity, investment, current_value, profit_loss, profit_percent
        ])
        print(f"{stock_name} Current Value: ${current_value:.2f}")
    else:
        print("Stock not found. Skipping.")

# DISPLAY SUMMARY
print("_" * 50)
print("\nPortfolio Summary")

for stock in portfolio:
    print(
        f"{stock[0]} | Shares: {stock[3]} | "
        f"P/L: ${stock[6]:.2f} | "
        f"Return: {stock[7]:.2f}%"
    )

# Overall Profit percentage
overall_profit_percent = (total_profit_loss / total_investment) * 100

print("_" * 50)

print("\nTotal Investment: $", round(total_investment, 2))
print("Total Profit/Loss: $", round(total_profit_loss, 2))
print("Overall Return:", round(overall_profit_percent, 2), "%")

print("_" * 50)

# Profit/Loss Status
if total_profit_loss > 0:
    print("OVERALL PROFIT :) ")
elif total_profit_loss < 0:
    print("OVERALL LOSS :( ")
else:
    print("Break-even --> No profit and no loss")
print("_" * 50)

# Information SAVE Option
save_option = input("\nSave results? (txt / csv / no): ").lower()

# Save as TXT
if save_option == "txt":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")
        for stock in portfolio:
            file.write(
                f"{stock[0]} | P/L: ${stock[6]:.2f} | "
                f"Return: {stock[7]:.2f}%\n"
            )
        file.write(f"\nTotal Investment: ${total_investment:.2f}")
        file.write(f"\nTotal Profit/Loss: ${total_profit_loss:.2f}")
        file.write(f"\nOverall Return: {overall_profit_percent:.2f}%")
    print("Saved as portfolio.txt")

# Save as CSV
elif save_option == "csv":
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Stock", "Buy Price", "Current Price", "Quantity", "Investment", "Current Value", "Profit/Loss", "Return %"
        ])
        writer.writerows(portfolio)
    print("Saved as portfolio.csv")
else:
    print("Results not saved.")




























