import unittest

# 1. reverseList - Write a function that reverses the values in the list (without creating a temporary array).
def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i],list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list


class reverseArrayTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([5,1,2,3]), [3,2,1,5])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main()