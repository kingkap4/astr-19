#python exceptions let you deal with unexpected results


try: 
	print(a)  #this will throw an exception bc a is undefined
except:
	print("a is not defined")

#there are specific errors to hep with cases
try:
	print(a)
except NameError:
	print("a is still not defined")
except:
	print("something else went wrong")

#this will break our program bc a is not defined
print(a)