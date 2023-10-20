import numpy as np

x = 1.0  #define a float
y = 2.0  #define another float

#exponenets and logs
print(f"np.exp({x}) = {np.exp(x)}") #exp(x)
print(f"np.log({x}) = {np.log(x)}") #log(x)
print(f"np.log10({x}) = {np.log10(x)}") #log10(x)
print(f"np.log2({x}) = {np.log2(x)}") #log2(x)

#min/max/misc functions
x = -1.0
print(f"np,fabs({x}) = {np.fabs(x)}") #absolute val as float
print(f"np,fmin({x},{y}) = {np.fmin(x,y)}") #min value of x and y
print(f"np,fmax({x},{y}) = {np.fmax(x,y)}") #max of x and y

#populate arrays
n = 100   #define an int
z = np.arange(n,dtype=float)   #get an array[0.0,n-1.]
z *= 2.0*np.pi / float(n-1)    #z = [0,2.*pi]
sin_z = np.sin(z)              #get an array sin(z)

#interpolation
print(f"our interpolated value of sin(0.75) = {np.interp(0.75,z,sin_z)}.")
print(f"Actual value of sin(0.75) = {np.sin(0.75)}.")