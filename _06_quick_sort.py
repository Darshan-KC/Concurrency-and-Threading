# Write a Python program to implement a multi-threaded quicksort algorithm.

import threading

def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]
  
    for j in range(low, high):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
  
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1