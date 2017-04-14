# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#
# You would not be expected to already know about modulo for the
# challenge.
#
# Difficulty: medium.

def is_prime(number):
    x = 1
    prime = True
    if number == 2:
        prime = True 
    while x <= number//2:
        if number % x == 0:
            if x!=1 and x!=number:
                prime = False
                break
        x+=1
    return prime

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if __name__ == '__main__':
    print(is_prime(2) == True)
    print(is_prime(3) == True)
    print(is_prime(4) == False)
    print(is_prime(9) == False)
        