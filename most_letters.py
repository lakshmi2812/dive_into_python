# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.
def most_letters(string):
    near_az = False
    str_list = list(string)
    n = len(string)-1
    if 'a' in str_list:
        a_idx = str_list.index('a')
        if 'z' in str_list: 
            z_idx = str_list.index('z')
            if z_idx in range(a_idx, a_idx+4):
                near_az = True
    return near_az


print(most_letters("baz") == True)
print(most_letters("abz") == True)
print(most_letters("abcz") == True)
print(most_letters("a") == False)
print(most_letters("z") == False)
print(most_letters("za") == False)
                