import pandas as pd
import akshare as ak
import talib

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="300750", period="daily", start_date="19900101", end_date='21000101', adjust="qfq")
fund_etf_hist_em_df = ak.fund_etf_hist_em(symbol="159915", period="daily", start_date="20000101", end_date="21000101", adjust="qfq")
stock_zh_a_hist_df_s=stock_zh_a_hist_df[stock_zh_a_hist_df["日期"]>pd.to_datetime("2021-01-01")]
fund_etf_hist_em_df_s = fund_etf_hist_em_df[pd.to_datetime(fund_etf_hist_em_df["日期"])>pd.to_datetime("2021-01-01")]

fund_etf_hist_em_df_s["日期"] = pd.to_datetime(fund_etf_hist_em_df_s["日期"])
stock_zh_a_hist_df_s["日期"] = pd.to_datetime(stock_zh_a_hist_df_s["日期"])
merge_stock_zh_df = pd.merge(stock_zh_a_hist_df_s[["日期", "涨跌幅"]], fund_etf_hist_em_df_s[["日期", "涨跌幅"]], how="inner", on="日期")

# 填充缺失值为上一条记录的涨跌幅
merge_stock_zh_df["涨跌幅_x"].fillna(method="ffill", inplace=True)
merge_stock_zh_df["涨跌幅_y"].fillna(method="ffill", inplace=True)
# 计算BETA
beta = talib.BETA(merge_stock_zh_df["涨跌幅_x"], merge_stock_zh_df["涨跌幅_y"], timeperiod=5)
print(beta)