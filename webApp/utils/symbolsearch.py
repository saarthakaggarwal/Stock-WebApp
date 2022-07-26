import finnhub
import yfinance as yf
import pandas


def symbolexists(symbol):
    stock = yf.Ticker(symbol)           
    hist = stock.history(period='3mo', interval = "1d")   
    return not hist.empty

