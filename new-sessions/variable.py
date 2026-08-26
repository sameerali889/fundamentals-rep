# num1=10
# print(num1)
# fruiT="banana"
# print(fruiT)

# x= 10
# y= 5    
# z =x + y
# print(x)
# print(y)
# print(z)



# x=1.0
# y=2.0
# z="ali"
# k="True"
# print(x)
# print(y)
# print(z)
# print(k)
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(k))

# x =-0.9
# print(x)
# print(type(x))


# Bool: a data type of two values True and False

# type1 = True
# print(type(type1)) #<class 'bool'>

# Sameer_Male = "True"
# print(Sameer_Male == "True")


# x = 5
# y = 4
# print(x + y == 9)


# str1= "Apple"
# print(str1)
# print(type(str1))
# print(len(str1)!=5)
#Strings: it is a seq of characters :alphabets,numbers,special characters and emojis
# These are 4 ways of writing strings in Python, but they are mainly two styles of quotation marks:

# 1.Single quotes → ' '
# 2.Double quotes → " "
# 3.Triple single quotes → ''' '''
# 4.Triple double quotes → """ """
#string manipulation functions
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# s1 = 'asdfghjk' 
# print(s1)
# s2 = 'SDFGHJK'
# print(s2)
# s3 = 'DFGHfghj'
# print(s3)
# s4 = "I'm your buddy"
# print(s4)
# s5 = '1234567'
# print(s5)
# s6 = '@#$%^&*()'
# print(s6)
# s7 = "Ali@#$1234"
# print(s7)
# s8 = '🔥'
# print(s8)
# s9 = '🔥gdiuwd3567$%^&FGH'
# print(s9)
# String Indexing :
# str2= "APPLE"
# print(str2[-2])
# print(str2[0])
# print(str2[3])
# Indexing:
# Character:   P    y    t    h    o    n
# Positive:    0    1    2    3    4    5
# Negative:   -6   -5   -4   -3   -2   -1
 # "Slicing" : string[start:end]
#  Start is included, end is excluded, step tells Python how to move.
# str2="India My Country"
# # print(str2[0])
# # print(str2[-5])
# print(str2[1:2:1]) #slicing
# print(str2[-2])

# str3="1234567890"
# #123
# # print(str3[0:3:1])
# # # print(str3[-3::1])
# # print(str3[3:8:1])
# print (str3[3::-1])
# print(str3[-1::-1]) # 0987654321
# print(str3[0:10:3]) # 1470
# 0864 printing :1 skipping :1 yaad rakh
# print(str3[-1:-8:-2])
#String Manipulation Functions:
# 1.upper()
# 2.lower()
# 3.capitialize()
# 4.title()
# 5.swapcase()
# upper() changes from lower case to upper case ex:
#str1= "Apple"
#print(str1.upper())

# lower() changes from upper case to lower case ex:
#str1= "Kiwi"
#print(str1.lower())
#capitalize()
#str1 = "my dear friend"
#print(str1.capitalize())
str3 = "Danny is a good boy"
print(str3.capitalize())
# title() :first letter of each word will be capitalized
str1 = "my dear friend"
print(str3.title())
str2 = "Ashraf Ali My Boy"
print(str2.title())
# swapcase():changes upper case to lower case and lower case to upper case
# str1 = "My dear friend"
# print(str1.swapcase())
# str2 = "Ashraf Ali My Boy"
# print(str2.swapcase())

#index() : returns the index of the first occurrence of the specified value
#str1 ="ABCDEFGHIJKLMN"
#print(str1.index("C"))
#print(str1.index("A"))
#print(str1.index("D"))

#rindex() : returns the index of the last occurrence of the specified value from the right side
#str1 ="ABCDEFGHIJKLMN"
#print(str1.rindex("C"))
#str2 ="Ashraf Ali My Boy"
#print(str2.rindex("A"))
#string.rindex(value, start, end)
#text = "apple banana apple"
#print(text.rindex("apple"))
#str11 = "ABCBCA"
#print(str11.index("BC"))
#print(str11.rindex("BC"))

