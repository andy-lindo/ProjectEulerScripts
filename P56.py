###https://projecteuler.net
###Problem 56 - https://projecteuler.net/problem=56
### Solution 6/10/
import sys
sys.path.append('./utils')
from primes import isPrime


#initial parameters for diagnol wrap
diagnol  = 1.0
primes_on_diag = 0.0
side_len = 1 
curren_int = 1
#begins with diagnol ratio
#artifact of necesity
percent_prime_diagnol = 1
#each iteration wraps one new layer around
#stops once desired percentage reached
while percent_prime_diagnol > .1:
	#each layer increases
	side_len += 2
	to_next_diagnol = side_len - 1
	diagnol += 4.0
	for i in range(4):
		curren_int += to_next_diagnol

		if isPrime(curren_int):
			primes_on_diag += 1.0

	percent_prime_diagnol = primes_on_diag/diagnol

#final answer
print(side_len)
