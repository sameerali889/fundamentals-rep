# #Operators:
# ## Definition of Operators

# An operator is a symbol or keyword that tells the computer to perform a specific operation on one or more values.

# => In programming, operators work on operands (the values or variables).
# => Examples include:
#   `+` for addition
#   => `-` for subtraction
#   => `*` for multiplication
#   => `/` for division
#  => `==` for equality comparison
#   => `and`, `or`, `not` for logical operations

# ### In Python
# -> Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
# -> Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
# -> Logical operators: `and`, `or`, `not`
# -> Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`
# -> Membership operators: `in`, `not in`
# -> Identity operators: `is`, `is not`
# Ternary Operators s1 in s2 is,is not

# > Operators are the basic tools used to compute values, compare values, and control logic in code.
# Arithmetic operators:
x=5
y=6
# + : adds two values
# print(x+y)
# # - : subtracts one value from another
# print(x-y)
# # * : multiplies values
# print(x*y)
# # / : divides values with a float result
# print(x/y)
# # // : divides values and returns the integer portion
# print(x//y)
# # % : returns the remainder after division
# print(x%y)
# # ** : raises one value to the power of another
# print(x**y)
# Assignment operators
# = : stores a value in a variable
# print(x)
# print(y)
# # += : adds to a variable and stores the result
# x+=y
# print (x)
# print(y)
# # -= : subtracts from a variable and stores the result
# x-=y
# print(x)
# print(y)
# # *= : multiplies a variable and stores the result
# x*=y
# print(x)
# print(y)
# # /= : divides a variable and stores the result
# x/=y
# print(x)
# print(y)
# # //= : floor-divides a variable and stores the result
# x//=y
# print(x)
# print(y)
# # %= : computes remainder and stores the result
# x%=y
# print(x)
# print(y)
# # **= : raises a variable to a power and stores the result
# x**=y
# print(x)
# print(y)
# &=, |=, ^=, <<=, >>= : combine bitwise or shift operations with assignment

# --------------------------------------------------------------------------------
#Comparision Operator:
    # -> Equal to : ==
# print(x==y)
#     # -> Not equal to !=
# print(x!=y)
#     # -> greater than : >
# print(x>y)
#     # -> lesser than : <
# print(x<y)
#     # -> greater than or equal to: >=
# print(x>=y)
#     # -> lesser than or equal to <=
# print(x<=y)

# Identity operator:
# In Python, identity operators are used to compare whether two variables refer to the same object in memory, not just whether they have the same value.

# There are two identity operators:

# is – Returns True if both variables point to the same object.
# is not – Returns True if both variables point to different objects.


# is 
# is not
# from copy import deepcopy
# x=[1,2,3,4,5]
# y =x
# # y=deepcopy(x)
# #print( x is y) # is True

# # x is not y
# print( x is not y)

#  5: Membership operators are used to check whether a particular value exists inside a collection such as a string, list, tuple, set, or dictionary.

# Python has 2 membership operators:

# Operator	Meaning
# in	Checks if a value exists
# not in	Checks if a value does not exist
# s1 = {4, 7, 1, 'H', 0}
# # 1: in
# # print(True in s1)
# # print(8 in s1)
# # 2 not in
# print(False not in s1)
# print(12 not in s1)

# 6: Logical Operator:
# x =5
# y=12
# z =4

# # 1:and
# # print(z>x and z>y)
# # print(y>x and y>z)
# # print(z<x and z<y)

# # 2: or: either of the option should be true
# # print(z >y and z <x)
# # print(z >x and z >y)
# # print(z <x and z <y)
# # 3: not:
# print(not(x>y) and (y> z) or (z>x)) 
# Ternary operator: if logic is simple and very conditions then use:
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
