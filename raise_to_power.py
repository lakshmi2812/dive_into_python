import fractions
def raise_to_power(a,k):
    if k == 1:
        return a
    elif k > 1:
        power = a*raise_to_power(a,k-1)
        return power
    elif k < 0:
        p = abs(k)
        temp_power = a * raise_to_power(a,p-1)
        power = fractions.Fraction(1,temp_power)
        return power
    
if __name__ == '__main__':
    print(raise_to_power(2,4))
    print(raise_to_power(2,-4))
        
        