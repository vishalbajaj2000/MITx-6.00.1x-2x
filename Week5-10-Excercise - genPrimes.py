def genPrimes():
    n = 1
    x= [2,3,5,7]
    while True:
        n += 1
        if n in x:
            yield n
        for num in x:
            if n % num ==0:
                break
            else :
                x.append(n)
                yield n
                break
        print(x)

prime = genPrimes()
for i in range(10):
    print(prime.__next__())