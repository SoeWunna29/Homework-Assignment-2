def multiply(a, b):
    return a * b


def op(a, b, c):
    num = multiply(a, b)
    return num + c


print(op(2, 4, 3))
print(op(0, 3, 2))
print(op(3, 0, 2))
