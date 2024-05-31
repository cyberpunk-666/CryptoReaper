import pandas as pd
import talib

# Example data (closing prices)
closing_prices = [100, 102, 105, 110, 108, 115, 120, 118, 122, 125]

# Convert data to pandas Series
close_series = pd.Series(closing_prices)

# Calculate MACD with default parameters (12-day EMA, 26-day EMA, 9-day Signal)
macd, signal, _ = talib.MACD(close_series)

# Detect crossings
crossings = []

# Loop through each time point (starting from the second time point)
for i in range(1, len(macd)):
    # Check for upward crossover (MACD line crosses above Signal line)
    if macd[i-1] < signal[i-1] and macd[i] > signal[i]:
        crossings.append((i, 'upward'))
    # Check for downward crossover (MACD line crosses below Signal line)
    elif macd[i-1] > signal[i-1] and macd[i] < signal[i]:
        crossings.append((i, 'downward'))

# Print the detected crossings
print("Detected Crossings:")
for index, direction in crossings:
    print(f"Crossing at index {index}, direction: {direction}")