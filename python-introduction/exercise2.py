# finding prime numbers

def primeCounter(n):
    numIsPrime = True
    
    for i in range(2, int(n**2)+1 ):
        if n % i == 0:
            numIsPrime = False
            break
    
    return numIsPrime

primeCount = 0

for i in range( 1, 100 ):
    if primeCounter(i):
        primeCount = primeCount + 1
        print (i)

print( primeCount )