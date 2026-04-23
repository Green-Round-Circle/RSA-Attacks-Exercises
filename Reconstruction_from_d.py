import math
import random

def factor_from_d(n, e, d):
    k = e * d - 1
    s = 0
    t = k
    while t % 2 == 0:
        s += 1
        t //= 2

    while True:
        g = random.randrange(2, n - 1)
        y = pow(g, t, n)
        if y == 1 or y == n - 1:
            continue

        for _ in range(s):
            x = pow(y, 2, n)
            if x == 1:
                p = math.gcd(y - 1, n)
                if 1 < p < n:
                    return p, n // p
            if x == n - 1:
                break
            y = x
