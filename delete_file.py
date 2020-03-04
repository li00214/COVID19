# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:49:59 2020

@author: Administrator
"""
import os
 
def delete_image_file(pathName):
    '''删除.txt文件'''
    for maindir,subdir,file_name_list in os.walk(pathName):
        for filename in file_name_list:
            if(filename.endswith(".jpg")):
                os.remove(maindir+"\\"+filename)

def delete_special_file(pathName):

    files = os.listdir(pathName)
    for i, f in enumerate(files):
        if f.find("cat") >= 0 :
            print(i)
            os.remove(pathName + f)

#For testing
if __name__ == '__main__':
    pathName = 'Country/'
    delete_image_file(pathName)
    pathName = 'Province/'
    delete_image_file(pathName)
