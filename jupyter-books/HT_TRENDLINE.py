

# 希尔伯特瞬时变换 HT_TRENDLINE

import akshare as ak

import talib

import matplotlib.pyplot as plt

data = ak.stock_zh_a_hist(symbol="000001", period="daily",start_date="20150101", adjust="qfq")


# 计算双重指数移动平均线（DEMA）
data['HT_TRENDLINE'] = talib.HT_TRENDLINE(data['收盘'])

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(data['收盘'], label='Close Price', color='black')
plt.plot(data['HT_TRENDLINE'], label='DEMA5', color='red')

plt.title(f'HT_TRENDLINE ')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()