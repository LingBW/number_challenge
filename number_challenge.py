# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 22:10:32 2014

@author: san
"""

import random
import xlrd
import time
######################

row_list = []
fname = "Number-challenge-data.xls"
bk = xlrd.open_workbook(fname) #打开文件
sh = bk.sheet_by_name("Sheet1") #选择其中的表格
#Data = sh.col_values(0) #列值
nrows = sh.nrows #显示行数
for i in range(0,nrows):
    row_data = sh.row_values(i) #行值
    row_list.append(row_data)
try:
    challenge_num = input('Enter the number of rounds you want to challenge: ')
except:
    challenge_num = input('Please enter a Number: ')
#print t
r = 0
w = 0

for i in range(challenge_num):
    
    d_num = random.choice(row_list) #随机选择数列中的一个值
    print 'Challenge number: ',int(d_num[0]) #display a number randomly
    e_num = raw_input('Your answer: ')
    #time.sleep(5)
    if e_num == d_num[1]:
        print 'Correct !'
        r=r+1
    else : 
        print 'Wrong !'
        w=w+1
print 'Finished the challenge! ','\nTrue:',r, 'Flaut:',w
raw_input()
#print random.choice(data)



