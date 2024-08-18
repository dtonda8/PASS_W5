import unittest
from Q1 import remove_second_half 
from ed_utils.decorators import number
from data_structures.linked_list import LinkedList
from tests.conversions import LLtoList, LL


class Test_Q1(unittest.TestCase):
    def assertResultEqual(self, expected: LinkedList, actual: LinkedList):
        if len(actual) < len(expected):
            self.fail('Length of output is too short')
        
        for i in range(len(expected)):
            if actual[i] != expected[i]:
                self.fail(f"Results did not match: {LLtoList(expected)}, {LLtoList(actual)}")
            
    @number("1.1")
    def test_examples(self):
        self.assertResultEqual(remove_second_half(LL([1,0,0,8,1,0,5,4,2,0,8,5])), LL([1,0,0,8,1,0]))
        
    @number("1.2")
    def test_extra(self):
        self.assertResultEqual(remove_second_half(LL([1,1,0,8,2,0,8,5])), LL([1,1,0,8]))
        self.assertResultEqual(remove_second_half(LL([1,-1,2])), LL([1,-1]))
        self.assertResultEqual(remove_second_half(LL([1,-1])), LL([1]))

if __name__ == '__main__':
    unittest.main()