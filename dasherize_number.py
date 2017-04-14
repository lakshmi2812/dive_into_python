# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

def dasherize_number(num):
    str_num = str(num)
    list_num = list(str_num)
    new_list = list(range(len(list_num)))
    x = 0
    while x < len(list_num):
        n = int(list_num[x])
        if n % 2 == 1:
            if x == 0:
                new_list[x] = list_num[x] + '-'
            elif x == len(list_num) - 1:
                new_list[x] = '-' + list_num[x]
            else:
                if int(list_num[x-1]) % 2 == 1 and int(list_num[x+1]) % 2 == 1:
                    new_list[x] = list_num[x]
                elif int(list_num[x-1]) % 2 == 1 and int(list_num[x+1]) % 2 == 0:
                    new_list[x] = list_num[x] + '-'
                elif int(list_num[x-1]) % 2 == 0 and int(list_num[x+1]) % 2 == 1:
                    new_list[x] = '-' + list_num[x]
        else:
            new_list[x] = list_num[x]
        x+=1
    final_string = ''.join(new_list)
    return final_string
                
                
                
# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print(dasherize_number(203) == "20-3")
print(dasherize_number(303) == "3-0-3")
print(dasherize_number(333) == "3-3-3")
print(dasherize_number(3223) == "3-22-3")