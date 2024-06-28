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

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        # Create threads for the two halves
        left_thread = threading.Thread(target=quicksort, args=(arr, low, pi - 1))
        right_thread = threading.Thread(target=quicksort, args=(arr, pi + 1, high))
        
        # Start the threads
        left_thread.start()
        right_thread.start()
        
        # Wait for both threads to complete
        left_thread.join()
        right_thread.join()
        
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Unsorted array:", arr)
    quicksort(arr, 0, n - 1)
    print("Sorted array:", arr)