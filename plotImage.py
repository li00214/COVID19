import csv
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.dates as mdate
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
from pylab import mpl

def plot_image(resultDst,x,y1,y2,y3,y4,Title,dateEnd):   
    date2num = mdate.strpdate2num('%Y-%m-%d')
    mpl.rcParams['font.size'] = 18
    fig = plt.figure(figsize=(30,15)) 
    ax1 = fig.add_subplot(1,1,1)
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    autodate = mdate.AutoDateLocator()
    ax1.xaxis.set_major_locator(autodate)  # 设置时间间隔
    # 设置时间标签显示格式
    dateFmt = mdate.DateFormatter('%y%m%d')
    ax1.xaxis.set_major_formatter(dateFmt)
    # 将x轴次刻度标签设置为61的倍数
    xminorLocator = MultipleLocator(61)
    # 显示次刻度标签的位置,没有标签文本
    ax1.xaxis.set_minor_locator(xminorLocator)
    #ax1.set_xticks() # 设置x轴间隔 
    ax1.set_xlim(date2num('2019-12-01'),date2num(dateEnd)) # 设置x轴范围
    ax1.xaxis.set_major_locator(mdate.DayLocator(bymonthday=range(1,32), interval=5))
    #x_major = MultipleLocator(locaterOfX)
    #ax1.yaxis.set_major_locator(x_major)
    plt.xticks(rotation=45) # 显示日期旋转90度 
    
    plt.title(u''+Title)
    A, = plt.plot(x,y1,label='确诊人数',linewidth=2.0)
    B, = plt.plot(x,y2,label='疑似人数',linewidth=2.0)
    C, = plt.plot(x,y3,label='治愈人数',linewidth=2.0)
    D, = plt.plot(x,y4,label='死亡人数',linewidth=2.0)

    plt.legend(handles=[A,B,C,D])

    plt.grid(True)
    plt.xlabel(u'日期')
    plt.ylabel(u'人数')
    #plt.legend(loc=2,prop={'family':'SimHei','size':12}) # loc=2 : upper left
    plt.savefig(resultDst, dpi=100)
#    plt.draw()
#    plt.show()


def plot_image_Accumulated(filename,resultDst,Title,dateEnd):
    #lists = np.loadtxt(filename,delimiter=',',unpack=True)
    date2num = mdate.strpdate2num('%Y-%m-%d')
    reader = csv.reader(open(filename,encoding='utf-8'))
    x = [] 
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    xF = []
    yF1 = []
    yF2 = []
    yF3 = []
    yF4 = []

    for line in reader:     
        xF.append(date2num(line[0]))
        yF1.append(float(line[7]))   #confirmed
        yF2.append(float(line[8]))   #suspected
        yF3.append(float(line[9]))   #cured
        yF4.append(float(line[10]))   #dead                 
        
    if xF[0] > float(737394):
        for i in range(0, int (xF[0] - float(737394)) ):
            x.append(float(737394 + i))
            y1.append(float(0))
            y2.append(float(0))
            y3.append(float(0))
            y4.append(float(0))
            
    x.extend(xF)    
    y1.extend(yF1)      
    y2.extend(yF2)  
    y3.extend(yF3)      
    y4.extend(yF4)
    
    Title1 = Title + '累计确诊、疑似、治愈和死亡人数情况'
    resultDst1 = resultDst+'_accumulated_image.jpg'
    plot_image(resultDst1,x,y1,y2,y3,y4,Title1,dateEnd)
    
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    
    b1.append(y1[0]-0) #confirmed
    for i in range(len(y1)-1):
        m = y1[i+1] + y3[i+1] - y1[i] 	#后者减前者
        b1.append(m)	#添加元素到新列表
#    print(b1)
#    print(len(y1),len(b1))
    
    b2.append(y2[0]-0) 
    for i in range(len(y2)-1):
        m = y2[i+1] - y2[i] 	#后者减前者
        b2.append(m)	#添加元素到新列表
#    print(b2)
#    print(len(y2),len(b2))
    
    b3.append(y3[0]-0) 
    for i in range(len(y3)-1):
        m = y3[i+1] - y3[i] 	#后者减前者
        b3.append(m)	#添加元素到新列表
#    print(b3)
#    print(len(y3),len(b3))
    
    b4.append(y4[0]-0) 
    for i in range(len(y4)-1):
        m = y4[i+1] - y4[i] 	#后者减前者
        b4.append(m)	#添加元素到新列表
#    print(b4)
#    print(len(y4),len(b4))    
    
    Title2 = Title + '较前日新增确诊、疑似、治愈和死亡人数情况'    
    resultDst2 = resultDst+'_increase_image.jpg'
    plot_image(resultDst2,x,b1,b2,b3,b4,Title2,dateEnd)
    
    
    
def plot_image_special(filename,resultDst,Title,dateEnd):
    date2num = mdate.strpdate2num('%Y-%m-%d')
    reader = csv.reader(open(filename,encoding='utf-8'))
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    xF = []
    yF1 = []
    yF2 = []
    yF3 = []
    yF4 = []

    for line in reader:     
        xF.append(date2num(line[0]))
        yF1.append(float(line[1]))   #confirmed
        yF2.append(float(line[2]))   #suspected
        yF3.append(float(line[3]))   #cured
        yF4.append(float(line[4]))   #dead   
    print(xF,yF1)
        
    if xF[0] > float(737394):
        for i in range(0, int (xF[0] - float(737394)) ):
            x.append(float(737394 + i))
            y1.append(float(0))
            y2.append(float(0))
            y3.append(float(0))
            y4.append(float(0))
    else:
         x = [] 
         y1 = []
         y2 = []
         y3 = []
         y4 = []
