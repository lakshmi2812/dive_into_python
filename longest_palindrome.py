# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:
#
#     "abcd".slice(1, 2) == "bc"
#     "abcd".slice(1, 3) == "bcd"
#     "abcd".slice(2, 1) == "c"
#     "abcd".slice(2, 2) == "cd"
#
# Difficulty: hard.

def is_palindrome(string):
    x = 0
    palindrome = True
    n = len(string)-1
    while x <= n:
        if string[x] != string[n-x]:
            palindrome = False
            break
        x+=1
    return palindrome

def longest_palindrome(string):
    x = 0
    #dist = 1
    sub_string = ""
    sub_string_list = []
    palindrome_dict = dict()
    while x < len(string):
        dist = 1
        #x = string.index(string[i])
        #print(x)
        while (x+dist) <= len(string):
            sub_string = string[x:x+dist]
            sub_string_list.append(sub_string)
            dist+=1
        x+=1
    #print(sub_string_list)
    for s in sub_string_list:
        if is_palindrome(s) == True:
            palindrome_dict[len(s)] = s
    #print(palindrome_dict)
    longest = 0
    for (k,v) in palindrome_dict.items():
        if k > longest:
            longest = k
    longest_palindrome = palindrome_dict[longest]
    return longest_palindrome
        

if __name__ == '__main__':
    print(longest_palindrome("abcbd") == "bcb")
    print(longest_palindrome("abba") == "abba")
    print(longest_palindrome("abcbdeffe") == "effe")
    