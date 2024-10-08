import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker_symbol = 'GOOGL'
start_date = '2023-01-01'
end_date = '2023-12-31'


stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)


plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='Close Price')
plt.title(f'Historical Stock Prices of {ticker_symbol} from {start_date} to {end_date}')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
