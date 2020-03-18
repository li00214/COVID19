# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:55:54 2020

@author: Administrator
"""
import csv
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.dates as mdate
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter



#用reder读取csv文件
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def is_same_province(str, Province):   
    province = str[4]
    city = str[5]
    countryCode = str[2]
    #print(str[0])
    if province == Province and city == '' and countryCode == 'CN':
#        print(province,'   ', city)
        return True
    else:
        return False
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def is_same_country(str, Country):   
    countrycode = str[2]
    provinceCode = str[4]
    city = str[5]
    #print(str[0])
    if countrycode == Country and provinceCode == '' and city == '' :
#        print(Country,'   ', provinceCode)
        return True
    else:
        return False
    
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def is_between_time(str, start): 
    date2num = mdate.strpdate2num('%Y-%m-%d')
    if str[0] == 'date':
        return False
    else:
        datetime2 = date2num(str[0])
        #print(datetime2, 'datetime    in else   -------')       
        if datetime2 == float(start):
#            print(datetime2)
            return True
        else:
            return False
    
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def is_not_china(str, Country):   
    countrycode = str[2]
    provinceCode = str[4]
    city = str[5]
#    dateTime = date2num(str[0])  
    if countrycode != Country and provinceCode == '' and city == '' :
#        if dateTime == float(737394):
#            count++
#        print(Country,'   ', provinceCode)
        return True
    else:
        return False
    
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def is_not_Hubei(str, CountryCode):
    countrycode = str[2]
    province = str[3]
    provinceCode = str[4]
    city = str[5]
#    dateTime = date2num(str[0])  
    if countrycode == CountryCode and province!= '' and provinceCode != '420000' and city == '' :
#        if dateTime == float(737394):
#            count++
#        print(city,'   ', provinceCode)
        return True
    else:
        return False    
    
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10    
def is_country(str):
    province = str[3]
    provinceCode = str[4]
    city = str[5]
    cityCode = str[6]
#    dateTime = date2num(str[0])  
    if province == '' and provinceCode == '' and city == '' and cityCode == '':
#        if dateTime == float(737394):
#            count++
#        print(str[1],'   ', str[2])
        return True
    else:
        return False    
    
#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10    
def is_china(str, Country):
    countryCode = str[2]
    provinceCode = str[4]
    city = str[5]
#    dateTime = date2num(str[0])  
    if countryCode == Country and provinceCode == '' and city == '' :
#        if dateTime == float(737394):
#            count++
#        print(Country,'   ', provinceCode)
        return True
    else:
        return False

def filter_China(filename,resultfile,ProvinceCode):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_same_province(line, ProvinceCode):
            #print(line)
            writer.writerow(line)
    filetowrite.close()
    
def filter_foreign(filename,resultfile,CountryCode):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_same_country(line, CountryCode):
            #print(line)
            writer.writerow(line)
    filetowrite.close()

def confirm_date(date1,text1):
    date2num = mdate.strpdate2num('%Y-%m-%d')
    n = 0
    while date2num(date1) > float(text1 + n):
        n =  n + 1
#    print('confirm_data function:', n, date2num(date1), float(text1 + n))
    return n
        


#date,country,countryCode,province,provinceCode,city,cityCode,confirmed,suspected,cured,dead
#0      1       2            3        4          5      6       7        8         9     10
def filter_date(filename,resultfile, dateRange):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    date2num = mdate.strpdate2num('%Y-%m-%d')
#    date2str= str2date.strftime('%Y-%m-%d')
    num1 = 0
    num = 0 
    #dateRange1 = int( date2num(dateRange) - date2num('2019-12-01'));    num = num1 = 0
    k = 0
    sum_temp1 = [0] * 150  # five months
    sum_temp2 = [0] * 150
    sum_temp3 = [0] * 150
    sum_temp4 = [0] * 150
    j = 0 
#    sum_date = []
    for line in reader:
#        print(line)
        list2 = []
        if k < 0:
            k = k + 1
        else:
            if k == 0:
                num1 = confirm_date(line[0], float(737394))
                if is_between_time(line, 737394 + num1):
#                    print('--------if k==1 between---------', sum_temp1,'buchongshu',num1)
                    sum_temp1[j] = sum_temp1[j] + int(line[7])
                    sum_temp2[j] = sum_temp2[j] + int(line[8])
                    sum_temp3[j] = sum_temp3[j] + int(line[9])
                    sum_temp4[j] = sum_temp4[j] + int(line[10])
                    num = num1
                    k = 10000000000
#                    print('sum_temp   line[7]', j, line[7], sum_temp1[j],'buchongshu',num1, num, k)

            else:   
                num1 = confirm_date(line[0], float(737394))
#                print(num1,num,'else fenzhi      -=---==-================')
                if num < num1 :
#                k = 10000000
                    list2.append(mdate.num2date(737394 + num).strftime('%Y-%m-%d'))
                    list2.append(sum_temp1[j])
                    list2.append(sum_temp2[j])
                    list2.append(sum_temp3[j])
                    list2.append(sum_temp4[j])
#                    print(list2)
                    writer.writerow(list2)
                    j = j + 1
                    if is_between_time(line, 737394 + num1):
#                        print('--------else if between---------', sum_temp1)
                        sum_temp1[j] = sum_temp1[j] + int(line[7])
                        sum_temp2[j] = sum_temp2[j] + int(line[8])
                        sum_temp3[j] = sum_temp3[j] + int(line[9])
                        sum_temp4[j] = sum_temp4[j] + int(line[10])
#                        print('sum_temp[j]   line[7]    j', j, line[7], sum_temp1[j])
                        num = num1
                elif num == num1:
                    if is_between_time(line, 737394 + num1):
#                        print('--------else else between---------', sum_temp1)
#                        sum_temp[j] = sum_temp[j] + int(line[7])
                        sum_temp1[j] = sum_temp1[j] + int(line[7])
                        sum_temp2[j] = sum_temp2[j] + int(line[8])
                        sum_temp3[j] = sum_temp3[j] + int(line[9])
                        sum_temp4[j] = sum_temp4[j] + int(line[10])
                        num = num1
#                        print('sum_temp[j]   line[7]', j, line[7], sum_temp1[j])
    list2 = []
    list2.append(mdate.num2date(737394 + num1).strftime('%Y-%m-%d'))
    list2.append(sum_temp1[j])
    list2.append(sum_temp2[j])
    list2.append(sum_temp3[j])
    list2.append(sum_temp4[j])
#    print(list2)
    writer.writerow(list2)                   
#        sum_foreign.append(sum_temp)
#    writer.writerow(sum_foreign)
    filetowrite.close()  

def get_suspected_num(filename,resultfile):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_country(line):
            #print(line)
            writer.writerow(line)
    filetowrite.close()    

def full_of_all(filename,resultfile):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_country(line):
            #print(line)
            writer.writerow(line)
    filetowrite.close()    
    

def full_foreign(filename,resultfile,CountryCode):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_not_china(line, CountryCode):
            #print(line)
            writer.writerow(line)
    filetowrite.close()

def full_china(filename,resultfile,CountryCode):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_china(line, CountryCode):
            #print(line)
            writer.writerow(line)
    filetowrite.close()
    
def full_without_hubei(filename,resultfile,CountryCode):
    reader = csv.reader(open(filename,encoding='utf-8'))
    filetowrite = open(resultfile,'w', newline='',encoding='utf-8')
    writer = csv.writer(filetowrite)
    for line in reader:
        if is_not_Hubei(line, CountryCode):
            #print(line)
            writer.writerow(line)
    filetowrite.close()

#def full_of_all(filename,resultfile):
#    reader = csv.reader(open(filename))
#    filetowrite = open(resultfile,'w', newline='')
#    writer = csv.writer(filetowrite)
#    for line in reader:
#        if is_country(line):
#            #print(line)
#            writer.writerow(line)
#    filetowrite.close()
           
def get_province(filename,mainFile):
    reader = csv.reader(open(filename,encoding='utf-8'))
    for line in reader:
        dstFile = 'Province/'+line[2]+'.csv'       
#        print(dstFile)
        filter_China(mainFile,dstFile,line[1])        
    
def get_country(filename,mainFile):
    readerC = csv.reader(open(filename,encoding='utf-8'))
    for line in readerC:
        dstFile = 'Country/'+line[2]+'.csv'        
#        print(dstFile) 
        filter_foreign(mainFile,dstFile,line[1])    

def get_full_foreign(mainFile):
    dstFile = 'FullWithoutChina/FullWithoutChina.csv'   
    full_foreign(mainFile,dstFile,'CN')
    
def get_full_china(mainFile):
    dstFile = 'FullChina/FullChina.csv'   
    full_china(mainFile,dstFile,'CN')
    
def get_full_without_Hubei(mainFile):
    dstFile = 'FullWithoutHubei/FullWithoutHubei.csv'   
    full_without_hubei(mainFile,dstFile,'CN')
    
def get_total(mainFile):
    dstFile = 'FULL/FULL.csv'
    full_of_all(mainFile,dstFile)

def main_data_prepare(fileNameOfAll, dateTime):
    get_full_china(fileNameOfAll)
    filter_date('FullChina/FullChina.csv','DateOrder/TimeTestFullChina.csv', dateTime)
    get_full_foreign(fileNameOfAll)
    filter_date('FullWithoutChina/FullWithoutChina.csv','DateOrder/TimeTestFullForeign.csv', dateTime)
    get_full_without_Hubei(fileNameOfAll)
    filter_date('FullWithoutHubei/FullWithoutHubei.csv','DateOrder/TimeTestWithoutHubei.csv', dateTime) 
    get_total(fileNameOfAll)
    filter_date('FULL/FULL.csv','DateOrder/TimeTestFULL.csv', dateTime) 
    get_province('ProvinceCode.csv',fileNameOfAll)
    get_country('CountryCode.csv',fileNameOfAll)     
 
if __name__ == '__main__':
    
    fileNameOfAll='Wuhan-2019-nCoV.csv'
    filter_foreign(fileNameOfAll,'Country/The Republic of Namibia.csv','The Republic of Namibia')
    
#    filter_China('Wuhan-2019-nCoV.csv','Province/Xizang.csv','540000')  
#    confirm_date('2020-01-02', float(737394) ) 
#    print('---------------------------------EEEEEEEEEEEEEEEEE------------------------')
#    get_full_china('Wuhan-2019-nCoV.csv')
#    filter_date('FullChina/FullChina.csv','DateOrder/TimeTestFullChina.csv', '2020-03-03')
#    get_full_foreign('Wuhan-2019-nCoV.csv')
#    filter_date('FullWithoutChina/FullWithoutChina.csv','DateOrder/TimeTestFullForeign.csv', '2020-03-03')
#    get_full_without_Hubei('Wuhan-2019-nCoV.csv')
#    filter_date('FullWithoutHubei/FullWithoutHubei.csv','DateOrder/TimeTestWithoutHubei.csv', '2020-03-03') 
#    get_total('Wuhan-2019-nCoV.csv')
#    filter_date('FULL/FULL.csv','DateOrder/TimeTestFULL.csv', '2020-03-03') 
#    