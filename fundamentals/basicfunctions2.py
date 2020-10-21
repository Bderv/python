# 1. Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0(as the last element).
def nums(inp):
    lst = []
    for i in range (inp,0,-1):
        lst.append(i)
    return lst
print(nums(300)) 

# 2. Create a function that will receive a list with two numbers. Print the first value and return the second. 
def printreturn(inp):
    print(inp[0])
    return inp[1]
        
print(printreturn([6,4]))

# 3. Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def sum(inp):
    return (inp[0] + len(inp)) 
print(sum([4,2,6]))

# 4. Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how mnay values this is and then return the new list. If the list has less than 2 elements, have the function return False
def greater(inp):
    lst = []
    for i in range(0,len(inp),1):
        if inp[i] > inp[1]:
            # print(inp[i])
            lst.append(inp[i])
    print(len(lst))
    return lst
    

print(greater([4,3,5,2,6,8,1]))

# 5. Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def thisthat(size,value):
    lst = []
    for i in range(0, size, 1):
        lst.append(value)
    return lst

print(thisthat(8,6))