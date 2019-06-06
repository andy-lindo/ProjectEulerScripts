###https://projecteuler.net
###Problem 43 - https://projecteuler.net/problem=43
### Solution 6/5/19
import itertools



###Helper function to check property described in problem
def check_property(n):
	s = str(n)
	primes = [2,3,5,7,11,13,17]

	slices = [int(s[i:i+3]) for i in range(1,8)]
	divisible = [slices[i] % primes[i] for i in range(len(slices))]
	
	return all(p == 0 for p in divisible)  

pandigitals_with_property_sum = 0

###Makes all palindrom
def make_pandigital(i,l):
	###base case: list is empty, all integers added to pandigital
	if len(l) == 0:
		### only return those that have desired property
		if check_property(int(i)):
			return int(i)
		return 0;

	total = 0
	###recursive step, add each item in list individually,
	### recurse with remaining list
	for j in l:
		k = l.copy() 
		k.remove(j)
		new_i = i + str(j)
		total += make_pandigital(new_i,k)
	return total

###initial pandigital number
for i in range(1,10):
	a = list(range(10))
	a.remove(i) 
	###recursive call for pandigital starting with i
	pandigitals_with_property_sum += make_pandigital(str(i), a)

print(pandigitals_with_property_sum)