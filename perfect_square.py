#Write a function that returns the number of perfect squares that occur before a number

def square(num):
    x = 1
    square_b = False
    factor_list = []
    while x <= num:
        if num % x == 0:
            factor_list.append(x)
        x+=1
    for i in factor_list:
        if i*i == num:
            square_b = True
            break
    return square_b

def perfect_square(n):
    x = 1
    count = 0
    while x < n:
        if square(x) == True:
            count+=1
        x+=1
    return count


if __name__ == '__main__':
    print(perfect_square(5) == 2)
    print(perfect_square(10) == 3)
    print(perfect_square(25) == 4)
    #print(square(1) == True)
    #print(square(2) == False)
    #print(square(4) == True)            
    #print(square(19) == False)            
        
    