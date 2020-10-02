from random import randint

n = int(input('Input a number of digits'))

lowest_boundary = 10 ** (n-1)
highest_boundary = (10 ** n) - 1

number = randint(lowest_boundary,highest_boundary)
#print(number)
result = 0
for i in range(n):
    a = number % 10
    result += a
    number = number // 10

print(result)

# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0