#            
    x.extend(xF)    
    y1.extend(yF1)      
    y2.extend(yF2)  
    y3.extend(yF3)      
    y4.extend(yF4)
    
    
#    print(y1)
#    print(y2)
#    print(len(y1))
    
    Title1 = Title + '累计确诊、疑似、治愈和死亡人数情况'
    resultDst1 = resultDst+'_accumulated_image.jpg'
    plot_image(resultDst1,x,y1,y2,y3,y4,Title1,dateEnd)
    
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    
    b1.append(y1[0]-0) 
    for i in range(len(y1)-1):
        m1 = (y1[i+1] + y3[i+1] - y1[i]) 	#后者减前者
        b1.append(m1)	#添加元素到新列表
#    print(b1)
#    print(len(y1),len(b1))
    
    b2.append(y2[0]-0) 
    for i in range(len(y2)-1):
        m = (y2[i+1] - y2[i]) 	#后者减前者(当日疑似病例减去(前日疑似+今日确诊))
        b2.append(m)	#添加元素到新列表
#    print(b2)
#    print(len(y2),len(b2))
    
    b3.append(y3[0]-0) 
    for i in range(len(y3)-1):
        m = (y3[i+1] - y3[i]) 	#后者减前者
        b3.append(m)	#添加元素到新列表
#    print(b3)
#    print(len(y3),len(b3))
    
    b4.append(y4[0]-0) 
    for i in range(len(y4)-1):
        m = (y4[i+1] - y4[i]) 	#后者减前者
        b4.append(m)	#添加元素到新列表
#    print(b4)
#    print(len(y4),len(b4))    
    
    Title2 = Title + '新增确诊、疑似、治愈和死亡人数情况'    
    resultDst2 = resultDst+'_increase_image.jpg'
    plot_image(resultDst2,x,b1,b2,b3,b4,Title2,dateEnd)
#    
#      

def plot_image_auto_coutry(filename,dateEnd,dateTitle):
    readerC = csv.reader(open(filename,encoding='utf-8'))
    for line in readerC:
        dstFile = 'Country/'+line[2]+'' 
        readFile = 'Country/'+line[2]+'.csv'
#        print(dstFile) 
        plot_image_Accumulated(readFile,dstFile,dateTitle+line[0],dateEnd)


def plot_image_auto_province(filename,dateEnd,dateTitle):
    readerC = csv.reader(open(filename,encoding='utf-8'))
    for line in readerC:
        dstFile = 'Province/'+line[2]+'' 
        readFile = 'Province/'+line[2]+'.csv'
#        print(dstFile) 
        plot_image_Accumulated(readFile,dstFile,dateTitle+line[0],dateEnd)

def plot_image_FULL(filename,dateEnd,dateTitle):
        dstFile = 'DateOrder/FULL' 
#        print(dstFile) 
        dateTitle = dateTitle + '全球' 
        plot_image_special(filename,dstFile,dateTitle,dateEnd)

def plot_image_foreign(filename,dateEnd,dateTitle):
        dstFile = 'DateOrder/FullForeign' 
#        print(dstFile) 
        dateTitle = dateTitle + '国外' 
        plot_image_special(filename,dstFile,dateTitle,dateEnd)

def plot_image_china(filename,dateEnd,dateTitle):
        dstFile = 'DateOrder/FullChina' 
#        print(dstFile) 
        dateTitle = dateTitle + '全国' 
        plot_image_special(filename,dstFile,dateTitle,dateEnd)

def plot_image_without_hubei(filename,dateEnd,dateTitle):
        dstFile = 'DateOrder/WithoutHubei' 
#        print(dstFile) 
        dateTitle = dateTitle + '非湖北' 
        plot_image_special(filename,dstFile,dateTitle,dateEnd)

def main_plot(filename,dateEnd,dateTitle):
    plot_image_auto_province('ProvinceCode.csv',dateEnd,dateTitle)
    plot_image_auto_coutry('CountryCode.csv',dateEnd,dateTitle)
    
    plot_image_FULL('DateOrder/TimeTestFULL.csv',dateEnd,dateTitle)
    plot_image_china('DateOrder/TimeTestFullChina.csv',dateEnd,dateTitle)
    plot_image_without_hubei('DateOrder/TimeTestWithoutHubei.csv',dateEnd,dateTitle)
    plot_image_foreign('DateOrder/TimeTestFullForeign.csv',dateEnd,dateTitle)    ####bug in  datetime
                

#For testing
#if __name__ == '__main__':
#    dateEnd='2020-03-03'
#    dateTitle='20191201-20200303'
#    date2num = mdate.strpdate2num('%Y-%m-%d')
#    plot_image_Accumulated('Republic of Korea.csv','Republic of Korea', dateTitle+'韩国', dateEnd)
#    plot_image_Accumulated('Hubei.csv','Hubei', dateTitle+'湖北', dateEnd)
#    plot_image_Accumulated('Beijing.csv','Beijing',dateTitle+'北京',dateEnd)