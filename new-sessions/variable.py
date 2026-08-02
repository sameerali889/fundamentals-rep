"""num1=10
print(num1)
fruiT="banana"
print(fruiT)"""

"""x= 10
y= 5    
z =x + y
print(x)
print(y)
print(z)"""

"""x=1.0
y=2.0
z="ali"
k="True"
print(x)
print(y)
print(z)
print(k)
print(type(x))
print(type(y))
print(type(z))
print(type(k))"""""

"""x =-0.9
print(x)
print(type(x))"""

"""type1 = True
print(type1)

Sameer_Male = "True"
print(Sameer_Male == "True")"""""

"""x = 5
y = 4
print(x + y == 9)
"""""

#str1= "Apple"
#print(str1)
#print(type(str1))
#print(len(str1)!=5)
#string manipulation functions

# upper() changes from lower case to upper case ex:
#tr1= "Apple"
#print(str1.upper())

# lower() changes from upper case to lower case ex:
#str1= "Kiwi"
#print(str1.lower())
#capitalize()
#str1 = "my dear friend"
#print(str1.capitalize())
"""str3 = "Danny is a good boy"
print(str3.capitalize())"""
# title() :first letter of each word will be capitalized
"""str1 = "my dear friend"
print(str1.title())
str2 = "Ashraf Ali My Boy"
print(str2.title())"""
# swapcase():changes upper case to lower case and lower case to upper case
"""str1 = "My dear friend"
print(str1.swapcase())
str2 = "Ashraf Ali My Boy"
print(str2.swapcase())"""""

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
"""str1 ="ABCDEF"
print(str1.find("C"))
print(str1.find("A"))
print(str1.find("D"))  
print(str1.find("Z"))"""  # returns -1 if the value is not found
#.rfind() : returns the index of the last occurrence of the specified value from the right side
#str1 ="ABCDEF"
#print(str1.rfind("C"))

"""x=10
y=x
x=20
print(y)
a=b=c=5
print(a,b,c)"""""
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
#str2 =" "
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
# List is a built-in data structure used to store an ordered collection of items. 
# They are dynamic, resizable and capable of storing multiple data types
#list (),list[]
# students = ["Ali", "Ahmed", "Ayesha", "Zara"]
# print(students)
# student =[23,45,67,89]
# print(student)
# students1=["Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89] list collection is ordered and changeable. Allows duplicate members.
# print(students1)
# students2 =("Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89) # Tuple collection is ordered and unchangeable. Allows duplicate members.
# print(students2)

# set collection is unordered and unindexed. No duplicate members.
set1 = {"Ali", 23, "Ahmed", 45, "Ayesha", 67, "Zara", 89}
print(set1)