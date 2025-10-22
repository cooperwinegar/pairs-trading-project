import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("--- Running Pairs Trading Data Retrieval ---")

# Define tickers and start date
ticker1 = 'KO'  # Coke
ticker2 = 'PEP' # Pepsi
start_date = '2020-01-01'

# Download data
try:
    data = yf.download([ticker1, ticker2], start=start_date)['Close']
    
    # Check if data is empty
    if data.empty:
        print("No data downloaded.")
        exit()
    
    # Ensure we have data for both tickers
    if data[ticker1].isnull().all() or data[ticker2].isnull().all():
        print("Missing data for one or both tickers.")
        exit()
        
except Exception as e:
    print(f"Error downloading data: {e}")
    exit()


# Calculate and plot the spread
data['SPREAD'] = data[ticker1] / data[ticker2]

# Print head and save plot
print("Data downloaded and spread calculated successfully:")
print(data.head())

# Plot the spread over time
plt.figure(figsize=(10, 6))
data['SPREAD'].plot()
plt.title(f"{ticker1} / {ticker2} Price Ratio (Spread)")
plt.axhline(data['SPREAD'].mean(), color='red', linestyle='--', label='Spread Mean')
plt.legend()
plt.savefig('spread_plot.png')

print(f"\nSuccessfully saved plot.")

plt.show()

print("Data retrieval complete")