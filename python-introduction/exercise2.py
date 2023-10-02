# finding prime numbers

def primeCounter(n):
    numIsPrime = True
    i = 0
    
    for i in range(2, n):
        if n % i == 0:
            numIsPrime = False
            break
    
    return numIsPrime

choosen = int( input( "choose your number: " ) )

if primeCounter( choosen ):
    print( "number is prime." )

else:
    print( "not prime :(" )