#.find() : returns the index of the first occurrence of the specified value
# str1 ="ABCDEF"
# print(str1.find("C"))
# print(str1.find("A"))
# print(str1.find("D"))  
# print(str1.find("Z"))  # returns -1 if the value is not found
#.rfind() : returns the index of the last occurrence of the specified value from the right side
#str1 ="ABCDEF"
#print(str1.rfind("C"))

# x=10
# y=x
# x=20
# print(y)
# a=b=c=5
# print(a,b,c)
#-----------------------
# is methods
# isalpha() : returns True if all characters in the string are alphabetic
#str1 = "1234"
#print(str1.isalpha())
# isdigit() : returns True if all characters in the string are digits
#str2 = "1234"
#print(str2.isdigit())
# isalnum() : returns True if all characters in the string are alphanumeric (letters or digits)
#str3 = "1234"
#print(str3.isalnum())
# is space() : returns True if all characters in the string are whitespace
#str4 = "1234"
#print(str4.isspace())

#str1 = "asdfghjk"
#print(str1.isalpha())
#str1="apple123"
# str2 =split(s2)
# print(dir(str))
#str3 ="@#$%"
#str4 = "Apple@123"
#print(str2.isalpha()) 
#print(str2.isdigit())
#print(str2.isalnum())
#print(str2.isspace())
#print(str3.isalpha())
#print(str3.isdigit())
#print(str3.isalnum())
#print(str3.isspace())
#print(str4.isalpha())
#print(str4.isdigit())
#print(str4.isalnum())
#print(str4.isspace())
#-----------------------
# List is a built-in data structure used to store an ordered collection of items. 
# They are dynamic, resizable and capable of storing multiple data types
#list (),list[] mutable, ordered, allows duplicate members
# students = ["Ali", "Ahmed", "Ayesha", "Zara"]
# print(students)
# student =[23,45,67,89]
# print(student)
# students1=["Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89] list collection is ordered and changeable. Allows duplicate members.
# print(students1)
# students2 =("Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89) # Tuple collection is ordered and unchangeable. Allows duplicate members.
# print(students2)
# list is heterogeneous collection of items. It can store different data types in a single list.
# set collection is unordered and unindexed. No duplicate members.
# set1 = {"Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89}
# print(set1)

# l1 =[]
# print(l1)
# print(type(l1)) #<class 'list'>

# l2 = list()
# print(l2)
# print(type(l2)) #<class 'list'>

# l3 = [1, 2, 3, 4, 5]
# print(l3)
# print(type(l3))

# l4 =list({1,2,3,4,5})
# print(l4)
# print(type(l4))    
# l5 = [1.1,2.2,3.06,-0.45,12]
# print(l5)
# print(type(l5))
# number = [1,2,3,4,5,6,7,8,9,10]
# print(number)
# print(type(number))
        # 0      1         2          3
# list1 = ["Ali", "Ahmed", "Ayesha", "Zara"]
# print(list1[0]) # Ali
# print(list1[1]) # Ahmed. indexing hogaya
# print(list1[3])
# print(list1[-1]) # Zara negartive indxing right to left hogaya
# print(list1[-2]) # Ayesha
# print(list1[-4]) # Ali
# print(list1[0:3:1]) #slicing 0 to 3 index tak print hoga step size 1 hoga
# print(list1[0:4:2]) # step size 2 hoga 0
# print(list1[0::3])

# ad elements to a list using append() method 
# append() method adds an element to the end of the list. It takes a single argument, which is the element to be added.
# list2 =[1,2,3,4,5,6]
# list2.append(7)
# print(list2) # [1, 2, 3, 4, 5, 6, 7]
# extend() method adds multiple elements to the end of the list. It takes an iterable (like a list, tuple, or set) as an argument and adds each element of the iterable to the end of the list.
# list3 =[1,2,3,4,5]
# # list3.extend([6,7,8])
# print(list3) # [1, 2, 3, 4, 5, 6, 7, 8]
# # list3.extend([9,10])
# print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # list3.extend({11,12,14})
# print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
# print(type(list3)) # <class 'list'>
# # insert() method adds an element at a specific index in the list. It takes two arguments
# list3.insert(0,0)
# list3.insert(5,100)
# print(list3) # [0, 1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10, 11, 12, 14]
# list3.insert(-1,200)
# print(list3) # [0, 1, 2, 3, 4 
# -----------------------------------
# removing elements from a list using remove() method
# remove() method removes the first occurrence of a specified value from the list. It takes a single argument, which is the value to be removed. If the value is not found in the list, it raises a ValueError.
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list4.remove(5)
# print(list4) # [1, 2, 3, 4, 6   
#    pop() method removes an element at a specific index from the list and returns the removed element. It takes a single argument, which is the index of the element to be removed. If no index is specified, it removes and returns the last element of the list.
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2.pop(4)
# print(list2) 
# list2.pop(5)
# print(list2)

