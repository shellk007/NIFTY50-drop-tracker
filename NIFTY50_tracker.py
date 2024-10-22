import yfinance as yf

# Function to fetch the latest close value for a given index.
def get_latest_close(index_ticker):
    try:
        ticker = yf.Ticker(index_ticker)
        data = ticker.history(period="1d")  # Get today's data
        if not data.empty:
            return data['Close'].iloc[-1]
        else:
            print(f"Error: Could not fetch today's data for {index_ticker}.")
            return None
    except Exception as e:
        print(f"Error fetching latest close for {index_ticker}: {e}")
        return None

# Function to fetch the all-time highest close value for a given index.
def get_all_time_high(index_ticker):
    try:
        ticker = yf.Ticker(index_ticker)
        data = ticker.history(period="max")  # Get all historical data
        if not data.empty:
            return data['Close'].max()  # Find the highest close value
        else:
            print(f"Error: Could not fetch historical data for {index_ticker}.")
            return None
    except Exception as e:
        print(f"Error fetching all-time high for {index_ticker}: {e}")
        return None

# Main function to compare the latest close with the all-time high for multiple indices.
def main():
    indices = {
        "NIFTY50": "^NSEI",
        "NIFTYMIDCAP50": "^NSEMDCP50",
    }

    for index_name, index_ticker in indices.items():
        latest_close = get_latest_close(index_ticker)
        all_time_high = get_all_time_high(index_ticker)

        if latest_close is None or all_time_high is None:
            print(f"Skipping {index_name} due to data issues.")
            continue  # Skip to the next index if data couldn't be fetched.

        if latest_close >= all_time_high:
            print(f"{index_name}: New peak detected! Closed at {latest_close}.")
        else:
            drop_percentage = ((all_time_high - latest_close) / all_time_high) * 100
            print(f"{index_name}: Currently {drop_percentage:.2f}% ({latest_close}) below its peak of {all_time_high}.")

if __name__ == "__main__":
    main()
    input("Press Enter to close...")
