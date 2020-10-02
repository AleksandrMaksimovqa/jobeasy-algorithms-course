number = input()
odd = 0
even = 0

for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print ('amount of even digits = ' ,even)
print ('amount of odd digits = ' ,odd)