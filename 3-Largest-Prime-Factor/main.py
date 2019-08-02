from math import sqrt, ceil
def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
N = 600851475143
P = primes(ceil(sqrt(N)))
pf = []
for each in P:
    if N%each==0:
        pf.append(each)
print(max(pf))