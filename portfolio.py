import yfinance as yf
import pandas as pd
import numpy as np
import random
import datetime
import matplotlib.pyplot as plt
# Read and print the stock tickers that make up S&P500
sptab = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = sptab['Symbol'].tolist()
nb_asset = np.random.randint(80,200)
# nb_asset = 5
print(nb_asset)
asset_list = random.sample(tickers, nb_asset)
print(asset_list)
start_time = datetime.datetime(2010,1,1)
size_momentum = 1000
end_time = datetime.datetime(2016,1,1)
df = yf.download(asset_list, start= start_time, end = end_time, group_by="tickers")
print(df)
NAV= pd.DataFrame({'Date':datetime.date(2009,12,31),'NAV':100}, index=[0])


for i in range(1,size_momentum,1):
    returns_total = pd.DataFrame(columns=["Date","tickers","return"])
    for j in asset_list:
        returns=df[j]['Close'].pct_change()
        new_return = [x for x in returns if np.isnan(x) == False]
        if len(new_return)<size_momentum:
            break
        new_row = pd.DataFrame({'Date':df.index[i],'tickers':j, 'return':returns[i]},index=[0])
        returns_total = pd.concat([new_row,returns_total]).reset_index(drop=True)
    returns_total['quintile']=pd.cut(returns_total['return'],2, labels = [1,5])
    sum_long = 0
    sum_short = 0
    count_long = 0
    count_short = 0
    for ni in range(0,len(returns_total)):
        if returns_total['quintile'][ni] == 5:
            sum_long=+(1+returns_total['return'][ni])
            count_long=+1
        if returns_total['quintile'][ni] == 1:
            sum_short=+(1-returns_total['return'][ni])
            count_short=+1
    nav_new = 0.5*NAV['NAV'][i-1]*sum_long/count_long+0.5*NAV['NAV'][i-1]*sum_short/count_short
    new_df = {'Date':returns_total['Date'][1],'NAV':nav_new}
    NAV= NAV.append(new_df,ignore_index=True)
print(NAV)
plt.plot('Date','NAV',data=NAV)
plt.xlabel('Date')
plt.ylabel('NAV')
plt.show()





