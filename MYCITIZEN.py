"""
A docstring that describes the class

An init method that takes first_name 
and last_name arguments (strings) 
and assigns them as instance variables

An instance method called full_name 
that returns a string that combines 
the first and last name instance variables, 
with a single space between them

A class variable called greeting
which is a string set to For the glory of Python!
"""
import sys

class Citizen:
	"""Class docstrings go here."""
	#this is the class variable
	greeting = "For the glory of Python!"
#this is going to be the instance method
	def __init__(self,first_name=1,last_name=2):
		"""class method docstrings go here."""
		self.first_name = sys.argv[1]
		self.last_name = sys.argv[2]
		
full_name = Citizen("","")
print(full_name.greeting)
print(full_name.first_name + " " + full_name.last_name)

	