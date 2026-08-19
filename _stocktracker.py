# Simple Stock Portfolio Tracker
# Stock prices are predefined for this project
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 185
}

def show_available_stocks():
    """Display the stocks available in the tracker."""

    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} - ${price}")

def calculate_portfolio():
    """Take user input and calculate the total investment."""

    portfolio = {}
    total_investment = 0

    print("\nLet's build your portfolio!")
    print("Type 'done' when you have finished adding stocks.")

    while True:

        stock = input("\nEnter stock symbol: ").upper().strip()

        # Stop adding stocks
        if stock == "DONE":
            break

        # Check if the stock exists
        if stock not in stock_prices:
            print("Sorry, that stock isn't available.")
            print("Please choose from the available stocks.")
            continue

        # Get quantity
        quantity_input = input(f"How many shares of {stock} do you own? ")

        # Make sure quantity is a valid number
        if not quantity_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        quantity = int(quantity_input)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        # Calculate investment for this stock
        investment = stock_prices[stock] * quantity

        # Add stock to portfolio
        portfolio[stock] = quantity

        total_investment += investment

        print(
            f"Added {quantity} share(s) of {stock}. "
            f"Investment: ${investment:,.2f}"
        )

    # Display portfolio summary
    print("\n" + "=" * 40)
    print("           PORTFOLIO SUMMARY")
    print("=" * 40)

    if not portfolio:
        print("Your portfolio is empty.")
        return

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity

        print(
            f"{stock}: {quantity} share(s) "
            f"= ${investment:,.2f}"
        )

    print("-" * 40)
    print(f"Total Investment: ${total_investment:,.2f}")
    print("=" * 40)

def main():
    """Start the stock portfolio tracker."""

    print("=" * 40)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    print("\nWelcome! Let's calculate your investments.")

    show_available_stocks()

    calculate_portfolio()

    print("\nThanks for using the Stock Portfolio Tracker!")

# Start the program
if __name__ == "__main__":
    main()
