# Write a function that accepts two numbers a and b
# and returns whether a is smaller than, bigger than, or equal to b, as a string.
# (5, 4)   ---> "5 is greater than 4"
# (-4, -7) ---> "-4 is greater than -7"
# (2, 2)   ---> "2 is equal to 2"
# There is only one problem...
# You cannot use if statements, and you cannot us
# the ternary operator ? :.
# In fact the word if and the character ? are not
# allowed in your code.


def mathy(x, y):
    '''
    defined a func called mathy, 
    had while loop compare x and y
    had a nested while to see if they are ==
    else is had to be less than
    '''
    while x > y or x == y:
        while x == y:
            return(f'{x} is equal to {y}')
        return(f'{x} is greater than {y}')
    else:
        return(f'{x}, is less than {y}')


print(mathy(5, 10))


def compareTwo(a, b):
    dict = {a > b:" is greater than ", a < b: " is less than ", a == b: " is equal to "}
    while True in dict.keys():
        return f"{a}{dict[True]}{b}"




