import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for market trend analysis
data = {
    'Month': ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
    'Gaming': [15000, 20000, 25000, 10000, 5000, 15000],
    'StockMarket': [10000, 11000, 9000, 13000, 12000, 12500],
    'Electronics': [8000, 9500, 10000, 10500, 11000, 11500]
}

df = pd.DataFrame(data)

# Set style
sns.set(style='whitegrid')

# 1. Line Chart - Sales Trend Over Time
plt.figure(figsize=(10,6))
for category in ['Electronics', 'StockMarket', 'Gaming']:
    plt.plot(df['Month'], df[category], marker='o', label=category)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart - Sales in Each Category in Last Month
plt.figure(figsize=(8,5))
last_month_sales = df.iloc[-1, 1:]  # Last row, excluding 'Month'
last_month_sales.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Sales by Category in JULY')
plt.xlabel('Category')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.show()

# 3. Pie Chart - Market Share in Last Month
plt.figure(figsize=(6,6))
plt.pie(last_month_sales, labels=last_month_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Market Share by Category in JULY')
plt.tight_layout()
plt.show()

# 4. Histogram - Distribution of Electronics Sales
plt.figure(figsize=(8,5))
plt.hist(df['Electronics'], bins=5, color='orange', edgecolor='black')
plt.title('Distribution of Electronics Sales')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
