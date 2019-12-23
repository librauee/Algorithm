# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:16:19 2019

@author: Administrator
"""

def Quick_Sort(A,p,r):
    if p<r:
        q=Partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q,r)

        
def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def Quick_Sort_Random(A,p,r):
    if p<r:
        q=Partition1(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q,r)

        
def Partition1(A,p,r):
    k=random.randint(p,r)
    A[k],A[r]=A[r],A[k]

    return Partition(A,p,r)




import random   

def quicksort_0(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_0(left) + middle + quicksort_0(right)

def quicksort_mid(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_mid(left) + middle + quicksort_mid(right)


def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot_index=random.randint(0,len(arr)-1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + middle + quicksort_random(right)


A=[random.randint(1,1000000) for i in range(10000)]
A=quicksort_random(A)

import time

time1,time2,time3,time4,time5=[],[],[],[],[]
for i in range(1,4):

    
    start1=time.time()
    quicksort_0(A)
    end1=time.time()
    time1.append(end1-start1)
    print('第{}次排序用时{:.3f}s'.format(i,end1-start1))
    start2=time.time()
    quicksort_mid(A)
    end2=time.time()
    time2.append(end2-start2)
    print('第{}次排序用时{:.3f}s'.format(i,end2-start2))
    start3=time.time()
    quicksort_random(A)
    end3=time.time()
    time3.append(end3-start3)
    print('第{}次排序用时{:.3f}s'.format(i,end3-start3))
    b=A.copy()
    start4=time.time()
    Quick_Sort(b,0,len(A)-1)
    end4=time.time()
    time4.append(end4-start4)
    print('第{}次排序用时{:.3f}s'.format(i,end4-start4))
    b=A.copy()
    start5=time.time()
    Quick_Sort_Random(b,0,len(A)-1)
    end5=time.time()
    time5.append(end5-start5)
    print('第{}次排序用时{:.3f}s'.format(i,end5-start5))
    
    
print('第1种快速排序平均用时：{:.8f}s'.format(sum(time1)/len(time1)))
print('第2种快速排序平均用时：{:.8f}s'.format(sum(time2)/len(time2)))
print('第3种快速排序平均用时：{:.8f}s'.format(sum(time3)/len(time3)))
print('第4种快速排序平均用时：{:.8f}s'.format(sum(time4)/len(time4)))
print('第5种快速排序平均用时：{:.8f}s'.format(sum(time5)/len(time5)))