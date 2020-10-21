# 1. Given a list, write a function that changes all positive numbers in the list to "big".
def biggie(somelist):
    for i in range(0,len(somelist), 1):
        if somelist[i]>0:
            somelist[i]="big"
    print(somelist)
# biggie([-1,2,3,4,-5,6,-2])

# 2. Given a list of numbers, create a function to replace the last value with the number of positive values.
x = [-1,2,3,4,-5,6,-2]
def positivo(somelist):
    postivetotal = 0
    for i in range(0, len(somelist), 1):
        if somelist[i] > 0:
            postivetotal += 1
    somelist[len(somelist)-1] = postivetotal
    print(somelist)

# positivo(x)

# 3. Create a function that takes a list and returns the sum of all the values in the list.
x = [1,2,3]
def sumreturn(somelist):
    return sum(somelist)
    
# print(sumreturn(x))

# or you can also

def sum_total(someList):
    total = 0
    for num in someList:
        #print(element)
        total += num
    return total
# print(sum_total(x))


# 4. Create a function that takes a list and returns the average of all the values.
x = [1,2,3]
def sumaverage(somelist):
    return sum(somelist) / len(somelist)

# print("Average =", sumaverage(x))

# 5. Create a function that takes a list and returns the length of the list.
x = [1,2,3]
def length(somelist):
    return len(somelist)

# print(length(x))

# 6. Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, the function return False.
x = [1,2,4,3,-2]
def findmin(somelist):
    for i in range(0, len(somelist), 1):
        min = somelist[0]
        if somelist[i] < min:
            min = somelist[i]
    return min

# print(findmin(x))

# 7. Create a function that takes a list and returns the maximum value in the list. 
x = [0,1,2,3,4]
def findmax(somelist):
    for i in range(0, len(somelist), 1):
        max = somelist[0]
        if somelist[i] > max:
            max = somelist[i]
    return max

# print(findmax(x))

# 8. Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
x = [1,2,4,6]
def everything(somelist):
    for i in range(0, len(somelist), 1):
        max = somelist[0]
        min = somelist[0]
        length = len(somelist)
        sumTotal = sum(somelist)
        average = sum(somelist) / len(somelist)
        if somelist[i] > max:
            max = somelist[i]
        if somelist[i] < min:
            min = somelist[i]
    return sumTotal, average, min, max, length

print(everything(x))

# 9. Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
x = [1,2,3,4]
def reversing(somelist):
    for i in range(0, int(len(somelist)/2),1):
        somelist[i], somelist[len(somelist)-1-i] = somelist[len(somelist)-1-i],somelist[i]
    return somelist

# print(reversing(x))


