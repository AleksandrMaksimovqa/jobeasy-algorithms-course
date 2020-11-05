def remove_duplicates(list):
    rem_list = []
    for word in list:
        if word not in rem_list:
            rem_list.append(word)
    return rem_list


list = ['dsd', 'we', '12','12','qa', 'we','fgghh','12','1']
print(remove_duplicates(list))


def row_sum_odd_numbers(n):
    a = 0
    for k in range(n):
        a +=k
    first_odd = a*2 + 1
    sum = 0
    for i in range(n):
        sum += first_odd + 2*i
    return sum

print(row_sum_odd_numbers(3))


