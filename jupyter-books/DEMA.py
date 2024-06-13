# 双移动平均线 DEMA

import akshare as ak

import talib
import pandas as pd

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import mpl_finance as mpf
import matplotlib.dates as mdates


data = ak.stock_zh_a_hist(symbol="000001", period="daily",start_date="20150101", adjust="qfq")


# 计算双重指数移动平均线（DEMA）
data['DEMA21'] = talib.DEMA(data['收盘'], timeperiod=21)

# 计算双重指数移动平均线（DEMA）
data['DEMA10'] = talib.DEMA(data['收盘'], timeperiod=10)

# 计算双重指数移动平均线（DEMA）
data['DEMA5'] = talib.DEMA(data['收盘'], timeperiod=5)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(data['收盘'], label='Close Price', color='black')
plt.plot(data['DEMA5'], label='DEMA5', color='red')
plt.plot(data['DEMA10'], label='DEMA10', color='orange')
plt.plot(data['DEMA21'], label='DEMA21', color='green')

plt.title(f'Double Exponential Moving Average (DEMA)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()