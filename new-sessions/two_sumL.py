# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         user=int(input("Enter Number :"))
#         Check=int(input("Enter Second Number :"))
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#         # Return an empty list if no solution is found
#         return []


# solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))
# print(user)
# print(Check)
                
n = int(input("How many numbers: "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

target = int(input("What sum do you want: "))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print("Numbers:", numbers[i], "and", numbers[j])
            print("Sum:", target)
            print("Indexes:", i, j)
            break