from pandas_datareader import data
import datetime as dt
import pandas as pd
ticker = 'GLD'
start = '2008-11-11'
end = '2018-11-11'
#data1 = data.DataReader(ticker,'yahoo',dt.datetime(2014,11,11),dt.datetime(2016,11,11))
#print (data1)
#data1.head()
apple = data.DataReader("AAPL", "yahoo", start, end)
microsoft = data.DataReader("MSFT", "yahoo", start, end)
google = data.DataReader("GOOG", "yahoo", start, end)

stocks1 = pd.DataFrame({"AAPL": apple["High"],
                     "MSFT": microsoft["High"],
                     "GOOG": google["High"]})
stocks2 = pd.DataFrame({"AAPL": apple["High"]})
stocks2.plot(kind='line', title='HIGH', fontsize=9, figsize=(16,9))
stocks3 = pd.DataFrame({"MSFT": microsoft["High"]})
stocks3.plot(kind='line', title='HIGH', fontsize=9, figsize=(16,9))
stocks4 = pd.DataFrame({"GOOG": google["High"]})
stocks4.plot(kind='line', title='HIGH', fontsize=9, figsize=(16,9))
#print("HIGH")
#print(stocks1)
stocks1.plot(kind='line', title='HIGH', fontsize=9, figsize=(16,9))

stocks = pd.DataFrame({"AAPL": apple["Adj Close"],
                     "MSFT": microsoft["Adj Close"],
                     "GOOG": google["Adj Close"]})
#print("Adj Close")
print(stocks)
#print(stocks.head())
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
print(stocks.describe())