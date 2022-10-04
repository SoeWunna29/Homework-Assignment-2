prime_nums = []


def is_prime(num):
    for n in range(0, num + 1):
        if n > 0:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                prime_nums.append(n)
    return prime_nums


def cnt_primes(num):
    cnt_list = is_prime(num)
    print(f"Prime numbers from 1 to {num}", cnt_list)
    print(len(cnt_list) - 1, f"prime numbers from 1 to {num}")


cnt_primes(6)
