import numpy as np
import matplotlib.pyplot as plt

#interval
a = 8
b = 10

epsilon = 0.0000000001	#accuracy

def f(x):	#function
	return np.sin(x)+np.cos(x)


def c():	#next point
	#next point is root of line connecting points (a,f(a)) and (b,f(b))
	return (f(b)*a - f(a)*b)/(f(b)-f(a))

while abs(f(c())) > epsilon:	#if required accuracy isn't met
	print(a,b)
	if f(c()) < 0:
		if f(a) > 0:
			a = c()
		else:
			b = c()
	else:
		if f(a) > 0:
			a = c()
		else:
			b = c()


print(f(c()))

plt.figure()

x = np.linspace(-10,10,50)
y = f(x)

plt.plot(x,y)
plt.plot(c(),f(c()),'ro')
plt.show()