# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:41:19 2022

@author: Orbit sgl
"""
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr [j]
                swapped = True
        
        if swapped == False:
            break

arr = []
for num in range(5):
    number = int(input("Omagad :"))
    arr.append(number)
    
bubbleSort(arr)

print("Sorted Array :")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")