import sys
import matplotlib.pyplot as plt
import numpy as np

if (len(sys.argv)!=2):
	print("Error: only one integer argument expected!")
	print("Usage: ")
	print("1: f(x)=x**2")
	exit(1)

ind = int(sys.argv[1])

def f1(x):
	return x

funcList = [f1, np.sin, np.cos, np.tan]

funcList = [f2]

xval = [ (i*0.1 - 0.5) for i in range(0,11) ]
yval = [ funcList[ind-1](x) for x in xval ]

plt.plot(xval,yval)
plt.show()
