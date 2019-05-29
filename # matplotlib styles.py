# matplotlib.styles
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
import numpy as np
import urllib 

style.use('dark_background')


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep,'-', label='Price', color='k')
    ax1.fill_between(date, closep, 225, where=(closep > [100]), label='Profit', alpha=0.5, color='g')
    ax1.fill_between(date, closep, 225, where=(closep < [100]), label='Loss', alpha=0.5, color='orange')
                         
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    ax1.grid(True, color ='k', linestyle='-' )
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('b')
    ax1.set_yticks([0,200,400,600,800])
    
    #ax1.spines['left'].set_color('#58AFD0')
    ax1.spines['left'].set_linewidth(2)
    
    ax1.tick_params(axis = 'x', colors='#58AFD0')
        
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('"TSLA" Stock Price\nProfit vs. Loss')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90,wspace=.2, hspace=0)
    plt.show()


graph_data('TSLA')