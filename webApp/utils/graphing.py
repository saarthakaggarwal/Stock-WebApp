import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot
import time
from dash import Dash, dcc, html, Input, Output



def makePlot(symbol):
    spy = yf.Ticker(symbol)
    hist = spy.history(period='3mo', interval = "1d")
    

    graphs = []

    graphs.append(
        go.Candlestick(x=hist.index,
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                             )
    )

    layout = {
        'xaxis_title': 'Time',
        'yaxis_title': 'Price ($)',
        'height' : 600,
        'paper_bgcolor' : 'rgba(0,0,0,0)',
         'plot_bgcolor':'rgba(0,0,0,0)'
    }


    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div', show_link=False, link_text="",config = {'displayModeBar': False, 'responsive': True})
    return plot_div

def returnnews():
    spy = yf.Ticker('SPY')
    jsonData = spy.news


    return jsonData[:3]