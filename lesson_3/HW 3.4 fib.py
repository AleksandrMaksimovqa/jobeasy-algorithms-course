

def fibonachi(n):
    if n <= 1:
        return n
    if n > 1:
        return fibonachi(n - 1) + fibonachi(n -2)

#print(fibonachi(7))


def factorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)

#print(factorial(4))
