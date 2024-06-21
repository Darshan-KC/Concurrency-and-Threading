# Write a python program to implement multi-threaded merge sort algorithm
import threading

def merge_sort(arr) ->list:
    if len(arr) <=1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
    
def merge(left,right) ->list:
    merged_list = []
    
    return merged_list