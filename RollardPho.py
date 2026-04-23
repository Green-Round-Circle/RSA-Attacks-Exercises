import random
from math import gcd
from Crypto.Util.number import long_to_bytes,isPrime
#We will use this attack when we want to factorize N, when N is small
def rollardPho(n):
    if n%2==0:
        return 2
    x=random.randrange(2,n)
    f = lambda x: (x*x+1)%n 

    y =x 
    d =1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y),n)
    if d == n:
        return None
    else: return d 
