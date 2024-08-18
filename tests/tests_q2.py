import unittest
from Q2 import kth_smallest
from ed_utils.decorators import number
from tests.conversions import AR, ARtoList

### copy you function bellow

class Test_Q2(unittest.TestCase):
    def assertResultEqual(self, expected, actual):
        if len(actual) < len(expected):
            self.fail('Length of output is too short')
        
        for i in range(len(expected)):
            if actual[i] != expected[i]:
                self.fail(f"Results did not match: {ARtoList(expected)}, {ARtoList(actual)}")

    @number("2.1")
    def test_examples(self):
        self.assertResultEqual(kth_smallest(AR([1, 8, 2, 0, 5, 4, 7]), AR([4, 2, 1, 7])), AR([4,1,0,8]))

    @number("2.2")
    def test_extra(self):
        self.assertResultEqual(kth_smallest(AR([17, 94, 65, 82, 10]), AR([3, 2, 1])), AR([65, 17, 10]))
        self.assertResultEqual(kth_smallest(AR([5, 12, 77, 3, 45, 22]), AR([6, 3, 1])), AR([77, 12, 3]))
        

if __name__ == '__main__':
    unittest.main()