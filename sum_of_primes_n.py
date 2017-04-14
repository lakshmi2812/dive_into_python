def is_prime(n):
    x = 1
    prime = True
    while x <= n:
        if n % x == 0:
            if x != 1 and x != n:
                prime = False
                break
        x+=1
    return prime

def sum_of_primes_n(n):
    x = 2
    prime_sum = 0
    while x < n:
        if is_prime(x) == True:
            #print(is_prime(x))
            prime_sum += x
            #print(prime_sum)
        x+=1
    return prime_sum

if __name__ == '__main__':
    print(sum_of_primes_n(5) == 5)
    print(sum_of_primes_n(6) == 10)
    print(sum_of_primes_n(10) == 17)
    print(sum_of_primes_n(200))

