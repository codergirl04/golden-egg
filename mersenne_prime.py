def findPrimes(n):
    # finds n prime numbers
    primes = [2]
    sec = []
    r = 0
    isPrime = True
    while len(primes)<n:
        sec = list(range(r, r+10))
        for i in sec:
            if i==0 or i==1 or i==2:
                continue
            for j in primes:
                if i%j==0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            if isPrime:
                primes.append(i)
        r += 10
    return primes[:n]

def findMersenneNumber(num):
    primes = findPrimes(num)
    return 2**primes[num-1]-1

print(findMersenneNumber(1))