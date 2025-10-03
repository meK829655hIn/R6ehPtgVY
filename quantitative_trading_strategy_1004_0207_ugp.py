# 代码生成时间: 2025-10-04 02:07:25
import yfinance as yf
import pandas as pd
from gradio import Gradio, components

"""
Quantitative Trading Strategy
This application demonstrates a basic quantitative trading strategy using Python and Gradio.
It fetches historical stock data and calculates moving averages to identify buy/sell signals.
"""

# Define the supported stocks
SUPPORTED_STOCKS = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]

# Function to fetch historical stock data
def fetch_stock_data(stock, start_date, end_date):
    try:
        data = yf.download(stock, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None

# Function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    data["Short_MA"] = data["Adj Close"].rolling(window=short_window).mean()
    data["Long_MA"] = data["Adj Close"].rolling(window=long_window).mean()
    return data

# Function to generate buy/sell signals
def generate_signals(data):
    signals = pd.DataFrame(index=data.index)
    signals["signal"] = 0.0
    signals.loc[data["Short_MA"] > data["Long_MA"], "signal"] = 1.0
    signals.loc[data["Short_MA"] < data["Long_MA"], "signal"] = -1.0
    return signals

# Define the Gradio interface
def trading_strategy_ui(stock, start_date, end_date, short_window, long_window):
    data = fetch_stock_data(stock, start_date, end_date)
    if data is not None:
        data = calculate_moving_averages(data, short_window, long_window)
        signals = generate_signals(data)
        return data, signals
    else:
        return "Error fetching data", None

# Create the Gradio interface
iface = Gradio(components.Dropdown(label="Stock", choices=SUPPORTED_STOCKS, value=SUPPORTED_STOCKS[0]),
            components.DatePicker(label="Start Date", value="2020-01-01"),
            components.DatePicker(label="End Date", value="2023-01-01"),
            components.Slider(label="Short Window", minimum=5, maximum=20, step=1, value=10),
            components.Slider(label="Long Window", minimum=20, maximum=50, step=1, value=30),
            fn=trading_strategy_ui,
            inputs=["dropdown", "date-picker", "date-picker", "slider", "slider"],
            outputs=["dataframe", "dataframe"])

iface.launch(share=True)