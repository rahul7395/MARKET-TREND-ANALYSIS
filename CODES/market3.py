# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

# Generate a sample market data for the analysis
np.random.seed(42)

# Simulating a stock price over a year (daily data)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
stock_prices = np.random.randn(len(dates)) * 2 + 100  # Random walk around 100

# Create a DataFrame
market_data = pd.DataFrame({"Date": dates, "Stock_Price": stock_prices})
market_data["Date"] = pd.to_datetime(market_data["Date"])

# Add moving averages (simple trend analysis)
market_data['SMA_30'] = market_data['Stock_Price'].rolling(window=30).mean()  # 30-day moving average
market_data['SMA_100'] = market_data['Stock_Price'].rolling(window=100).mean()  # 100-day moving average

# Plot the stock price and moving averages
plt.figure(figsize=(14, 7))

# Plot stock prices
plt.plot(market_data['Date'], market_data['Stock_Price'], label='Stock Price', color='blue', alpha=0.7)

# Plot the moving averages
plt.plot(market_data['Date'], market_data['SMA_30'], label='30-Day Moving Average', color='green', linestyle='--')
plt.plot(market_data['Date'], market_data['SMA_100'], label='100-Day Moving Average', color='red', linestyle='--')

# Customize plot
plt.title('Market Trend Analysis: Stock Price with Moving Averages', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()

# Correlation between stock price and moving averages
correlation_30 = market_data['Stock_Price'].corr(market_data['SMA_30'])
correlation_100 = market_data['Stock_Price'].corr(market_data['SMA_100'])

print(f"Correlation between Stock Price and 30-Day Moving Average: {correlation_30:.2f}")
print(f"Correlation between Stock Price and 100-Day Moving Average: {correlation_100:.2f}")

# 1. Histogram of Stock Prices
plt.figure(figsize=(10, 6))
sns.histplot(market_data['Stock_Price'], kde=True, color='blue', bins=30)
plt.title('Distribution of Stock Prices', fontsize=16)
plt.xlabel('Stock Price ($)')
plt.ylabel('Frequency')
plt.show()

# 2. Heatmap of Correlations between Stock Price and Moving Averages
correlation_matrix = market_data[['Stock_Price', 'SMA_30', 'SMA_100']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap: Stock Price vs Moving Averages', fontsize=16)
plt.show()

# 3. Box Plot of Stock Price
plt.figure(figsize=(10, 6))
sns.boxplot(x=market_data['Stock_Price'], color='orange')
plt.title('Box Plot of Stock Prices', fontsize=16)
plt.xlabel('Stock Price ($)')
plt.show()
