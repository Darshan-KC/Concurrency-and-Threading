# Write a python program to implement multi-threaded merge sort algorithm
import threading

def merge_sort(arr) ->list[int]:
    if len(arr) <=1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
    
def merge(left,right) ->list[int]:
    merged_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i +=1
        else:
            merged_list.append(right[j])
            j += 1
    while i < len(left):
        merged_list.append(left[i])
        i += 1
    
    while j < len(right):
        merged_list.append(right[j])
        j += 1
    
    return merged_list

def main() -> None:
    input_list = [ 4,5,8,3,0,5,3,9,4,3]
    # num_threads = 2
    print("Original List:", input_list )
    # sorted_list = multi_threaded_merge_sort(input_list, num_threads)
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()