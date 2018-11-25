import numpy as np
import matplotlib.pyplot as plt

#interval
xn = 6

epsilon = 0.0000000001	#accuracy

def f(x):	#function
	return np.sin(x)

def df(x):
	return np.cos(x)

	

def c():	#next point
	#next point is root of line connecting points (a,f(a)) and (b,f(b))
	return (xn - (f(xn)/df(xn)))

while abs(f(xn)) > epsilon:
	xn1 = c()
	xn = xn1

print(xn)

plt.figure()

x = np.linspace(-10,10,50)
y = f(x)

plt.plot(x,y)
plt.plot(c(),f(c()),'ro')
plt.show()