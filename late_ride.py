def late_ride(n):
    #coding and coding..
    hrs = n//60
    mins = n%60
    hrs_str = str(hrs)
    mins_str = str(mins)
    hrs_list = list(hrs_str)
    mins_list = list(mins_str)
    time1 = 0
    for i in hrs_list:
        time1 = time1 + int(i)
    time2 = 0
    for j in mins_list:
        time2 = time2 + int(j)
    time_taken = time1 + time2
    return time_taken


if __name__ == '__main__':

    print("Basic Tests")
    print(late_ride(240) == 4)
    print(late_ride(808) == 14)
    print(late_ride(1439) == 19)
    print(late_ride(0) == 0)
    print(late_ride(23) == 5)
    print(late_ride(8) == 8)