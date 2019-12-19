# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:06:03 2019

@author: Administrator
"""


def print_queen():
    print(Queen)

def check(row,column):
    for i in range(8):
        if Queen(i,column)==1:
            return False
    

def find_Queen(row):
    if row>7:
        print_queen()
        return 
    
    for column in range(8):
        if check(row,column):
            Queen[row][column]=1
            find_Queen(row+1)
            Queen[row][column]=0
            
            
