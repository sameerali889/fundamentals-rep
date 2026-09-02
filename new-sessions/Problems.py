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

# 2.Create two variables a and b and swap their values without using a third variable. copied
# a = 10
# b = 20

# a, b = b, a

# print("a =", a)
# print("b =", b)

#3.Take the user's name and age as input and print: copied
# -My name is Rahul and I am 25 years old.
# User=input("Enter name:")
# age=int(input("Enter age:"))
# print(f"My name is {User} and I am {age} years old.")

# 4.- Store a person's first name and last name in two variables and create their full name.
# f → formatted string , {} → put the variable's value here
# First_Name ="Sameer Ali"   
# Last_Name  = " Mohammed"
# print(First_Name+Last_Name)

# Take two numbers from the user and print their sum.copied
# Num1 = int(input("Enter the first number: "))
# Num2 = int(input("Enter the second number: "))
# print("Sum =", Num1 + Num2)

# Create variables of type int, float, str, bool, list, tuple, set, and dict. Print their types.
# int_var1 = 10 
# print(type(int_var1))  #<class 'int'>
# float_var2 =2.0
# print(type(float_var2)) # <class:float>
# str_var3 ="Hello"
# print(type(str_var3)) #<>
# bool_var4 =True
# print(type(type(bool_var4))) # <>
# list_var5 =[1,2,3,4,5,"Hello",True]
# print(type(list_var5)) # <>
# tuple_var6 = (1,2,3,4,5,"Hello",True)
# print(type(tuple_var6))  # <>
# set_var7 ={1,2,3,4,5,"ahhh",True}
# print(type(set_var7)) # <>
# dict_var8={"name": "Sameer", "age": 20, "student": True} # Key:value pair
# print(type(dict_var8)) # <>

# Take a number as input and convert it into int, float, and str. copied
# number_input = input("Enter a number: ")
# number_int = int(number_input)
# number_float = float(number_input)
# number_str = str(number_input)

# print(number_int, type(number_int))
# print(number_float, type(number_float))
# print(number_str, type(number_str))
# Calculate the area of a rectangle using length and width variables.
# length = 10
# width = 5
# area = length * width
# print("Area of the rectangle =", area)
# principal = 1000
# rate = 5
# time = 2

# simple_interest = principal * rate * time / 100
# print("Simple interest =", simple_interest)

# Convert temperature from Celsius to Fahrenheit.
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius * 9 / 5 + 32
# print("Temperature in Fahrenheit =", fahrenheit)

# # Take two numbers and demonstrate +, -, *, /, //, %, and **.
# Num1=20
# Num2=30
# Num3=Num1+Num2
# print(Num3)
# Num4=Num1-Num2
# print(Num4)
# Num5=Num1 * Num2
# print(Num5)
# Num6=Num1/Num2
# print(Num6)
# Num7=Num1//Num2
# Num8=Num1%Num2
# Num9=Num1**Num2
# print(Num7)
# print(Num7)
# print(Num8)

# Find the remainder when one number is divided by another.
# dividend = int(input("Enter the first number: "))
# divisor = int(input("Enter the second number: "))
# remainder = dividend % divisor
# print("Remainder =", remainder)
# Check even %
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# if num %2==0:
#     print("Even")
# else:
#     print("ODD")

# Calculate the total bill including 18% GST.
# bill=float(input("Enter number:"))
# gst=bill*18/100
# total=bill*gst
# print("GST:",gst)
# print("TOTAL:",total)

# n1=float(input("enter number:"))
# n2=float(input("enter number:"))
# n3=float(input("enter number:"))
# n4=float(input("enter number:"))
# n5=float(input("enter number:"))
# total = n1 + n2 + n3 + n4 + n5
# percentage = total / 5

# print("Total:", total)
# print("Percentage:", percentage)

# x=5
# y=5
# if x==y:
#     print("Equal")
# else:
#     print("Not Equal;")

    #Take a number and check whether it is positive, negative, or zero.
# num=50
# if num>0:
#         print("pos")
# elif num <0:
#         print("neg")
# else:
#         print("zero")

# - [ ] Check whether a number is between 10 and 50.

# a=24
# if 10 <= a <= 50:
#     print("Between 10 and 50")
# else:
#     print("Not between 10 and 50")

# [ ] Check whether a person is eligible to vote using comparison and logical operators.

# age = int(input("Enter age:"))
# is_citizen = True
# if age >= 18 and is_citizen:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
# Given x = 10, predict the output:print(x > 5 and x < 20)

# x=10
# if x >5 and x < 20:
#     print("Greater True")
# else:
#     print("Not Greater False ")
    
# print(x < 5 or x == 10)

# x = int(input("Enter Number:"))

# print(x < 5 or x == 10)

# x = 15
# print(not (x == 10))

