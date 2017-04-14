def sum_to_n_recursion(n):
    '''This method returns the sum of first n natural numbers. Input is n'''
    if n < 1:
        return 'Error! Enter a number greater than 1'
    elif n == 1:
        return 1
    else:
        sum = n + sum_to_n_recursion(n-1)
        return sum
    

if __name__ == '__main__':
    print(sum_to_n_recursion(3))
    print(sum_to_n_recursion(10))
    