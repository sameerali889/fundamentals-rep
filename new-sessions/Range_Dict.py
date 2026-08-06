#Range:It is a data type which generates a sequence of numbers
# it is generated on fly i.e stores only temporarily
#immutable,memory friendly

# r1 = range[5]
# print(r1)
# print(type(r1)) # <class 'range'>

# r2 =(50,100) #start =50 end =100 step =1
# print(r2)
# print(type(r2))

# r3 =range(20,50,2)
# print(r3)
# print(type(r3)) #<class 'range'>

# r4=set(range(0,10))
# print(r4)
# print(type(r4)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} Set

r5=list(range(50,100,4))
print(r5)
print(type(r5))
# Range Completed