
def arrayManip(array):
# your code goes here
    b_arr = list(range(len(array)))
    res = []
    least_greater = -10
    for item in array:
        x = array.index(item) + 1
        if x < len(array)-1:
            if array[x+1] > item:
                least_greater = array[x+1]
        while x < len(array):
            if array[x] > item and array[x] < least_greater:
                least_greater = array[x]
            x+=1
        if least_greater == -10:
            res.append(-1)
        else:
            res.append(least_greater)
    return res

if __name__ == '__main__':
    print(arrayManip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]) == [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1])