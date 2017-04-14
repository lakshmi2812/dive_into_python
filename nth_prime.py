# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.
#
# Difficulty: medium.

# You may use our `is_prime?` solution.

def is_prime(number):
    x = 1
    prime = True
    if number < 2:
        prime = False
    if number == 2:
        prime = True
    while x <= number//2:
        if number % x == 0:
            if x!=1 and x!=number:
                prime = False
                break
        x+=1
    return prime


def nth_prime(n):
    count = 0
    x = 1
    while count < n:
        if is_prime(x):
            count+=1
            prime_n = x
        x+=1
    return prime_n


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if __name__ == '__main__':
    print(nth_prime(1) == 2)
    print(nth_prime(2) == 3)
    print(nth_prime(3) == 5)
    print(nth_prime(4) == 7)
    print(nth_prime(5) == 11)
