#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 00:02:23 2018

@author: mdanishs
"""
from datetime import datetime

transactions = []
dates = []
with open('Data/rawtafeng/D01','r') as testFile:
    testFile.readline()
    for line in testFile:
        date = line.split(';')[0]
        print(date)
        date= date.split(' ')[0]
        print(date)
        dates.append(datetime.strptime(date,'%Y-%m-%d'))
        transactions.append(line)
        break;
        
with open('Data/rawtafeng/D02','r') as testFile:
    for line in testFile:        
        transactions.append(line)

with open('Data/rawtafeng/D11','r') as testFile:
    for line in testFile:        
        transactions.append(line)

with open('Data/rawtafeng/D12','r') as testFile:
    for line in testFile:        
        transactions.append(line)

print((transactions[-1]))
print(dates[0])