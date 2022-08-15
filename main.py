%matplotlib inline

import pandas as pd
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt


import yfinance as yf

# portfolio stocks
tickers = ['AAPL', 'CHV', 'TSLA']

# stock weights
weights = np.array([0.25, 0.35, 0.40])

# size of portfolio
portfolio_value = 1000

# confidence level
confidence = 0.05

# gather stock data from tickers
data =  yf.download(tickers, start='2018-01-01', end='2021-21-31')['Close']