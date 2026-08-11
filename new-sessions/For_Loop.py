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
#         print("Index:", i)

word =input("enter your name:")
character=input("Enter a Character :")
count =0
for i in range(len(word)):
    if word[i]==character:
        count+=1
        print(character, "appears", count, "times")
        break
    