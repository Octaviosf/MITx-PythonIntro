def genPrimes(num=2):
    multDict = {}
    while True:
        try:
            for i in range(1,num-1):
                for k in range(1,num-1):
                    if str(i)+'*'+str(k) in multDict.keys():
                        if multDict[str(i)+'*'+str(k)] == num:
                            raise Exception
                    else:
                        multDict[str(k)+'*'+str(i)] = i*k
                        multDict[str(i)+'*'+str(k)] = k*i
                        if multDict[str(k)+'*'+str(i)] == num:
                            raise Exception
            yield num
            num += 1
        except Exception:
            num += 1

import time
start_time = time.time()
primes = genPrimes()

for i in range(50):
    print(str(primes.__next__())+', ', end ='')

print('\n--- %s seconds ---' %(time.time()-start_time))

