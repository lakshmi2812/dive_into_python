# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.
#
# Difficulty: 1/5

def letter_count(string):
    str_list = [s for s in string if s!= " "]
    l_count_dict = dict()
    for i in str_list:
        l_count_dict[i] = str_list.count(i)
    return l_count_dict


print("\nTests for #letter_count")
print("===============================================")
print(letter_count("cat") == {"c" : 1, "a" : 1, "t" : 1})
print(letter_count("moon") == {"m" : 1, "o" : 2, "n" : 1})
print(letter_count("cats are fun") == {"a" : 2, "c" : 1, "e" : 1, "f" : 1, "n" : 1, "r" : 1, "s" : 1, "t" : 1, "u" : 1})
print("===============================================")