from data_structures.list_adt import List
from data_structures.referential_array import ArrayR
from data_structures.array_sorted_list import ArraySortedList

def kth_smallest(nums: ArrayR, queries: ArrayR) -> ArrayR:
    # add to sorted list
    sorted_lst = ArraySortedList(len(nums))
    for i in range(len(nums)):
        sorted_lst.add(nums[i])
        
    # answer to queries
    results = ArrayR(len(queries))
    for i in range(len(queries)):
        idx = queries[i] - 1
        results[i] = sorted_lst[idx]
    
    return results

if __name__ == "__main__": # for personal tests
	pass