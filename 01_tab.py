import sys

if (len(sys.argv)!=2):
	print("Error: wrong number of arguments!")
	exit(1)

# print(sys.argv[1])

def f(x):
	return x*x

xval = [ (i*0.1 - 0.5) for i in range(0,11) ]
yval = [f(x) for x in xval]

print(xval)
print(yval)