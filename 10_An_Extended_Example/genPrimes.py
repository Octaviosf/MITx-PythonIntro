def genPrimes():
    primes = [2]
    num = 3
    prime = False
    yield 2
    while True:
        for i in primes:
            if num % i != 0:
                prime = True
            else:
                num += 1
                prime = False
                break
        if prime:
            yield num
            primes.append(num)
            num += 1

import time
start_time = time.time()
primes = genPrimes()

for i in range(50):
    print(str(primes.__next__())+', ', end ='')

print('\n--- %s seconds ---' %(time.time()-start_time))
