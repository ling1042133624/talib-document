import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt

# 下载历史价格数据
stock = yf.download("AAPL", start="2022-01-01", end="2023-01-01")

# 获取收盘价
price_series = stock['Adj Close'].values

# 计算方差
time_period = 20  # 使用20天的窗口
nbdev = 1  # 使用默认缩放因子
var = talib.VAR(price_series, timeperiod=time_period, nbdev=nbdev)

# 绘制收盘价和方差
plt.figure(figsize=(14, 7))
plt.plot(price_series, label='收盘价')
plt.plot(var, label='方差', linestyle='--')
plt.legend()
plt.title('AAPL收盘价及其方差')
plt.show()
