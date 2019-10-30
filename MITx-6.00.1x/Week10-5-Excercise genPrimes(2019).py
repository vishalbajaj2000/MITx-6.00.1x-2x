def genPrimes():
    n = 1
    x= [2,3,5,7]
    while True:
        n += 1
        if n in x:
            yield n
        else:
            test = True
            for num in x:
                if n % num ==0:
                    test = False
            if test == True:
                x.append(n)
                yield n



 
prime = genPrimes()
for i in range(10):
    print(prime.__next__())