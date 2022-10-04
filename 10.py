def bnc_bck_frth(n):
    k = 1
    assending = True
    num_found = False
    for i in range(1, n):
        # print(k)
        j = i
        while j != 0:
            if i % 10 == 7:
                num_found = True
                break
            j //= 10
        # print(num_found)
        if i % 7 == 0 or num_found == True:
            num_found = False
            if assending:
                assending = False
            else:
                assending = True
        if assending:
            k += 1
        else:
            k -= 1
    return k


print(bnc_bck_frth(7))
print(bnc_bck_frth(8))
print(bnc_bck_frth(15))
print(bnc_bck_frth(21))
print(bnc_bck_frth(22))
print(bnc_bck_frth(30))
