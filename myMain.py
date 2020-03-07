import csv
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.dates as mdate
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
from plotImage import main_plot,plot_image_foreign
from PrePareData import main_data_prepare

if __name__ == '__main__':
#    get_province('ProvinceCode.csv','Wuhan-2019-nCoV.csv')
#    get_country('CountryCode.csv','Wuhan-2019-nCoV.csv')   
    fileNameOfAll='Wuhan-2019-nCoV.csv'
    dateTime='2020-03-07'
    dateTitle='20191201-20200307'
    main_data_prepare(fileNameOfAll, dateTime)
    
    print('---------------------- Data Pre-processing End ---------------------')
    
#    dateEnd='2020-03-03'
#    dateTitle='20191201-20200303'
#    plot_image_auto_coutry('CountryCode.csv',dateEnd, dateTitle)
#    plot_image_auto_province('ProvinceCode.csv',dateEnd, dateTitle)
#    print('--------------------- Image Ploting End-----------------------------')
    
    main_plot(fileNameOfAll,dateTime,dateTitle)
    print('--------------------- Image Ploting End-----------------------------')
#    main_plot(fileNameOfAll,dateTime,dateTitle)
    
#    getFullForeign('test3.csv')
#    plot_image('Hubei.csv','Hubei.jpg',2500)
    
    