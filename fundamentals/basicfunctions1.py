# #1
def a():
    return 5
print(a())
# # my prediction for #1: it will return 5.


# #2
def a():
    return 5
print(a()+a())
# # my prediction for #2: it will return 10.


# #3
def a():
    return 5
    return 10
print(a())
# # my predcition for #3: it will return 5 then end the function.


# #4
def a():
    return 5
    print(10)
print(a())
# # my prediction for #4: it will return 5. It will not print 10 because it was after returning.


# #5
def a():
    print(5)
x = a()
print(x)
# # my prediction for #5: it will print 5 then nothing. 

# #6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# # my prediction for #6: it should print 3, 5, 8 all on seperate lines.
# # output was Different! : It showed 3, and 5 on seperate lines then read an error regarding line 41.


# #7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# # my prediction for #7: it will print 7,7 on seperate lines.
# # outcome: 25, which means the string added 2 to the end of 5 making it 25.

# #8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# # my prediction for #8: it will print 100 and return 7.
# # outcome: it did not print anything, had the error invalid character for else:


# #9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# # my prediction: it will return 7, then return 14 then return 21


# #10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# # my prediction: it will return 8 and end the function.


# #11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# # My prediction: it will print 500, 500, 500 all on seperate lines
# # outcome: it printed 500, 500, 300, 500. meaning it printed def a() as well.

# #12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# my prediction: it will print 500, 500, 300 then return 300 and then print 500


# #13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# # my prediction: it will print 500, 500, 300 then return 300


# #14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# my prediction: 1,2
# # output: 1,3,2 meaning i forgot to input def b() where b() is at line 129.


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# my prediction: 1,3,5,10

















