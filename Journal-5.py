import numpy as np

def main():
	x = np.linspace(0,2*np.pi, num=1000)
	sinx = np.sin(x)

	print("  x | sin(x)")
	print("--------")

	for i  in range(len(x)):
		print(f"{x[i]:.3f}|{sinx[i]:.3f}")


if __name__=="__main__":
	main()