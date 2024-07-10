import numpy as np
import talib
import datetime
import backtrader as bt

import yfinance as yf
import pandas as pd

# 指数的yfinance ticker符号
indices = {
    # "S&P 500": "^GSPC",                 ## 标普500
    # "NASDAQ Composite": "^IXIC",  ## 纳斯达克
    # "DAX": "^GDAXI",                    ## 德国DAX指数
    # "FTSE 100": "^FTSE",                ## 英国富时100指数
    # "CAC 40": "^FCHI",                  ## 法国CAC40指数
    # "Nikkei 225": "^N225",              ## 日本日经指数
    # "Nifty 50": "^NSEI",                ## 印度Nifty50指数
    "Shanghai Composite": "000001.SS",  ## 沪市综合指数
    # "Hang Seng Index": "^HSI",          ## 香港恒生指数
    # "BSE Sensex": "^BSESN",             ## 印度孟买指数
    # "Gold Continuous Contract": "GC=F",  ## 黄金连续合约
    # "ASHR":"ASHR",   ## 美股的沪深300
}

# 创建一个空的DataFrame来存储所有指数的数据
all_data = pd.DataFrame()

# 获取每个指数的日线数据
for name, ticker in indices.items():
    print(f"Fetching data for {name} ({ticker})")
    # data = yf.download(ticker, start="2019-05-01", end="2024-12-31", interval="1d", )
    data = yf.download(ticker, start="1990-01-01", end="2024-12-31", interval="1d", )

    all_data = pd.concat([all_data, data])

print("Data fetching complete!")

ATR_PERIOD = 10
PERIOD = 5 * 20
SYMBOL = "sma"


# 创建策略
class FortyDaySMAStrategy(bt.Strategy):
    params = (('sma_period', PERIOD),
              ('atr_period', ATR_PERIOD),
              ('di_period', 22)
              )
    scale_factor = 2

    def __init__(self):
        # 对纳指的买入点 较为有效
        # # 计算14日威廉指标
        # self.WILLR = bt.talib.WILLR(self.data.high, self.data.low, self.data.close, timeperiod=66)
        # self.EMA = bt.talib.EMA(self.WILLR, timeperiod=10)
        # self.EMA.plotinfo.plotmaster = self.WILLR

        # 名称： Three-Line Strike 三线打击
        # 简介：四日K线模式，前三根阳线，每日收盘价都比前一日高， 开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。
        self.integer = bt.talib.CDL3OUTSIDE(self.data.open, self.data.high, self.data.low, self.data.close)

        # self.buy_index = None
        # self.sell_index = None
        # self.position_percent = 0.0

        # self.indicators()

    def next(self):
        if self.integer[0] != 0:
            print(f"{self.data.datetime.date(), self.integer[0]}")
        # if self.integer[-1]!=0:
        # print(self.integer[0])
        #
        # buy_index = (self.short_avg[0] > self.long_avg[0]) & (self.short_avg[-1] <=self.long_avg[-1])
        # sell_index = (self.short_avg[0] < self.long_avg[0]) & (self.short_avg[-1] >=self.long_avg[-1])
        # if buy_index:
        #     # self.buy()
        #     self.position_percent += 0.2
        #     self.position_percent = 1 if self.position_percent > 1 else self.position_percent
        #     self.order = self.order_target_percent(target=self.position_percent)
        # if sell_index:
        #     # self.sell()
        #     self.position_percent -= 0.4
        #     self.position_percent = 0 if self.position_percent < 0 else self.position_percent
        #     self.order = self.order_target_percent(target=self.position_percent)
        pass

    def indicators(self):
        # 输出：0代表不符合k线形态，-100表示符合形态，100表示符合相反的形态。

        # 两只乌鸦 Two Crows
        # 第一跟K线：长阳线。
        # 第二根K线：阴线，和第一根K线之间存在缺口。
        # 第三根K线：阴线，开盘价位于第二根k线实体之间，收盘价位于第一根k线实体之间。
        self.CDL2CROWS = bt.talib.CDL2CROWS(self.data.open, self.data.high, self.data.low, self.data.close)

        # 名称：Three Black Crows 三只乌鸦
        # 简介：三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价， 每日开盘价都在上根K线实体内，预示股价下跌。
        self.CDL3BLACKCROWS = bt.talib.CDL3BLACKCROWS(self.data.open, self.data.high, self.data.low, self.data.close)

        # 名称：Three Black Crows 三只乌鸦
        # 简介：三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价， 每日开盘价都在上根K线实体内，预示股价下跌。
        self.integer = bt.talib.CDL3INSIDE(self.data.open, self.data.high, self.data.low, self.data.close)

        # 名称： Three-Line Strike 三线打击
        # 简介：四日K线模式，前三根阳线，每日收盘价都比前一日高， 开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。
        # 阳阳阳阴100，阴阴阴阳-100
        self.integer = bt.talib.CDL3LINESTRIKE(self.data.open, self.data.high, self.data.low, self.data.close)

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
# cerebro.addobserver(bt.observers.Benchmark, data=data)

cerebro.broker = bt.brokers.BackBroker(coc=True)
# 设置初始资本
cerebro.broker.setcash(1000000.0)

# 添加分析器
cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

# 运行策略
# results = cerebro.run()

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

cerebro.plot(style='candle', barup='red', bardown='green')
# from btplotting import BacktraderPlotting,BacktraderPlottingOptBrowser
# from btplotting.schemes import Tradimo
#
# # 格式化日期为"%Y-%m-%d"
# date_str = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
# output_path = f"plot/all_indicators.html"
# p = BacktraderPlotting(style='line', plot_mode='single', scheme=Tradimo(), filename=output_path, output_mode='save',)
# cerebro.plot(p, )

# from btplotting import BacktraderPlotting
# from btplotting.schemes import Tradimo
#
# # 格式化日期为"%Y-%m-%d"
# date_str = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
# output_path = f"plot/all_indicators.html"
# p = BacktraderPlotting(style='line', plot_mode='single', scheme=Tradimo(), filename=output_path, output_mode='save')
# cerebro.plot(p, )
