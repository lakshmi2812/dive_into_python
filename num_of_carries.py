def number_of_carries(a,b):
    a_list_str = list(str(a))
    b_list_str = list(str(b))
    a_list = list(map(int, a_list_str))
    b_list = list(map(int, b_list_str))
    if len(a_list) < len(b_list):
        less_list = a_list
        big_list = b_list
    else:
        less_list = b_list
        big_list = a_list
    while len(less_list) < len(big_list):
        less_list.insert(0,0)
    x = 0
    count = 0
    while x < len(less_list) and x < len(big_list):
        if (less_list[x] + big_list[x]) > 9:
            count+=1
        x+=1
    carries = count
    return count

print(number_of_carries(543, 3456) == 0)
print(number_of_carries(543,3456) == 0)
print(number_of_carries(1927,6426) == 2)
print(number_of_carries(9999,1) == 4)
print(number_of_carries(1234,5678) == 2)

            
    
    