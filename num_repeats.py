# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.

def num_repeats(string):
    string_lst = list(string)
    letter_count = []
    for x in string_lst:
        if string_lst.count(x) > 1:
            if x not in letter_count:
                letter_count.append(x)
    print(letter_count)
    repeats = len(letter_count)
    return repeats
# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if __name__ == '__main__':

    print(num_repeats("abdbc") == 1)
    # one character is repeated
    print(num_repeats("aaa") == 1)
    print(num_repeats("abab") == 2)
    print(num_repeats("cadac") == 2)
    print(num_repeats("abcde") == 0)
