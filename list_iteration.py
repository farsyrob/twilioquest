import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

for index, item in enumerate (order_of_succession, start = 1):
	#função sys.argv funciona como lista; 
	#index vai de 1 a N ; INDEX - 1 = de 0 a N-1
	string_to_print = f"{index}. {sys.argv[index-1]}",
	print(string_to_print)
