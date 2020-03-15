cache = {}
primes = []
def find_primes(maxNum, primes, cache):
    print(f"trying: {maxNum}")
    try: 
        if maxNum == 2:
            cache[maxNum] = 2
            primes.append(maxNum)
            return
        if maxNum == 1:
            cache[maxNum] = 1
            return
        if maxNum == 0:
            return
        if cache.get[maxNum]:
            return
    except:
        pass

    isPrime = maxNum
    if isPrime % 2 is not 0:
        primes.append(isPrime)
        cache[isPrime] = isPrime

    while isPrime % 2 == 0:
        cache[maxNum] = maxNum
        isPrime = isPrime / 2
    find_primes(maxNum - 1, primes, cache)
    
find_primes(997, primes, cache)
primes.sort()
print(primes)