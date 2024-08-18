from data_structures.list_adt import List
from data_structures.linked_list import LinkedList
from data_structures.array_sorted_list import ArraySortedList
from data_structures.referential_array import ArrayR

def AR(lst: List) -> ArrayR:
    res = ArrayR(len(lst))
    for i, num in enumerate(lst):
        res[i] = num
    return res

def ARtoList(ar: ArrayR):
    out = []
    for i in range(len(ar)):
        out.append(ar[i])
    return out

def LL(lst: List) -> LinkedList:
    res = LinkedList()
    for i, num in enumerate(lst):
        res.insert(i, num)
    return res

def LLtoList(ll: LinkedList):
    out = []
    for i in range(len(ll)):
        out.append(ll[i])
    return out

def SLtoList(sl: ArraySortedList):
    out = []
    for i in range(len(sl)):
        out.append(sl[i].value)
    return out