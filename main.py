import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("--- Running Pairs Trading Data Retrieval ---")

# --- 1. Define Tickers and Timeframe ---
ticker1 = 'KO'  # Coke
ticker2 = 'PEP' # Pepsi
start_date = '2020-01-01'

# --- 2. Download Data ---
# We only need the 'Adj Close' price column
try:
    data = yf.download([ticker1, ticker2], start=start_date)['Close']
    
    # Check if data is empty
    if data.empty:
        print("No data downloaded. Check tickers and date range.")
        exit()
    
    # Ensure we have data for both tickers
    if data[ticker1].isnull().all() or data[ticker2].isnull().all():
        print(f"Missing data for one or both tickers. Cannot proceed.")
        exit()
        
except Exception as e:
    print(f"Error downloading data: {e}")
    exit()


# --- 3. Calculate and Plot the Spread ---
# The 'spread' is the ratio of the two prices.
# We are betting that this ratio will return to its mean.
data['SPREAD'] = data[ticker1] / data[ticker2]

# --- 4. Print Head and Save Plot ---
print("Data downloaded and spread calculated successfully:")
print(data.head())

# Plot the spread over time
plt.figure(figsize=(10, 6))
data['SPREAD'].plot()
plt.title(f"{ticker1} / {ticker2} Price Ratio (Spread)")
plt.axhline(data['SPREAD'].mean(), color='red', linestyle='--', label='Spread Mean')
plt.legend()
plt.savefig('spread_plot.png') # Save the plot to a file

print(f"\nSuccessfully saved plot to 'spread_plot.png'.")
print("Notice how the spread (blue line) tends to return to the mean (red line).")

plt.show()

print("--- Data Retrieval Complete ---")