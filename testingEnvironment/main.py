# BASICS
# variables in python do not need to be declared
integer = 1
"""
print("A" operation "B") can do math within the print perenthesis will change the order of stuff
% gives the remainder
pow, round, floor, ceil, sqrt in the "from math import *" library

"""
string = "God this is weird"
"""
string.lower() makes everything in the strong lowercase
string.upper() makes everything in uppercase
string[x] finds a character in the string
string.isupper/islower() is a boolean 
string.index(A) finds the locations of the character "A" in the string ***will cause an error if no character 
    or line of characters are found***
string.replace("God", "not god lol") replaces the word
"""
double = 1.078
# can assign multiple variables at once
a, b, c = 4, "x", 6
print(integer, ",", string)
print(b)
# f is used when you want python to fill in values within the print
print(f"the integer's value is {integer}")
# otherwise, gotta use this weird %(variable)s shit
print("the integer's value is %(number)s" % {"number": integer})

# LISTS AND ARRAYS

manta = ["List Spot" for i in range(100)] # creates a long 1D array of similar variables
print(manta) # for a long line of stuff
# 2D arrays are pretty easy to use...
twoDManta = [[1, 2, 3], [4, 'x', 6], [7, 8, 9]] # variables can be intertwined really easily
print(twoDManta)
print(twoDManta[1])
# creating a larger 2D array seems harder than Java...
largeArray = [[1 for i in range(5)] for i in range(50)]
print(largeArray)

# What are the limits of this variable interchange ability???
twoDManta[1][1] = 2 # turning a string to an integer
print(twoDManta[1]) # nope its alright\
twoDManta[1][1] = 'x'
# sum = integer + twoDManta[1][1] <-- here's a problem aha

# TUPLES
# Lists that cannot change (does not support item assignment)
coordinates = (1, 3)

# INPUT VALUES
"""name = input("Enter your name: ")
print(f"Hello {name}!")"""

# FLOW CONTROL STATEMENTS
# python has while, for, if, else, else if (elif), break, continue, pass
increasingList = list(range(10)) # creates a list from 0 to 9
print(increasingList)
for number in increasingList: # number is the spot within the list similar to for loops in java
    # (int number = 0; number < increasingList.length; number++)
    if number == 9:
        print("stop")
        break
    else:
        print("still going")
        continue
number = 0
while (number in increasingList):
    print(number)
    number += 1

# FUNCTIONS (METHODS)
def addition():
    print("The sum is " + str(twoDManta[0][1] + twoDManta[0][2]))

def multiplication(a, b):
    product = a * b
    return product

"""one = int(input("Number a: ")) # gotta make sure you define the input if you put words in it
two = int(input("Number b: "))
addition()
print(f"The product is {multiplication(one, two)}")"""

# TRY AND EXCEPT
try:
    number = int(input("enter a number"))
    print(number)
except: # catches anything that causes an error in the try:
    print("invalid input")
# errorTrap
def errorTrap(input):
    checker = bool(False)
    print("Enter a number")
    while (checker == False):
        try:
            input = int(input())
            checker = True
            return input
        except:
            print("Invalid input, please try again")

aNumber = errorTrap(input)

# READING FILES
Shakespeare = open("Shakespeare.txt", "r", errors = 'ignore') # r is read, w is write, a is append, r+ is read and write
checker = False
# print(Shakespeare.readlines())
for word in Shakespeare.readlines():
    print(word)
"""while (checker == False):
    try:
        print(Shakespeare.readline())
    except:
        print("Line cannot be read")
        checker = True"""
Shakespeare.close()

# WRITING FILES