# x =int(input("Enter Number:"))
# if x % 3 == 0 and x % 5 == 0:
#     print("Divisible by 3 and 5")
# else:
#     print("Not divisible by 3 and 5")
#Check whether a number is positive.
# num3=20
# if num3>0:
#     print("Posiive")
# else:
#     print("Neg")

#Check whether a number is positive, negative, or zero.
# num3=20
# if num3>0:
#     print("Positive")
# elif num3<0:
#     print("Negative")
# else:
#     print("Zero")

# n=int(input("Enter Number:"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# age=int(input("Enter age:"))
# if age>=18:
#     print("Eligible")
# elif age<18:
#     print("Not Eligible")
# else:
#     print("Exactly 18 - Eligible")

# Check whether a student has passed or failed.
# student=int(input("Enter Marks:"))
# if student >=25:
#     print("Pass")
# elif student<25:
#     print("Fail")
# else:
#     print("Nothing")
#Check whether a number is divisible by 5.
# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")

# Check whether a given character is a vowel or consonant.
# char = input("Enter a character: ").lower()

# if len(char) == 1 and char.isalpha():
#     vowels = "aeiou"
#     if char in vowels:
#         print(f"'{char}' is a Vowel")
#     else:
#         print(f"'{char}' is a Consonant")
# else:
#     print("Please enter a single alphabetic character")
# Create a grading system:
#     * 90 or above: A
#     * 75–89: B
#     * 60–74: C
#     * 40–59: D
#     * Below 40: Fail
# grade = input("Enter your grade (A/B/C/D/F): ").upper()

# match grade:
#     case 'A':
#         print("Excellent! 90-100%")
#     case 'B':
#         print("Good! 80-89%")
#     case 'C':
#         print("Average! 70-79%")
#     case 'D':
#         print("Below Average! 60-69%")
#     case 'F':
#         print("Failed! Below 60%")
#     case _:
#         print("Invalid grade")


# Classify a person's age:
#     * 0–12: Child
#     * 13–19: Teenager
#     * 20–59: Adult
#     * 60 or above: Senior Citizen

# age = int(input("Enter your age: "))
# match True:
#     case _ if 0 <= age <= 12:
#         print("Child (0-12 years)")
#     case _ if 13 <= age <= 19:
#         print("Teenager (13-19 years)")
#     case _ if 20 <= age <= 59:
#         print("Adult (20-59 years)")
#     case _ if age >= 60:
#         print("Senior Citizen (60+ years)")
#     case _:
#         print("Invalid age")
# Find the largest of three numbers.
a = 18
b = 79
c = 4

# if a > b and a > c:
#     print(f"Largest number is {a}")
# elif b > a and b > c:
#     print(f"Largest number is {b}")
# else:
#     print(f"Largest number is {c}")
    
# Alternative using max() function:
# print(f"Largest number is {max(a, b, c)}")

# Find the smallest of three numbers.

# print("\n--- Finding Smallest Number ---")
# if a < b and a < c:
#     print(f"Smallest number is {a}")
# elif b < a and b < c:
#     print(f"Smallest number is {b}")
# else:
#     print(f"Smallest number is {c}")

# # Alternative using min() function:
# # print(f"Smallest number is {min(a, b, c)}")
# - [ ] Create a simple calculator that supports +, -, *, and /.

# Simple calculator
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Choose an operator (+, -, *, /): ")

# if operator == '+':
#     result = num1 + num2
#     print("Result:", result)
# elif operator == '-':
#     result = num1 - num2
#     print("Result:", result)
# elif operator == '*':
#     result = num1 * num2
#     print("Result:", result)
# elif operator == '/':
#     if num2 == 0:
#         print("Error: Cannot divide by zero.")
#     else:
#         result = num1 / num2
#         print("Result:", result)
# else:
#     print("Invalid operator. Please choose +, -, *, or /.")

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False


# for year in range(2020, 2040):
#     if is_leap_year(year):
#         print(year, "- Leap year")
#     else:
#         print(year, "- Not a leap year")



def can_form_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    if (
        side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1
    ):
        return True
    else:
        return False


a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if can_form_triangle(a, b, c):
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")

def calculate_final_bill(bill_amount):
    if bill_amount < 0:
        return None

    if bill_amount >= 200:
        discount_rate = 0.15
    elif bill_amount >= 100:
        discount_rate = 0.10
    elif bill_amount >= 50:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount_amount = bill_amount * discount_rate
    final_amount = bill_amount - discount_amount

    return discount_rate, discount_amount, final_amount


bill = float(input("Enter the bill amount: $"))

result = calculate_final_bill(bill)

if result is None:
    print("Bill amount cannot be negative.")
else:
    rate, discount, final_bill = result

    print(f"Original bill: ${bill:.2f}")
    print(f"Discount rate: {rate * 100:.0f}%")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Final bill: ${final_bill:.2f}")