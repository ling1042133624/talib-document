# 布林线指标 BBANDS

import akshare as ak

import talib
import pandas as pd

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import mpl_finance as mpf
import matplotlib.dates as mdates


data = ak.stock_zh_a_hist(symbol="000001", period="daily", adjust="qfq")


# 计算布林带指标
data['upper_band'], data['middle_band'], data['lower_band'] = talib.BBANDS(data['收盘'], timeperiod=20, nbdevup=2, nbdevdn=2)

# 将日期转换为mpf模块需要的数字格式
data['日期'] = mdates.date2num(data['日期'])

# 准备绘图数据
quotes = list(zip(data['日期'], data['开盘'], data['最高'], data['最低'], data['收盘']))

# 绘制布林带图表
fig, ax = plt.subplots(figsize=(10, 6))
mpf.candlestick_ohlc(ax, quotes, width=0.6, colorup='r', colordown='g', alpha=0.8)

ax.plot(data['日期'], data['upper_band'], label='Upper Band', color='red', linestyle='--')
ax.plot(data['日期'], data['middle_band'], label='Middle Band', color='green', linestyle='--')
ax.plot(data['日期'], data['lower_band'], label='Lower Band', color='red', linestyle='--')

# 设置x轴日期显示格式
ax.xaxis_date()

# 显示图例
ax.legend()

# 设置图表标题和标签
plt.title(f'Bollinger Bands')
plt.xlabel('日期')
plt.ylabel('股价')

plt.show()