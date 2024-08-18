""" Linked-node based implementation of List ADT. """
from data_structures.node import Node
from data_structures.abstract_list import List, T

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class LinkedList(List[T]):
    """ List ADT implemented with linked nodes. """
    def __init__(self, dummy_capacity=1) -> None:
        """ Linked-list object initialiser. """
        List.__init__(self) # Could use super(LinkedList, self).__init__() instead
        self.head = None

    def clear(self):
        """ Clear the list. """
        # first call clear() for the base class
        List.clear(self)
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item
        
    def __get_node_at_index(self, index: int) -> Node[T]:
        if 0 <= index and index < len(self):
            current = self.head
            for i in range(index):
                current = current.link
            return current
        else:
            raise ValueError('Index out of bounds')
 
    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        current = self.head
        index = 0
        while current is not None and current.item != item:
            current = current.link
            index += 1
        if current is None:
            raise ValueError('Item is not in list')
        else:
            return index

    def delete_at_index(self, index: int) -> T:
        if self.is_empty():
            raise ValueError("Cannot delete from empty list")
        
        if index > 0:
            previous_node = self.__get_node_at_index(index-1)
            item = previous_node.link.item
            previous_node.link = previous_node.link.link
        elif index == 0:
            item = self.head.item
            self.head = self.head.link
        else:
            raise IndexError("Index out of bounds")
        
        self.length -= 1
        return item
        

    def insert(self, index: int, item: T) -> None:
        if index > len(self):
            raise IndexError("Index out of bounds")
        
        new_node = Node(item)
        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            previous_node = self.__get_node_at_index(index-1)
            new_node.link = previous_node.link
            previous_node.link = new_node
        self.length += 1