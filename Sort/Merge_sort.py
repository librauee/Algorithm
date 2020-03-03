# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:37:05 2020

@author: Administrator
"""

A=[3,9,7,1,2,99,6,53]

def merge_sort(A):
    if len(A)==1:
        return A
    left=merge_sort(A[:int(len(A)/2)])
    right=merge_sort(A[int(len(A)/2):])
    return merge(left,right)

def merge(left,right):
    c=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            c.append(left[i])
            i+=1
        else:
            c.append(right[j])
            j+=1
    if len(left)==i:
        for k in right[j:]:
            c.append(k)
    else:
        for k in left[i:]:
            c.append(k)
    print(c)
    return c
    

print(merge_sort(A))