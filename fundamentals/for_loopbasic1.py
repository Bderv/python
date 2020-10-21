# 1. Print all intergers from 0 - 150.
for i in range(0,151,1):
    print (i)

# 2. Print all the multiples of 5 from 5 to 1,000.
for i in range(0,1000,5):
    print (i)

# 3. Print Integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(0,100,1):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
    print(i)

# 4. Add odd integers from 0 to 500,000 and print the final sum.
lst = []
for i in range(0,500000,1):
    if i % 2 != 0:
        lst.append(i)
print(sum(lst))

# 5. Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)

# 6. Set three variables: lowNum, highNum, mult. Starting at lowNum and groung through highNum, print only the integers that are a multiple of mult. For Example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9 on seperate lines.
lowNum = 4
highNum = 12
mult = 3
for i in range(lowNum,highNum,1):
    if i % mult == 0:
        print(i)