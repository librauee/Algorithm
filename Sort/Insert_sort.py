# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:35:42 2020

@author: Administrator
"""

A=[3,9,7,1,2,99,6,53]

def insert_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    return A

print(insert_sort(A))  