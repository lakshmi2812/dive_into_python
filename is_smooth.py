def is_smooth(arr):
    #coding and coding..
    is_smooth = False
    n = len(arr)
    if n % 2 == 1:
        middle = arr[(n//2)]
        print(middle)
    else:
        middle = arr[(n//2)]+arr[(n//2)-1]
        print(middle)
    if arr[0] == arr[n-1] and arr[0] == middle:
        is_smooth = True
        print(arr[0], arr[n-1])
    return is_smooth

if __name__ == '__main__':
    
    #print(is_smooth([7, 2, 2, 5, 10, 7]) == True)
    print(is_smooth([-12, 34, 40, -5, -12, 4, 0, 0, -12]) == True)
    print(is_smooth([-5, -5, 10]) == False)
    print(is_smooth([4, 2]) == False)
    print(is_smooth([45, 23, 12, 33, 12, 453, -234, -45]) == False)
    print(is_smooth([9, 0, 15, 9]) == False)
    print(is_smooth([-6, 6, -6]) == False)
    print(is_smooth([26, 26, -17]) == False)
    print(is_smooth([-7, 5, 5, 10]) == False)
    print(is_smooth([3, 4, 5]) == False)
    print(is_smooth([-5, 3, -1, 9]) == False)