def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1
    if n < 0:
        print('Wrong value')
    if n == 0:
        print(0)


    if n == 1:
        print(1)
    if n == 2:
        print(1)

    if n > 2:
        index = 0
        while index < n - 2:
            fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
            index += 1
        print(fibonacci_2)

fibonacci(5)
