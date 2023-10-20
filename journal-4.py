#this function will define a class that describes my fav animal

#I will describe a monkey

import sys
class shape:
	def print(self):
		print("Here is my animal!")
		print(f"length of arms = {self.lenarms}")
		print(f"length of legs = {self.lenlegs}")
		print(f"number of eyes = {self.numeyes}")
		print(f"tail? = {self.tail}")
		print(f"furry? = {self.furry}")
	def __init__(self, lenarms, lenlegs, numeyes, tail, furry):
		self.lenarms = lenarms
		self.lenlegs = lenlegs
		self.numeyes = numeyes
		self.tail = tail
		self.furry = furry

def main():
	lenarms = 4.0
	lenlegs = 4.0
	numeyes = 2
	tail = yes = True
	furry = yes = True

	our_shape = shape(lenarms=lenarms, lenlegs=lenlegs, numeyes=numeyes, tail=tail, furry=furry)

	our_shape.print()

if __name__=="__main__":
	main()
