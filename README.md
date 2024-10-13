# NIFTY50 Tracker Script 📈

This Python script tracks the **NIFTY50 index's highest closing value** and prints how much the current close is below the all-time peak. It fetches live and historical data from **Yahoo Finance** using the `yfinance` library and provides daily insights about the market status. The script is designed to run **automatically every evening**.

---

## Features 🛠️

- **Fetches today's closing value** of the NIFTY50 index.
- **Finds the all-time highest close** dynamically from Yahoo Finance historical data.
- **Calculates the percentage drop** from the highest close if the latest close is lower.
- **Prints a message** if a new peak is reached.
- No need for local storage — all data is fetched directly from Yahoo Finance.

---

## Prerequisites 📋

Make sure you have the following installed:

- **Python 3.x**: You can download it from [Python's official site](https://www.python.org/).
- **`yfinance` library**: To fetch stock market data from Yahoo Finance.

You can install `yfinance` by running:
```bash
pip install yfinance
