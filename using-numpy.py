import numpy as np

x = 1.0 #define a float
y = 2.0 #define another float

#trig
print(f"np.sin({x}) = {np.sin(x)}") #sinx
print(f"np.cos({x}) = {np.cos(x)}") #cosx
print(f"np.tan({x}) = {np.tan(x)}") #tanx
print(f"np.arcsin({x}) = {np.arcsin(x)}") #arcsinx
print(f"np.arccos({x}) = {np.arccos(x)}") #arccosx
print(f"np.arctan({x}) = {np.arctan(x)}") #arctanx
print(f"np.arctan2({x},{y}) = {np.arctan2(x,y)}") #arctan(x/y)
print(f"np.rad2deg({x}) = {np.rad2deg(x)}") #convert rad to deg

#hyperbolic functions
print(f"np.sinh({x}) = {np.sinh(x)}") #trigfunc (x)
print(f"np.cosh({x}) = {np.cosh(x)}")
print(f"np.tanh({x}) = {np.tanh(x)}")
print(f"np.arcsinh({x}) = {np.arcsinh(x)}")
print(f"np.arccosh({x}) = {np.arccosh(x)}")
print(f"np.arctanh({x}) = {np.arctanh(x)}")