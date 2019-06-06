###https://projecteuler.net
###Problem 19 - https://projecteuler.net/problem=19
### Solution 6/5/19


### days in each momth
### Jan-Dec
days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
### [day,month,year] 20th century
first_sunday = [6,0,1901]

date = first_sunday
count = 0

##in the 20th century
while date[2] < 2001:
	##First of the month
	if date[0] ==1:
		count += 1

	#next sunday
	date[0] = date[0] + 7

	##change month
	if date[0] > days_in_month[date[1]]:
		date[0] = date[0] % days_in_month[date[1]]
		date[1] = date[1] + 1

	###change year
	if date[1] > 11:
		date[2] = date[2] + 1
		date[1] = 0

		##check for leap year
		if date[2] % 4 == 0:
			days_in_month[1] = 29
		else:
			days_in_month[1] = 28

print(count)