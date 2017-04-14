#Write a method that takes in a number and returns true if it is a
# power of 2. Otherwise, return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
#
# Difficulty: medium.

def is_power_of_two(num):
    power_2 = True
    if num < 1:
        power_2 =  False
    else:
        while num>1:
            rem = num%2
            num = num//2
            if rem == 1:
                power_2 = False
                break
    return power_2

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

assert(is_power_of_two(1) == True)
assert(is_power_of_two(16) == True)
assert(is_power_of_two(64) == True)
assert(is_power_of_two(78) == False)
assert(is_power_of_two(0) == False)


