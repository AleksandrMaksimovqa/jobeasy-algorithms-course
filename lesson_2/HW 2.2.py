def zeros_not_for_heroes(n):
    for _ in range(len(str(n))):
        if n % 10 ==0:
            n = n // 10
    return print(n)

zeros_not_for_heroes(-1030)