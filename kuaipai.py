#coding:utf-8
import re
import time
import random



listid = []	
	
for id in resultall:
    listid.append(id[0])
	
n = len(listid)

'''
#冒泡排序
for i in range(n):
    for j in range(n-i-1):
        if listid[j]>listid[j+1]:
            listid[j], listid[j + 1] = listid[j + 1], listid[j]
'''

def quick_sort(base):
    if len(base)<2:
        return base

    i = 0
    j = len(base)-1
    flag = base[0]
	
    #print(flag)

    while not(i==j):
        while not(i==j):
            if base[j]<flag:
                base[j],base[i] = base[i],base[j]
                i+=1
                #print(i,j)
                break
            else:
                j-=1
        
        while not(i==j):
            if base[i]>flag:
                base[i],base[j] = base[j],base[i]
                j-=1
                #print(i,j)
                break
            else:
                i+=1
    return quick_sort(base[:i]) + [base[i]] + quick_sort(base[i+1:])				

listid = quick_sort(listid)




