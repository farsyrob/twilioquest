import sys

number_one = sys.argv[1]
number_two = sys.argv[2]

if (int(number_one) + int(number_two)) <= 0:
	print('You have chosen the path of destitution.')
elif 1 < (int(number_one) + int(number_two)) <= 100:
	print ('You have chosen the path of plenty.')
elif (int(number_one) + int(number_two)) > 100:
	print ('You have chosen the path of excess.')
