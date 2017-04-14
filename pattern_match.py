def pattern_match(a, b):
    a_dict = dict()
    b_dict = dict()
    x = 0
    y = 0
    count = 0
    while x < len(a)-1:
        a_dict[x] = a[x] + a[x+1]
        #print(a_dict)
        x+=1
    while y < len(b)-1:
        b_dict[y] = b[y] + b[y+1]
        y+=1
    for (k,v) in a_dict.items():
        if (k,v) in b_dict.items():
            count+=1
    print(a_dict, b_dict)
    return count

if __name__ == '__main__':
    
    print(pattern_match('abc', 'abc') == 2)
    print(pattern_match('xxcaazz', 'xxbaaz') == 3)
    print(pattern_match('abc', 'axc') == 0)
    
    