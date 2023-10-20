import numpy as np

def f(x):
	return (np.sin(x))

def g(x):
	return(np.cos(x))

def main():
	x = np.linspace(0,2*np.pi, num=1000)
	print(f"  x  | f(x)| g(x)")
	print(f"-----------------")
	for i in range(len(x)):
		print(f"{x[i]:.3f}|{f(x)[i]:.3f}|{g(x)[i]:.3f}")


x = np.linspace(0,2*np.pi, num=1000)
print(f"  x  | f(x)| g(x)")
print(f"-----------------")
for i in range(10):
	print(f"{x[i]:.3f}|{f(x)[i]:.3f}|{g(x)[i]:.3f}")

if __name__=="__main__":
	main()