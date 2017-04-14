# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.
#
# Difficulty: medium.

def capitalise_words(string):
    if string == "":
        op = ""
    else:
        op_list = []
        str_list = string.split(' ')
        for x in str_list:
            x_list = list(x)
            #print(x_list)
            x_list[0] = x_list[0].upper()
            x_cap = ''.join(x_list)
            op_list.append(x_cap)
        op = ' '.join(op_list)
    print(op)
    return op

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if __name__ == '__main__':
    print(capitalise_words("this is a sentence") == "This Is A Sentence")
    print(capitalise_words("mike bloomfield") == "Mike Bloomfield")
    print(capitalise_words("") == "")