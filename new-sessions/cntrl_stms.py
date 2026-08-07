# Cntrl_strms:
# To perform operations or set of operations on multiple element /objects (Collection)
# Types of loop
# while loop:
# It is manual,it gives more control
# for loop:
# It is automatic
# It doesn't give access (Control)
#--------------------------- while Loop------

# count =0
# while count < 51:
#     print("Hello world",count)

# count = count +1

#  using while loop print table of 2
# count =1
# while count < 11:
#     print(count *2)
#     count =count +1
# to print all even numbers from 1 to 50

# count =1

# while count < 51:
#     if count % 2 == 0:
#         print(count)
#     else:
#         pass


#     count+=1

# count =1
# while count <51:
#     if count % 2 !=0:
#         print(Count)
#     else:
#         pass
#     count+=1
# print(14%2)
# print(7%4)

# write a program to print all those numbers that are divisble by 3 and 5 as well in between 50 and 100

# count =50
# while count <101:
#     if count %3  and count %5 ==0:
#         print(count)
#     else:
#         pass
#     count+=1

flag =True
while flag:
    num =input("Enter Number:") 
    if num =="Stop":
        break
    elif int (num) % 3 == 0 and  int(num) %5 == 0:
         print("divisble")
    elif int(num)%3 !=0 and int(num) %5 ==0:

      pass




