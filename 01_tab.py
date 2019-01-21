import sys
import matplotlib.pyplot as plt

if (len(sys.argv)!=2):
	print("Error: wrong number of arguments!")
	exit(1)

ind = int(sys.argv[1])

# print(sys.argv[1])

def f1(x):
	return x
def f2(x):
	return x*x
def f3(x):
	return x*x*x

funcList = [f1,f2,f3]



xval = [ (i*0.1 - 0.5) for i in range(0,11) ]
yval = [funcList[ind - 1](x) for x in xval]

print(xval)
print(yval)

plt.plot(xval,yval)
plt.show()
