# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

def greatest_common_factor(num1, num2):
    factor_list1 = list_of_factors(num1)
    #print(factor_list1)
    factor_list2 = list_of_factors(num2)
    #print(factor_list2)
    common_factor = []
    for f in factor_list1:
        if f in factor_list2:
            common_factor.append(f)
    gcf = 0
    for i in common_factor:
        if i > gcf:
            gcf = i
    #print(gcf)
    return gcf

def list_of_factors(num):
    x = 1
    factor_list = []
    while x <= num:
        if num % x == 0:
            factor_list.append(x)
        x+=1
    return factor_list
            
        
# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print(greatest_common_factor(3, 9) == 3)
print(greatest_common_factor(16, 24) == 8)
print(greatest_common_factor(3, 5) == 1)