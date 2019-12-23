# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:06:03 2019

@author: Administrator
"""


def print_queen():
    
    print(Queen)
    for i in range(8):
        for j in range(8):
            if Queen[i][j]==1:
                print('☆ '*j+'★ '+'☆ '*(7-j))
    print("\n\n")
            
            
def check(row,column):
    
    # 检查行列
    for k in range(8):
        if Queen[k][column]==1:
            return False
        
    # 检查主对角线    
    
    for i,j in zip(range(row-1,-1,-1),range(column-1,-1,-1)):
        if Queen[i][j]==1:
            return False   
        
    # 检查副对角线     
    for i,j in zip(range(row-1,-1,-1),range(column+1,8)):
        if Queen[i][j]==1:
            return False          

    return True
    
    

def find_Queen(row):

    if row>7:
        global count
        count+=1
        print_queen()
        return
    
    for column in range(8):
        if check(row,column):
            Queen[row][column]=1
            find_Queen(row+1)
            Queen[row][column]=0

          
if __name__=='__main__':    
     
    Queen=[[0 for i in range(8)] for i in range(8)]
    count=0
    find_Queen(0)
    print(count)
            
            
 


# 另解           
def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)
queen([None]*8)



