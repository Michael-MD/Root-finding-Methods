import numpy as np
import matplotlib.pyplot as plt

#interval
xn2 = 5
xn1 = 7

epsilon = 0.0000000001	#accuracy

def f(x):	#function
	return np.sin(x)


def c():	#next point
	#next point is root of line connecting points (a,f(a)) and (b,f(b))
	return (xn1 - f(xn1)*( (xn1 - xn2) / (f(xn1)-f(xn2)) ))


while abs(f(xn1)) > epsilon:
	temp = c()
	xn2 = xn1
	xn1 = temp



print(xn1)

plt.figure()

x = np.linspace(-10,10,50)
y = f(x)

plt.plot(x,y)
plt.plot(c(),f(c()),'ro')
plt.show()