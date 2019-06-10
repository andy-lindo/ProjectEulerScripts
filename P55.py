###https://projecteuler.net
###Problem 55 - https://projecteuler.net/problem=55
### Solution 6/10/19
import math 

def is_Palindrome(n):
	return str(n) == str(n)[::-1]

def is_Lychrel(n):
	for i in range(50):
		new_num = n + int(str(n)[::-1])
		if is_Palindrome(new_num):
			return False
		n = new_num
	return True


lychrel_under_ten_thousand = 0 
for i in range(1,10001):
	if is_Lychrel(i):
		lychrel_under_ten_thousand += 1
print(lychrel_under_ten_thousand)