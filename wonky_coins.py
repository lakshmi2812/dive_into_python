# Catsylvanian money is a strange thing: they have a coin for every
# denomination (including zero!). A wonky change machine in
# Catsylvania takes any coin of value N and returns 3 new coins,
# valued at N/2, N/3 and N/4 (rounding down).
#
# Write a method `wonky_coins(n)` that returns the number of coins you
# are left with if you take all non-zero coins and keep feeding them
# back into the machine until you are left with only zero-value coins.
#
# Difficulty: 3/5

def wonky_coins(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        count = wonky_coins(n//2)+wonky_coins(n//3)+wonky_coins(n//4)
        return count
    
        
            
if __name__ == '__main__':
    #print(wonky_coins(5))
    print("\nTests for #wonky_coins")
    print("===============================================")
    print(wonky_coins(1) == 3)
    print(wonky_coins(5) == 11)
    print(wonky_coins(6) == 15)
    print(wonky_coins(0) == 1)
    print("===============================================")
    
    
    
        