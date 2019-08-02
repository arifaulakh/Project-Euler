fib = [1,2]
while fib[len(fib)-1]<4000000:
    fib.append(fib[len(fib)-1]+fib[len(fib)-2])
s = 0
for i in fib:
    if i%2==0 and i<=4000000:
        s+=i
print(s)