import time

import numpy as np
import talib
import datetime

import yfinance as yf
import pandas as pd

# 指数的yfinance ticker符号
indices = {
    # "S&P 500": "^GSPC",                 ## 标普500
    "NASDAQ Composite": "^IXIC",  ## 纳斯达克
    # "DAX": "^GDAXI",                    ## 德国DAX指数
    # "FTSE 100": "^FTSE",                ## 英国富时100指数
    # "CAC 40": "^FCHI",                  ## 法国CAC40指数
    # "Nikkei 225": "^N225",              ## 日本日经指数
    # "Nifty 50": "^NSEI",                ## 印度Nifty50指数
    # "Shanghai Composite": "000001.SS",  ## 沪市综合指数
    # "Hang Seng Index": "^HSI",          ## 香港恒生指数
    # "BSE Sensex": "^BSESN",             ## 印度孟买指数
    # "Gold Continuous Contract": "GC=F",  ## 黄金连续合约
}

# 创建一个空的DataFrame来存储所有指数的数据
all_data = pd.DataFrame()

# 获取每个指数的日线数据
for name, ticker in indices.items():
    print(f"Fetching data for {name} ({ticker})")
    # data = yf.download(ticker, start="2009-01-01", end="2024-12-31", interval="1d", )
    data = yf.download(ticker, start="2009-01-01", end="2024-12-31", interval="1d", )

    # data['Index'] = name
    all_data = pd.concat([all_data, data])

# 将数据保存为CSV文件
# all_data.to_csv("indices_data.csv")

print("Data fetching complete!")
# all_data


import backtrader as bt
import pandas as pd

ATR_PERIOD = 10
PERIOD = 5*20
SYMBOL = "sma"
# 创建策略
class FortyDaySMAStrategy(bt.Strategy):
    params = (('sma_period', PERIOD),
              ('atr_period', ATR_PERIOD),
              )

    def __init__(self):
        self.boll = bt.indicators.BollingerBands(period=100, devfactor=2)
        self.dema = bt.indicators.DoubleExponentialMovingAverage(self.data.close, period=self.params.sma_period)
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.sma_period)
        # 计算 talib 指标
        self.ht_trendline = bt.talib.HT_TRENDLINE(self.data, timeperiod=self.params.sma_period)
        self.kama = bt.talib.KAMA(self.data, timeperiod=self.params.sma_period)
        self.ma = bt.talib.MA(self.data, timeperiod=self.params.sma_period)
        self.mama = bt.talib.MAMA(self.data)

        self.real = bt.talib.MIDPOINT(self.data, timeperiod=self.params.sma_period)

        # # 计算 MAVP
        # periods = np.random.randint(10, 50, size=100)
        # self.mavp = bt.talib.MAVP(self.data, periods, minperiod=10, maxperiod=50, matype=0)



    def next(self):
        pass

# 初始化Cerebro引擎
cerebro = bt.Cerebro()

# 添加策略
cerebro.addstrategy(FortyDaySMAStrategy)

all_data.reset_index(inplace=True)
all_data.columns = ['datetime', 'open', 'high', 'low', 'close', "_", 'volume']
all_data = all_data[['datetime', 'open', 'high', 'low', 'close', 'volume']]
all_data['datetime'] = pd.to_datetime(all_data['datetime'])
all_data.set_index("datetime", inplace=True)
data = bt.feeds.PandasData(dataname=all_data)

# 添加数据到Cerebro
cerebro.adddata(data)
cerebro.addobserver(bt.observers.Benchmark, data=data)

cerebro.broker = bt.brokers.BackBroker(coc=True)
# 设置初始资本
cerebro.broker.setcash(1000000.0)

# 添加分析器
cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

# 运行策略
results = cerebro.run()

# # 绘制结果
# cerebro.plot()

cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='pnl')  # 返回收益率时序数据
cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')  # 年化收益率
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')  # 夏普比率
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')  # 回撤

# # 启动回测
result = cerebro.run()

# 从返回的 result 中提取回测结果
strat = result[0]
# 返回日度收益率序列
# daily_return = pd.Series(strat.analyzers.pnl.get_analysis())
# 打印评价指标
write_str = f"\n"
write_str += str(strat.analyzers._AnnualReturn.get_analysis()) + "\n"
write_str += str(strat.analyzers._SharpeRatio.get_analysis()) + "\n"
write_str += str(strat.analyzers._DrawDown.get_analysis()) + "\n\n\n"
print("--------------- AnnualReturn -----------------")
print(strat.analyzers._AnnualReturn.get_analysis())
print("--------------- SharpeRatio -----------------")
print(strat.analyzers._SharpeRatio.get_analysis())
print("--------------- DrawDown -----------------")
print(strat.analyzers._DrawDown.get_analysis())

# cerebro.plot(style='candle', barup='red', bardown='green')
from btplotting import BacktraderPlotting
from btplotting.schemes import Tradimo


# 格式化日期为"%Y-%m-%d"
date_str = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
output_path = f"plot/result_{date_str}--PERIOD-{PERIOD}--{SYMBOL}.html"
p = BacktraderPlotting(style='line', plot_mode='single', scheme=Tradimo(), filename=output_path, output_mode='save')
cerebro.plot(p,)
