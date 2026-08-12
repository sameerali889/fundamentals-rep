#For Loop:
# for item in sequence:
#     # Code block to execute
# item: A temporary variable that holds the current value during the current iteration.
# sequence: The iterable object you want to loop through.
# Indentation: Python uses 4 spaces of indentation to define the loop body.
# for i in range(0,5):
#     print("Hello World")

# import numbers
# numbers = [10, 20, 30]
# for i in range(len(numbers)):
#         print(i, numbers[i])

# for i in range(1,11):
#         print(i*3)

# for i in range(1,100):
#      if i % 7 == 0 and i % 3 ==0:
#          print(i)
# else:
#      pass
# Username = input("Enter your Name:-")
# for i in range(0,6):
#     print(Username[i])
        
# Username = input("Enter your Name: ") # altaf
# character = input("Enter a character: ") # index :f # 4

# for i in range(len(Username)):
#     if Username[i] == character:
#         print("Index:", i)

# a = ["geeks", "for", "geeks"]
# for idx in range(len(a)):
#     print(a[idx])
# for i in range(0,10,1):
#     print(i*5)

# numbers = [10, 25, 30, 45, 50]

# target = int(input("Enter a number: "))

# for i in range(len(numbers)):
#     if numbers[i] == target:
# #         print("Index:", i)

# word =input("enter your name:")
# character=input("Enter a Character :")
# count =0
# for i in range(len(word)):
#     if word[i]==character:
#         count+=1
#         print(character, "repeats", count, "times")
#         break

    # write a program to print fibanocci series upto user wants
# num1=0
# num2=1
# nums_of_nums=int(input("Enter The Number you want :"))
# print(num1)
# print(num2)
# for i in range(2,nums_of_nums):
#     new= num1 + num2
#     print(new)
# num1=num2
# num2=new

# for i in range(1, 100):
#     if i % 7 == 0 and i % 3 == 0:
#         print(i)
#     else:
#         pass
# for i in range(10, 0, -1):
#     print(i*5)


# # print bellow strings charecters in reverse order using for loop

# str1 = "ASDFG"   # 4, -1, -1
# print(len(str1))

# for i in range(len(str1)-1, -1, -1):
#     print(str1[i]) below is using list[]:
# def fibonacci_with_list(n):
#     fib_series = [0, 1]
#     for i in range(2, n):
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series

# # Example usage:
# n = 10
# result = fibonacci_with_list(n)
# print(f"Fibonacci series with {n} elements:", result)
# for i in range(2,n):
