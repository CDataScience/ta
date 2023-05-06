import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

# Download data from Yahoo Finance
symbol = "AAPL"  # Example stock symbol (Apple Inc.)
start_date = "2022-01-01"  # Example start date
end_date = "2022-12-31"  # Example end date

data = yf.download(symbol, start=start_date, end=end_date).reset_index()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Resample the data to the desired time frame (e.g., daily, weekly)
# Here, we'll resample it to weekly candlesticks
weekly_data = data.resample('W').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
daily_data  = data.resample('W').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
# Reset the index
weekly_data.reset_index(inplace=True)

# Convert the 'Date' column to the required format for mplfinance
weekly_data['Date'] = weekly_data['Date'].apply(mdates.date2num)

# Create a new figure and subplot
fig, ax = plt.subplots()

# Plot the candlestick chart
candlestick_ohlc(ax, weekly_data.values, width=0.9, colorup='green', colordown='red')

# Set the x-axis label to display dates
ax.xaxis_date()

# Set the x-axis tick labels to rotate for better readability
plt.xticks(rotation=45)

# Set the title and labels
plt.title('Weekly Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Price')

# Show the plot
plt.show(block=True)
