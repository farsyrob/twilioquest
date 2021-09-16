import sys

python_is_glorious = True
failure_is_option = False 

#sys.argv[n] se n = 0, ele lê o o primeiro input, ou seja, o nome do proprio arquivo
greeting = sys.argv[1]

if greeting == 'For the glory of Python!':
	proper_greeting = True
else: 
	proper_greeting = False 

print (greeting)
print (bool(proper_greeting))
