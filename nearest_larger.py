# Write a function, `nearest_larger(arr, i)` which takes an array and an
# index.  The function should return another index, `j`: this should
# satisfy:
#
# (a) `arr[i] < arr[j]`, AND
# (b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j2]`.
#
# In case of ties (see example below), choose the earliest (left-most)
# of the two indices. If no number in `arr` is larger than `arr[i]`,
# return `nil`.
#
# Difficulty: 2/5

def nearest_larger(arr, idx):
    l = len(arr)
    right_idx = (idx+0.5)
    left_idx = (idx-0.5)
    left_dist = 1
    right_dist = 1
    nearest = 0
    nearest_idx = 'nil'
    nearest_left = 'nil'
    nearest_left_idx = 'nil'
    nearest_right_idx = 'nil'
    nearest_right = 'nil'
    while left_idx > 0 and left_idx < idx:
        left_idx = idx - left_dist
        print('my left index is:', left_idx)
        if arr[left_idx] > arr[idx]:
            nearest_left = arr[left_idx]
            nearest_left_idx = left_idx
            break
        left_dist+=1
    while right_idx > idx and right_idx < l-1:
        right_idx = idx + right_dist
        print('my right index is: ', right_idx)
        if arr[right_idx] > arr[idx]:
            nearest_right = arr[right_idx]
            nearest_right_idx = right_idx
            break
        right_dist+=1
    if nearest_left == 'nil':
        nearest_idx = nearest_right_idx
    elif nearest_right == nearest_left:
        nearest_idx = nearest_left_idx
    elif nearest_right == 'nil' and nearest_left == 'nil':
        nearest_idx = 'nil'
    else:
        nearest_idx = nearest_left_idx
    #print(nearest_left)
    #print(left_idx)
    #print(nearest_right)
    #print(right_idx)
    #print(nearest_idx)
    return nearest_idx

if __name__ == '__main__':
    
    print("Tests for #nearest_larger")
    print("===============================================")
    print(nearest_larger([2,3,4,8], 2) == 3)
    print(nearest_larger([2,8,4,3], 2) == 1)
    print(nearest_larger([2,6,4,8], 2) == 1)
    print(nearest_larger([2,6,4,6], 2) == 1)
    print(nearest_larger([8,2,4,3], 2) == 0)
    print(nearest_larger([2,4,3,8], 1) == 3)
    print(nearest_larger([2, 6, 4, 8], 3) == 'nil')
    print(nearest_larger([2, 6, 9, 4, 8], 3) == 2)
    print("===============================================")