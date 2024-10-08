import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


ticker_symbol = 'GOOGL'
start_date = '2023-01-01'
end_date = '2023-12-31'
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)


plt.figure(figsize=(10, 5))
plt.bar(stock_data.index, stock_data['Volume'], label='Trading Volume')
plt.title(f'Trading Volume of {ticker_symbol} from {start_date} to {end_date}')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.legend()
plt.grid(True)
plt.show()
