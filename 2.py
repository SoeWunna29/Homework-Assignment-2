def sum_num(n):
    total = 0
    step = 1
    if n % 2 == 0:
        for i in range(n + 1):
            if step % 2 == 0:
                pass
            else:
                total += i
            step += 1
        print(total)
    else:
        for i in range(n + 1):
            if step % 2 != 0:
                pass
            else:
                total += i
            step += 1
        print(total)


sum_num(4)
sum_num(5)
