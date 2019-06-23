import math
import numpy
### implementations of sieve of Eratosthenes
### https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
### Returns list of all primes under int number
def sieve(n):
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i*i::i] = False
    return numpy.flatnonzero(flags)