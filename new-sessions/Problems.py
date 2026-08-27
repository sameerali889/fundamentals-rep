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
principal = 1000
rate = 5
time = 2

simple_interest = principal * rate * time / 100
print("Simple interest =", simple_interest)
