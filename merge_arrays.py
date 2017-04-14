def merge_arrays(a,b):
    #coding and coding..
    c = []
    for item in a:
        if item not in b and item not in c:
            c.append(item)
        else:
            if item in b and item not in c:
                if a.count(item) == b.count(item):
                    c.append(item)
    for item in b:
        if item not in a and item not in c:
            c.append(item)
    c.sort()
    return c

if __name__ == '__main__':
    
    print("Basic Tests")
    print(merge_arrays([10, 10, 10, 15, 20, 20, 25, 25, 30, 7000],[10, 15, 20, 20, 27, 7200]) == [15, 20, 25, 27, 30, 7000, 7200])
    print(merge_arrays([500, 550, 1000, 1000, 1400, 3500],[2, 2, 2, 2, 3, 1500]) == [2, 3, 500, 550, 1000, 1400, 1500, 3500])
    print(merge_arrays([5],[5, 5, 7]) == [7])
    print(merge_arrays([2,2,2,2,2,2,2,2,2,3,3,3,3,3,5,7],[2,2,2,2,2,2,2,2,2,3,3,3,3,3,6,6,8]) == [2, 3, 5, 6, 7, 8])
    
    