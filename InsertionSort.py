# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:39:03 2022

@author: Orbit sgl
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#arr = [12, 11, 13, 5, 6]
arr = []
check = "y"
while check == "y":
    value = int(input("Nilai yang dimasukkan ke array: "))
    arr.append(arr)
    print("array anda: ", arr)
    check = input("masukkan y untuk tambah data: ").lower()

insertionSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i])
