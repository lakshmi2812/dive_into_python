def factorial(n):
    if n == 1:
        return 1
    else:
        res = n*factorial(n-1)
        return res
    

if __name__ == '__main__':
    print(factorial(5))