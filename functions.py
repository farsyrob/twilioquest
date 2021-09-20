import sys
#this defines function which takes the first and second number
def add_numbers(first_number,second_number):
	#this creates "result_sum" which is the operation i want to do with both numbers
	result_sum = first_number + second_number
	#this stores the result sum operation in memory so i can use it with any variables later on
	return result_sum
#this summons my function and attaches it to a variable i can later call on to print, and i have to store the numbers i want to use in it
first_number = add_numbers(121,4)

print (first_number)