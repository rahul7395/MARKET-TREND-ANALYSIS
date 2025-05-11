import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random stock-like data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=100)
prices = np.cumsum(np.random.randn(100) * 2 + 0.5) + 100  # Random walk

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Close': prices
})
df.set_index('Date', inplace=True)

# Calculate random "trends"
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# Calculate daily returns
df['Daily Return'] = df['Close'].pct_change()

# Plot: Close Price & Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['SMA_10'], label='10-Day SMA', color='green', linestyle='--')
plt.plot(df['SMA_20'], label='20-Day SMA', color='orange', linestyle='--')
plt.title("Random Market Trend (Close Price with SMA)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot: Daily Returns Distribution
plt.figure(figsize=(10, 4))
sns.histplot(df['Daily Return'].dropna(), bins=20, kde=True, color='purple')
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.tight_layout()
plt.show()

# Plot: Heatmap of correlation
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Close', 'SMA_10', 'SMA_20', 'Daily Return']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
