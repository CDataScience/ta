import yfinance as yf
import ta
import mplfinance as mpf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_technical_indicators(stock_data):
    # Calculate Bollinger Bands
    stock_data['bb_bbm'] = ta.volatility.BollingerBands(stock_data['Close']).bollinger_mavg()
    stock_data['bb_bbh'] = ta.volatility.BollingerBands(stock_data['Close']).bollinger_hband()
    stock_data['bb_bbl'] = ta.volatility.BollingerBands(stock_data['Close']).bollinger_lband()
    
    # Calculate RSI
    stock_data['rsi'] = ta.momentum.RSIIndicator(stock_data['Close']).rsi()
    
    return stock_data

def plot_stock_data_with_indicators(stock_data, ticker):
    # Plot candlestick chart with Bollinger Bands
    
    apds = [
        mpf.make_addplot(stock_data['bb_bbm'], color='blue'),
        mpf.make_addplot(stock_data['bb_bbh'], color='red'),
        mpf.make_addplot(stock_data['bb_bbl'], color='red'),
        mpf.make_addplot(stock_data['rsi'],    color='black')
    ]

    
    mpf.plot(
        stock_data,
        type='candle',
        style='charles',
        title=f'{ticker} Bollinger Bands',
        ylabel='Price',
        addplot=apds,
        volume=True
    )
    plt.show()
    
# Example usage
ticker = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-12-31'

stock_data = fetch_stock_data(ticker, start_date, end_date)
stock_data = calculate_technical_indicators(stock_data)

stock_data.to_csv('indicators.csv')


plot_stock_data_with_indicators(stock_data, ticker)
