def multiply_ab_recursive(a,b):
    '''Multiples a and b and returns the product a*b using only + and - operators'''
    if b == 1:
        return a
    else:
        product = a + multiply_ab_recursive(a, b-1)
        return product

if __name__ == '__main__':
    print(multiply_ab_recursive(2,6))