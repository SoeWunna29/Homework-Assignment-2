def cal(n):
    if n % 2 == 0 and n <= 1:
        return 0
    elif n % 2 == 1 and n <= 1:
        return 1

    elif n % 2 == 0:
        return n * cal(n - 2)
    return n * cal(n - 2)


print(cal(5))
print(cal(8))
