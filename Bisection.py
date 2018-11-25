import numpy as np
import matplotlib.pyplot as plt

#interval
a = 5
b = 10

epsilon = 0.0000000001	#accuracy

def f(x):	#function
	return np.sin(x)+np.cos(x)


def c():	#midpoint
	return (a+b)/2



while abs(f(c())) > epsilon:	#if we haven't met the required accuracy
	if f(c()) > 0:
		if f(a) > 0:
			a = c()
		else:
			b = c()
	else:
		if f(a) < 0:
			a = c()
		else:
			b = c()
	


print(c())


plt.figure()

x = np.linspace(-10,10,50)
y = f(x)

plt.plot(x,y)
plt.plot(c(),f(c()),'ro')
plt.show()