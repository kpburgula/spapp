import yfinance as yf
import streamlit as st
from nsetools import Nse

nse = Nse()
all_stock_codes = nse.get_stock_codes()

## Page expands to full width
st.set_page_config(layout="wide")
# expander_bar = st.expander("About")
st.write("""
# Stock Price App
Shown are the stock **closing price** and ***volume***
""")
cont = st.container()
col1 = st.sidebar
col2, col3 = st.columns((2))

col1.header('Select valid NSE symbol')
# ticker_symbol = 'HINDUNILVR.NS'
# ticker_symbol = col1.text_area('NSE Symbol', ticker_symbol, height=10)
ticker_stock = col1.selectbox('NSE Symbols', list(all_stock_codes.values()))
# print(all_stock_codes)

all_stocks = dict(map(reversed, all_stock_codes.items()))
ticker_symbol = all_stocks[ticker_stock]

col1.write(f'The ticker symbol is {ticker_symbol}')

# get data on this ticker
tickerData = yf.Ticker(ticker_symbol + '.NS')
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-10-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


cont.write("""
## Closing Price
""")
cont.line_chart(tickerDf.Close)

col2.write("""
## High Price
""")
col2.line_chart(tickerDf.High)
col3.write("""
## Volume
""")
col3.bar_chart(tickerDf.Volume)
