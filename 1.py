def fancy_printing(n, divisible_num):
    for i in range(n):
        if i == 0:
            print(i)
        elif divisible_num % i == 0:
            print("Buzz!")
        else:
            print(i)


fancy_printing(10, 5)
