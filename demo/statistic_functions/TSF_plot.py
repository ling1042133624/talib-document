import pandas as pd
import akshare as ak
import talib

ningde_hist_df = ak.stock_zh_a_hist(symbol="300750", period="daily", start_date="19900101", end_date='21000101', adjust="qfq")
bank_hist_df = ak.stock_zh_a_hist(symbol="601988", period="daily", start_date="19900101", end_date='21000101', adjust="qfq")
fund_etf_hist_em_df = ak.fund_etf_hist_em(symbol="159915", period="daily", start_date="20000101", end_date="21000101", adjust="qfq")

import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt

# 下载历史价格数据
stock = yf.download("AAPL", start="2022-01-01", end="2023-01-01")

# 获取收盘价
price_series = ningde_hist_df["收盘"].values

# 计算时间序列预测值
time_period = 20  # 使用20天的窗口
tsf = talib.TSF(price_series, timeperiod=time_period)

# 绘制收盘价和时间序列预测值
plt.figure(figsize=(14, 7))
plt.plot(price_series, label='收盘价')
plt.plot(tsf, label='时间序列预测值', linestyle='--')
plt.legend()
plt.title('601988')
plt.show()
