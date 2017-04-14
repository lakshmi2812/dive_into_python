def str_enc(s):
    s_list = list(s)
    count = 1
    s_enc = ""
    while count < len(s_list)-2:
        count+=1
    sum_s = 0
    i = 0
    count_list = list(str(count))
    if len(count_list) != 1:
        while i < len(count_list):
            sum_s+=int(count_list[i])
            i+=1
    s_enc = s_list[0] + str(sum_s) + s_list[len(s_list)-1]
    return s_enc
        

def same_encryption(s1,s2):
    same_enc = False
    if str_enc(s1) == str_enc(s2):
        same_enc = True
    print(str_enc(s1))
    print(str_enc(s2))
    return same_enc


#print(same_encryption("abc","abc") == True)
#print(same_encryption("abc","abd") == False)
#print(same_encryption("fKhjuytrdfcdc","flJc") == True)
#print(same_encryption("OKhjuytrdfcdc","OijK") == False)
print(same_encryption('YZYT', 'YHjMyBdtLPmEzeiiMYAKxKkzIrYaHvXvSTdKmUfCGuoYmUISKuTPnuHOsaditinsRtT'))# == True)

        
    