import sys
import matplotlib.pyplot as plt
import numpy as np

if (len(sys.argv)!=2):
	print("Error: wrong number of arguments!")
	exit(1)

idx = int(sys.argv[1])

def f1(x):
	return x

funcList = [f1, np.sin, np.cos, np.tan]

xval = [ (i*0.1 - 0.5) for i in range(0,11) ]
yval = [funcList[idx-1](x) for x in xval]

print(xval)
print(yval)

plt.plot(xval,yval)
plt.show()
