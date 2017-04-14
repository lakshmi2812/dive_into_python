# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.

def sum_of_two(nums):
    sum_zero = 'nil'
    for i in nums:
        idx = nums.index(i)
        idx2 = idx+1
        while idx2 < len(nums):
            if i+nums[idx2] == 0:
                sum_zero = [idx, idx2]
                break
            idx2+=1
    #print(sum_zero)
    return sum_zero
                
    
# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if '__main__' == __name__:
    print(sum_of_two([1, 3, 5, -3]) == [1, 3])
    print(sum_of_two([1, 3, 5]) == 'nil')
        
        
    