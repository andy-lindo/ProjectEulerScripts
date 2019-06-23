import math
import itertools
####    FIND FIRST TRIANGLE NUMBER WITH 500 DIVISORS
####    T(n) = (n (n+1))/2
####    take advanate of this to find the divisors of each side. 
####    


def sieve_alg(n):
    number = 10**n
    primes = list(range(2,number))

    i = 2
    #from 2 to sqrt(number)
    while(i <= int(math.sqrt(number))):
        #if i is in list
        #then we gotta delete its multiples
        if i in primes:
            #j will give multiples of i,
            #starting from 2*i
            for j in range(i*2, number+1, i):
                if j in primes:
                    #deleting the multiple if found in list
                    primes.remove(j)
        i = i+1
    return primes

primes = sieve_alg(4)
primes_2_digits = list(itertools.ifilter( lambda x:  9 < x < 100, primes))

for i in primes_2_digits:
    sub_list = 
    for j in primes_2_digits:
