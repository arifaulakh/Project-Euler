def fac(x):
    if x==0:
        return 1
    return x*fac(x-1)
def choose(a, b):
    return int(fac(a)/((fac(b))*fac(a-b)))
n = 20
m = 20

print(choose(n+m, n))


