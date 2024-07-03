import numpy as np
import talib
import datetime
import backtrader as bt

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
        # 计算14日威廉指标
        self.WILLR = bt.talib.WILLR(self.data.high, self.data.low, self.data.close, timeperiod=66)
        self.EMA = bt.talib.EMA(self.WILLR, timeperiod=10)
        self.EMA.plotinfo.plotmaster = self.WILLR

        self.buy_index = None
        self.sell_index = None
        self.position_percent = 0.0

        # self.indicators()

    def indicators(self):
        # 对纳指有效
        self.adx = bt.talib.ADX(self.data.high, self.data.low, self.data.close, timeperiod=self.params.di_period)
        self.adxr = bt.talib.ADXR(self.data.high, self.data.low, self.data.close, timeperiod=self.params.di_period)
        self.adxr.plotinfo.plotmaster = self.adx
        # ADXR(high, low, close, timeperiod=14)
        # 计算 +DI 和 -DI
        self.plus_di = bt.talib.PLUS_DI(self.data.high, self.data.low, self.data.close,
                                        timeperiod=self.params.di_period)
        self.minus_di = bt.talib.MINUS_DI(self.data.high, self.data.low, self.data.close,
                                          timeperiod=self.params.di_period)
        self.minus_di.plotinfo.plotmaster = self.plus_di

        # 计算 APO
        self.apo = bt.talib.APO(self.data, fastperiod=20, slowperiod=100, matype=3)

        # 计算 AROON Up 和 AROON Down
        self.aroon = bt.talib.AROON(self.data.high, self.data.low, timeperiod=self.params.sma_period)
        self.aroonosc = bt.talib.AROONOSC(self.data.high, self.data.low, timeperiod=self.params.sma_period)
        self.aroonosc.plotinfo.plotmaster = self.aroon

        # 计算 BOP
        self.bop = bt.talib.BOP(self.data.open, self.data.high, self.data.low, self.data.close)

        # self.buy_index = None
        # self.sell_index = None
        self.cci = bt.talib.CCI(self.data.high, self.data.low, self.data.close, timeperiod=PERIOD)
        self.buy_index = self.cci >= 100
        self.sell_index = self.cci <= -100
        self.position_percent = 0

        # 对纳指有效
        # 计算 CMO
        self.cmo = bt.talib.CMO(self.data, timeperiod=PERIOD)

        # 对纳指有效
        self.DX = bt.talib.DX(self.data.high, self.data.low, self.data.close, timeperiod=PERIOD)
        self.DXR = bt.talib.EMA(self.DX, timeperiod=66)
        self.plus_di = bt.talib.PLUS_DI(self.data.high, self.data.low, self.data.close,
                                        timeperiod=PERIOD)
        self.minus_di = bt.talib.MINUS_DI(self.data.high, self.data.low, self.data.close,
                                          timeperiod=PERIOD)
        self.plus_di.plotinfo.plotmaster = self.DX
        self.minus_di.plotinfo.plotmaster = self.DX
        self.DXR.plotinfo.plotmaster = self.DX

        # 对纳指  买点较有效
        scale_factor = 1
        self.macd = bt.talib.MACD(self.data.close, fastperiod=12 * scale_factor, slowperiod=26 * scale_factor,
                                  signalperiod=9 * scale_factor)

        # 与MACD雷同，用来做买点的选在比较有效
        scale_factor = 2
        self.MACDEXT = bt.talib.MACDEXT(self.data.close,
                                        fastperiod=12 * scale_factor, fastmatype=1,
                                        slowperiod=26 * scale_factor, slowmatype=0,
                                        signalperiod=9 * scale_factor, signalmatype=0)

        # 计算 MFI 指标
        self.mfi = bt.talib.MFI(self.data.high, self.data.low, self.data.close, self.data.volume, timeperiod=22)

        # 对纳指无效
        self.MOM = bt.talib.real = bt.talib.MOM(self.data.close, timeperiod=22)

        # 对纳指无效
        self.PPO = bt.talib.PPO(self.data.close, fastperiod=12, slowperiod=26, matype=0)
        self.PPO_EMA_signal = bt.talib.EMA(self.PPO, timeperiod=9)
        self.PPO_hist = self.PPO - self.PPO_EMA_signal
        self.EMA.plotinfo.plotmaster = self.PPO

        # ROC系列 用来确认买入或者处于上升周期较好用
        # 选择时间周期
        timeperiod = 125

        # 计算ROC
        self.ROC = bt.talib.ROC(self.data.close, timeperiod=timeperiod)

        # 计算ROCP
        self.ROCP = bt.talib.ROCP(self.data.close, timeperiod=timeperiod)

        # 计算ROCR
        self.ROCR = bt.talib.ROCR(self.data.close, timeperiod=timeperiod)

        # 计算ROCR100
        self.ROCR100 = bt.talib.ROCR100(self.data.close, timeperiod=timeperiod)

        # self.ROCP.plotinfo.plotmaster = self.ROC
        self.ROCR.plotinfo.plotmaster = self.ROCP
        self.ROCR100.plotinfo.plotmaster = self.ROC

        ##################################################################################
        # 对纳指的买点有效
        # 计算RSI
        self.RSI = bt.talib.real = bt.talib.RSI(self.data.close, timeperiod=66)

        ##################################################################################
        fastk_period = 14
        slowk_period = 3
        slowd_period = 3
        # 计算STOCH
        self.STOCH = bt.talib.STOCH(self.data.high, self.data.low, self.data.close,
                                    fastk_period=9 * 8,
                                    slowk_period=slowk_period * 8,
                                    slowk_matype=0,
                                    slowd_period=slowd_period * 8,
                                    slowd_matype=0)
        # 计算STOCHF
        self.STOCHF = bt.talib.STOCHF(self.data.high, self.data.low, self.data.close,
                                      fastk_period=fastk_period,
                                      fastd_period=3,
                                      fastd_matype=0)

        # 计算STOCHRSI
        self.STOCHRSI = bt.talib.STOCHRSI(self.data.close,
                                          timeperiod=14,
                                          fastk_period=14,
                                          fastd_period=3,
                                          fastd_matype=0)

        ##################################################################################

        # 纳指用来判断涨跌的置信区间 TRIX
        self.TRIX = bt.talib.TRIX(self.data.close, timeperiod=22)

        ##################################################################################
        # 获取ULTOSC指标值
        # 对纳指 买点确认较有效
        # timeperiod1 = 7, timeperiod2 = 14, timeperiod3 = 28
        self.ULTOSC = bt.talib.ULTOSC(self.data.high, self.data.low, self.data.close, timeperiod1=15, timeperiod2=30, timeperiod3=60)
        self.EMA_s = bt.talib.EMA(self.ULTOSC, timeperiod=10)
        self.EMA_l = bt.talib.EMA(self.ULTOSC, timeperiod=20)
        self.EMA_s.plotinfo.plotmaster = self.ULTOSC
        self.EMA_l.plotinfo.plotmaster = self.ULTOSC

        ##################################################################################
        # 对纳指的买入点 较为有效
        # 计算14日威廉指标
        self.WILLR = bt.talib.WILLR(self.data.high, self.data.low, self.data.close, timeperiod=66)
        self.EMA = bt.talib.EMA(self.WILLR, timeperiod=10)
        self.EMA.plotinfo.plotmaster = self.WILLR

        # talib.ADX()

    def next(self):
        # self.buy_index = self.RSI[0] > 43 >= self.RSI[-1]
        # self.sell_index = self.RSI[0] < 64 <= self.RSI[-1]
        # if self.buy_index:
        #     # self.buy()
        #     self.position_percent += 0.2
        #     self.position_percent = 1 if self.position_percent > 1 else self.position_percent
        #     self.order = self.order_target_percent(target=self.position_percent)
        # if self.sell_index:
        #     # self.sell()
        #     self.position_percent -= 0.4
        #     self.position_percent = 0 if self.position_percent < 0 else self.position_percent
        #     self.order = self.order_target_percent(target=self.position_percent)
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
output_path = f"plot/all_indicators.html"
p = BacktraderPlotting(style='line', plot_mode='single', scheme=Tradimo(), filename=output_path, output_mode='save')
cerebro.plot(p, )
