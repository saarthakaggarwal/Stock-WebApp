import yfinance as yf
import plotly.graph_objects as go


def test():
    tsla = yf.Ticker('TSLA')
    hist = tsla.history(period='1y')

    print(hist)