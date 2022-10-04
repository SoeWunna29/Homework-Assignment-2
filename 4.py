def increment(n):
    return n + 1


def triple(n):
    return 3 * n


def square(n):
    return n * n


def foo(f, n):
    if n == 1:
        return f
    return lambda x: f(foo(f, n - 1)(x))


print(increment(5))
add3 = foo(increment, 3)
print(add3(5))
print(foo(triple, 5)(1))
print(foo(square, 2)(5))

print(foo(square, 4)(5))
