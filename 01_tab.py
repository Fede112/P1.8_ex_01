import sys
import matplotlib.pyplot as plt
import numpy as np

if (len(sys.argv)!=2):
	print("Error: only one integer argument expected!")
	print("Usage: ")
	print("1: f(x)=x*")
	print("2: f(x)=x**2")
	print("3: f(x)=x**3")
	print("4: f(x)=sin(x)")
	print("5: f(x)=cos(x)")
	print("6: f(x)=tan(x)")
	exit(1)

ind = int(sys.argv[1])

def f1(x):
	return x
def f2(x):
	return x*x
def f3(x):
	return x*x*x

funcList = [f1, f2, f3, np.sin, np.cos, np.tan]

xval = [ (i*0.1 - 0.5) for i in range(0,11) ]
yval = [ funcList[ind-1](x) for x in xval ]

plt.plot(xval,yval)
plt.xlim(-0.3,0.3)
plt.show()
