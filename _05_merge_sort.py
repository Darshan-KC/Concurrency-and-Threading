# Write a python program to implement multi-threaded merge sort algorithm
import threading

def merge_sort(arr :list[int]) ->list[int]:
    """
    Sorts an array of integers using the merge sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.
    """
    if len(arr) <=1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
    
def merge(left :list[int],right :list[int]) ->list[int]:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (List[int]): The sorted left half list.
        right (List[int]): The sorted right half list.

    Returns:
        List[int]: The merged and sorted list.
    """
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

def threaded_sort(sublist,sorted_sublists, lock):
    sorted_sublist = merge_sort(sublist)
    with lock:
        sorted_sublists.append(sorted_sublist)

def multi_threaded_merge_sort(arr, num_threads):
    if num_threads <= 1:
        return merge_sort(arr)
    # Divide the input list into equal-sized sublists
    size = len(arr) // num_threads
    
    sublists = [arr[i:size+1] for i in range(0,len(arr),size)]
    
    # if((len(arr)%num_threads) != 0):
    #     sublists[-1].extend(arr[num_threads*size:])
    remaining = len(arr) % num_threads
    if remaining != 0:
        sublists[-1].extend(arr[-remaining:])
        
    sorted_sublists = []
    lock = threading.Lock()
    threads = []

    for sublist in sublists:
        thread = threading.Thread(target=threaded_sort, args=(sublist, sorted_sublists, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    while len(sorted_sublists) > 1:
        left = sorted_sublists.pop(0)
        right = sorted_sublists.pop(0)
        merged = merge(left, right)
        sorted_sublists.append(merged)

    return sorted_sublists[0]

def main() -> None:
    """
    Main function to execute merge sort on a sample list and print the results.
    """
    
    input_list = [ 4,5,8,3,0,5,3,9,4,3]
    num_threads = 2
    print("Original List:", input_list )
    sorted_list = multi_threaded_merge_sort(input_list, num_threads)
    # sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)
    
    # Print the docstring of the functions
    # print(merge_sort.__doc__)
    # print(merge.__doc__)
    # print(main.__doc__)

if __name__ == "__main__":
    main()