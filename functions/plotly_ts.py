import yfinance as yf
import plotly.express as px

def plot(ticker:str):
    """
    plot a time series

    Args:
        ticker (str): to company ticker.

    Returns:
        a plotly time series.
    """
    data = yf.download(ticker, period='max', multi_level_index=False)
    df = data.reset_index()[['Date','Close']]

    fig = px.line(df, x = 'Date', y = 'Close',title = f'historico de {ticker}' )
    return fig