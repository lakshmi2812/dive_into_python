def no_repeat(year):
    yr = str(year)
    no_repeat_d = True
    for x in range(0, len(yr)):
        y = x+1
        while y < len(yr):
            if yr[x] == yr[y]:
                no_repeat_d = False
                break
            else:
                y = y+1
    return no_repeat_d

def no_repeats(year_start, year_end):
    no_repeat_list = []
    year = year_start
    while year>=year_start and year<= year_end:
        if no_repeat(year) == True:
            no_repeat_list.append(year)
        year+=1
    return no_repeat_list
    
if __name__ == '__main__':
    print("\nTests for #no_repeats")
    print("===============================================")
    print(no_repeats(1234, 1234) == [1234])
    print(no_repeats(1123, 1123) == [])
    print(no_repeats(1980, 1987) == [1980,1982,1983,1984,1985,1986,1987])
    print("===============================================")
    #print(no_repeat(1991) == False)
    #print(no_repeat(1985) == True)
    #print(no_repeat(2001) == False)