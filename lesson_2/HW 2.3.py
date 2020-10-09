
def sum_of_all_digits(number):
    str_number = str(number)
    sum = 0
    for _ in range(len(str_number)):
        sum += int(str_number[_])
    return (sum)


n = int(input('Enter a number: ', ))
while (n-10 >= 0):
    n = sum_of_all_digits(n)


print(n)