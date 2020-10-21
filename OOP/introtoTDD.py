# ASSIGNMENT: INTRO TO TDD

# 1. reverseList - Write a function that reverses the values in the list.
def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i],list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list
# Add atleast 3 test cases
class reverseArrayTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([5,1,2,3]), [3,2,1,5])
    def testThree(self):
        self.assertEqual(reverseArray([6,4,3,7,2]), [2,7,3,4,6])

# 2. isPalindrome - Write a function that checks whther the given word is a palindrome (a word that spells the same backwards)
def reverseString(stringInput): 
    newstr = ""
    for i in range(len(stringInput)-1, -1, -1):
        newstr += stringInput[i]
    return newstr
# code for the reverse function above and comparing function below
def isPalindrome(stringInput):
    if stringInput != reverseString(stringInput):
        return False
    else:
        return True
# add 5 test cases
class isPalidromeTests(unittest.Testcase):
    def testOne(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testTwo(self):
        self.assertTrue(isPalindrome("racecar"), True)
    def testThree(self):
        self.assertFalse(isPalindrome("tarzan"), False)
    def testThree(self):
        self.assertFalse(isPalindrome("popsicle"), False)
    def testThree(self):
        self.assertEqual(isPalindrome("pop"), True)


# 3. coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.

