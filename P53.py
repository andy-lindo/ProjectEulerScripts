###https://projecteuler.net
###Problem 53 - https://projecteuler.net/problem=53
### Solution 6/10/19


def create_i_list(last_i_list):
	new_i_list = [1]
	for i in range(len(last_i_list)-1):
		new_i_list.append(last_i_list[i]+last_i_list[i+1])
	new_i_list.append(1)
	return new_i_list
more_than_million_perm = 0

i_list = [1,1]


for i in range(2,101):
	i_list = create_i_list(i_list)
	more_than_million_perm += 	sum(j > 1000000 for j in i_list)
print(more_than_million_perm)