# # remove() method removes the first occurrence of a specified value from the list. It takes a single argument, which is the value to be removed. If the value is not found in the list, it raises a ValueError.
# # list2.remove(3)
# # print(list2)
# # list2.remove(7)
# # print(list2)
# #clear() method removes all elements from the list, leaving it empty. It does not take any arguments and does not return any value.
# list2.clear()
# print(list2) # []
# search methods 
# .index() method returns the index of the first occurrence of a specified value in the list. It takes a single argument, which is the value to be searched for. If the value is not found in the list, it raises a ValueError.
# print(list2.index(3)) # 2
# print(list2.index(7))
# l1 =[10,32,45,67,89,100]
# l2 =l1.copy()
# print(l1)
# print(l2) # [10, 32, 45, 67, 89, 100]
# print(id(l1))
# print(id(l2))
# l2[0] = 1000
# print(l1) # [10, 32, 45, 67, 89
# print(l2) # [1000, 32, 45, 67, 89, 100]
# l1 = [10,32,45,67,89,100]
# l2 = l1.copy()
# print(l1,id(l1))
# print(l2,id(l2)) # [10, 32, 45, 67, 89
# l3 = l1
# print(l1,id(l1))
# print(l3,id(l3)) # [10, 32, 45, 67, 89, 100]
# l3[0] = 1000
# print(l1) # [1000, 32, 45, 67, 89, 100]
# print(l3) # [1000, 32, 45, 67, 89, 100]

# l1 =[10,23,34,[1,2,3]]
# l2 =l1
# print(l1,id(l1))
# print(l2,id(l2))
# --------------------------
# Range: range is a datatype which generateas seq of numbers and that seq is generatred on fly
# range is immutable datatype which means we cannot change the values of range once it is created
# range is memory efficient (friendly) datatype which means it does not store all the values in memory at once, it generates the values on fly when we iterate over it
# how to create a range:
# range(start, end, step)
# r1 =set(range(1, 11)) # start=1, end=11, step=1
# print(r1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r2 =set(range(1, 11, 2)) # start=1
        # ------------------------------

# nums = [1, 2, 3, 4, 5]
# def two_sum(nums):
#         for i in range(len(nums)):
#                 for j in range(i + 1, len(nums)):
#                         if nums[i] + nums[j] == 6:
#                                 return [i, j]


# print(two_sum(nums))

# 1.Create variables to store your name, age, height, and whether you are a student. Print them.  
# name=input("enter your name:")
# age=int(input("enter age:"))
# Height=float(input("enter your height:"))  
# student_answer = input("Are you a student? (yes/no): ")
# is_student = student_answer.lower() == "yes"
# print(name)
# print(age)
# print(Height)
# print(is_student)

# 2.Create two variables a and b and swap their values without using a third variable.
# a = 10
# b = 20

# a, b = b, a

# print("a =", a)
# print("b =", b)
#3.Take the user's name and age as input and print:
# -My name is Rahul and I am 25 years old.
# User=input("Enter name:")
# age=int(input("Enter age:"))
# print(f"My name is {User} and I am {age} years old.")

# 4.- Store a person's first name and last name in two variables and create their full name.
# f → formatted string , {} → put the variable's value here
# First_Name ="Sameer Ali"   
# Last_Name  = " Mohammed"
# print(First_Name+Last_Name)

# Take two numbers from the user and print their sum.
# Num1 = int(input("Enter the first number: "))
# Num2 = int(input("Enter the second number: "))
# print("Sum =", Num1 + Num2)

