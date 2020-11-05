def elements_bellow_arith_mean(list):
    ar_mean = 0
    new_list = []
    for i in list:
        ar_mean += i
    ar_mean = ar_mean / len(list)
    for i in list:
        if i < ar_mean:
            new_list.append(i)
    return new_list

list = [5,6,7,4,3,7,3,8,5,2,16,6,7,3,8]
print(elements_bellow_arith_mean(list))