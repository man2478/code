for x in range (1,10000):
    n = 2
    z = 0
    k = 0
    while n < 10000:

        if (x % n) == 0 and x != n:
            z += 1

        if (x % n) != 0 and x == 2:
            k += 1

        n += 1
    if z == 0 and x != 1:
        print(x)
    else:
        pass