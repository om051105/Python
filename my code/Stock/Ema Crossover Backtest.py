import pandas as pd
import matplotlib.pyplot as plt

# ===============================================
# 🧾 STEP 1: LOAD YOUR DATASET
# ===============================================
data = pd.read_csv(r"C:\Users\singh\OneDrive\Documents\Python\my code\Stock\stock_data.csv")

# Clean column names
data.columns = data.columns.str.strip()
print("✅ Columns found:", data.columns.tolist())

# ===============================================
# 🧠 STEP 2: DEFINE DATE & CLOSE COLUMNS
# ===============================================
# Change these if your file has different column names
date_col = 'Date'
close_col = 'Close'

# Convert Date column to datetime format
data[date_col] = pd.to_datetime(data[date_col])
data = data.sort_values(date_col)

# ===============================================
# ⚙️ STEP 3: CALCULATE EMAs
# ===============================================
data['EMA_10'] = data[close_col].ewm(span=10, adjust=False).mean()
data['EMA_50'] = data[close_col].ewm(span=50, adjust=False).mean()

# ===============================================
# 💹 STEP 4: GENERATE BUY/SELL SIGNALS
# ===============================================
data['Signal'] = 0
data.loc[data['EMA_10'] > data['EMA_50'], 'Signal'] = 1
data['Position'] = data['Signal'].diff()

# ===============================================
# 📈 STEP 5: PLOT PRICE, EMAs, SIGNALS
# ===============================================
plt.figure(figsize=(12,6))
plt.plot(data[date_col], data[close_col], label='Close Price', alpha=0.6)
plt.plot(data[date_col], data['EMA_10'], label='EMA 10', linestyle='--')
plt.plot(data[date_col], data['EMA_50'], label='EMA 50', linestyle='--')

# Mark Buy & Sell points
plt.plot(data[data['Position'] == 1][date_col],
         data[data['Position'] == 1][close_col], '^', color='g', markersize=10, label='Buy Signal')
plt.plot(data[data['Position'] == -1][date_col],
         data[data['Position'] == -1][close_col], 'v', color='r', markersize=10, label='Sell Signal')

plt.title("📊 EMA Crossover Strategy Backtest")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# ===============================================
# 💰 STEP 6: CALCULATE STRATEGY PERFORMANCE
# ===============================================
data['Return'] = data[close_col].pct_change()
data['Strategy_Return'] = data['Signal'].shift(1) * data['Return']
total_return = (data['Strategy_Return'] + 1).prod() - 1

print(f"📈 Total Strategy Return: {total_return*100:.2f}%")
