###https://projecteuler.net
###Problem 51 - https://projecteuler.net/problem=51
### Solution 6/10/19


###Checks if the number uses exact same numbers if multiplied by 1-6
def is_Permutated(n):

	premutations = [n*i for i in range(2,7)]
	n_list = list(str(n))

	for i in premutations:
		
		# if either len of number or set created are
		# not equal property does not hold
		if len(list(str(i))) != len(n_list) or set(str(i)) != set(n_list):
			return False
	
	return True

#simple check from 1 until property found.
permutaion_found = False

i = 1
while (not permutaion_found):
	i += 1
	permutaion_found = is_Permutated(i)
print(i)