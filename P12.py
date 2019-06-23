import math

####	FIND FIRST TRIANGLE NUMBER WITH 500 DIVISORS
####	T(n) = (n (n+1))/2
####	take advanate of this to find the divisors of each side. 
####	



###return first triangle number with atleast n divisors
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
 
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < factor_limit:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

n = find_triangular_index(500)

print(n * n + 1 /2)
print('done')