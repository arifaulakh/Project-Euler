for a in range(0,333):
    for b in range(a+1, 500):
        for c in range(b+1, 1000):
            if a+b+c == 1000:
                if a**2+b**2==c**2:
                    product = a*b*c
                    print(product)
                    break