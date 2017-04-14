#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_squares(n):
    x = 1
    sum_of_squares = 0
    while x <= n:
        square = x*x
        sum_of_squares = sum_of_squares + square
        x+=1
    return sum_of_squares

def square_of_sum(n):
    x = 1
    sum = 0
    while x <= n:
        sum = sum + x
        x+=1
    square_of_sum = sum*sum 
    return square_of_sum

def sum_square_difference(n):
    global sum_squares
    global square_of_sum
    sumof_square = sum_squares(n)
    print(sumof_square)
    squareof_sum = square_of_sum(n)
    print(squareof_sum)
    diff = squareof_sum - sumof_square
    return diff

if __name__ == '__main__':
    print(sum_square_difference(10) == 2640)
    print(sum_square_difference(100))
    
    

        
        