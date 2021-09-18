#inputs = list of all arguments to my script

#for each input in the list, do the following:
#    convert the input to a number
#    set my print string equal to a blank/empty string
#    if the number is divisible by 3, append "fizz" to the output string
#    if the number is divisible by 5, append "buzz" to the output string
#    if by now the output string is still blank, set it to the input number
#    print the output string

import sys

numbers = sys.argv
numbers.pop(0)

for item in numbers:
	item = int(item)
	output = ''
	
	if item%3 == 0:
		output = output + 'fizz'
	
	if item%5 == 0:
		output = output + 'buzz'
	
	if output == '':
		print(item)
	else:
		print(output)
	

