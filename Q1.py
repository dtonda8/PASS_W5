from typing import TypeVar
from data_structures.linked_list import LinkedList
T = TypeVar("T")

def remove_second_half(ll: LinkedList[T]) -> LinkedList[T]:
    n = len(ll)
    goal_length = n // 2
    
    # If odd, increment goal length by 1
    if n % 2 == 1:
        goal_length += 1
        
    while len(ll) > goal_length:
        ll.delete_at_index(goal_length)
    return ll

if __name__ == "__main__": # for personal tests
	pass