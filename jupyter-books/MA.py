
#  移动平均线 MA
# PERIOD_LIST=[5,10,15,30]
PERIOD_LIST=[10,21]
import akshare as ak

import talib

import matplotlib.pyplot as plt

data = ak.stock_zh_a_hist(symbol="000001", period="daily",start_date="20150101", adjust="qfq")


# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(data['收盘'], label='Close Price', color='black')

for period in PERIOD_LIST:
    # 计算指标
    data[f'MA{period}'] = talib.MA(data['收盘'], timeperiod=period)
    # 画图
    plt.plot(data[f'MA{period}'], label=f'MA{period}')

    # # 计算双重指数移动平均线（EMA）
    # data[f'EMA{period}'] = talib.EMA(data['收盘'], timeperiod=period)
    # # 画图
    # plt.plot(data[f'EMA{period}'], label=f'EMA{period}')

    # 计算双重指数移动平均线（EMA）
    data[f'DEMA{period}'] = talib.DEMA(data['收盘'], timeperiod=period)
    # 画图
    plt.plot(data[f'DEMA{period}'], label=f'DEMA{period}')


plt.title(f'KAMA ')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()