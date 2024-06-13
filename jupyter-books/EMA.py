
#  指数平均数 EMA 

import akshare as ak

import talib

import matplotlib.pyplot as plt

data = ak.stock_zh_a_hist(symbol="000001", period="daily",start_date="20150101", adjust="qfq")


# 计算双重指数移动平均线（EMA）
data['EMA21'] = talib.EMA(data['收盘'], timeperiod=21)

# 计算双重指数移动平均线（EMA）
data['EMA10'] = talib.EMA(data['收盘'], timeperiod=10)

# 计算双重指数移动平均线（EMA）
data['EMA5'] = talib.EMA(data['收盘'], timeperiod=5)



# 计算双重指数移动平均线（DEMA）
data['DEMA21'] = talib.DEMA(data['收盘'], timeperiod=21)

# 计算双重指数移动平均线（DEMA）
data['DEMA10'] = talib.DEMA(data['收盘'], timeperiod=10)

# 计算双重指数移动平均线（DEMA）
data['DEMA5'] = talib.DEMA(data['收盘'], timeperiod=5)


# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(data['收盘'], label='Close Price', color='black')
plt.plot(data['EMA5'], label='EMA5', color='red')
plt.plot(data['EMA10'], label='EMA10', color='orange')
plt.plot(data['EMA21'], label='EMA21', color='green')


plt.plot(data['DEMA5'], label='DEMA5', color='pink')
plt.plot(data['DEMA10'], label='DEMA10', color='yellow')
plt.plot(data['DEMA21'], label='DEMA21', color='blue')

plt.title(f'Exponential Moving Average (DEMA)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()