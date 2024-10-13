import yfinance as yf

# Function to fetch the latest NIFTY50 close value.
def get_latest_nifty50_close():
    ticker = yf.Ticker("^NSEI")
    data = ticker.history(period="1d")  # Get today's data
    if not data.empty:
        return data['Close'].iloc[-1]
    else:
        print("Error: Could not fetch today's NIFTY50 data.")
        return None

# Function to fetch the all-time highest close value of NIFTY50.
def get_all_time_high():
    ticker = yf.Ticker("^NSEI")
    data = ticker.history(period="max")  # Get all historical data
    if not data.empty:
        return data['Close'].max()  # Find the highest close value
    else:
        print("Error: Could not fetch historical NIFTY50 data.")
        return None

# Main function to compare the latest close with the all-time high.
def main():
    latest_close = get_latest_nifty50_close()
    all_time_high = get_all_time_high()

    if latest_close is None or all_time_high is None:
        return  # Exit if data couldn't be fetched.

    if latest_close >= all_time_high:
        print(f"New peak detected! NIFTY50 closed at {latest_close}.")
    else:
        drop_percentage = ((all_time_high - latest_close) / all_time_high) * 100
        print(f"NIFTY50 is currently {drop_percentage:.2f}% below its peak of {all_time_high}.")

if __name__ == "__main__":
    main()
