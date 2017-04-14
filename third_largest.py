# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

def third_largest(nums):
    x = 0
    largest = 0
    while x < len(nums):
        if nums[x] > largest:
            largest = nums[x]
        x+=1
    second_largest = 0 
    y = 0
    while y < len(nums):
        if nums[y] > second_largest and nums[y] < largest:
            second_largest = nums[y]
        y+=1
    third_largest = 0
    z = 0
    while z < len(nums):
        if nums[z] > third_lagest and nums[z] < secod_largest:
            third_largest = nums[z]
        z+=1
    return third_largest

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print(third_largest([5, 3, 7])== 3)
print(third_largest([5, 3, 7, 4]) == 4)
print(third_largest([2, 3, 7, 4]) == 3)
