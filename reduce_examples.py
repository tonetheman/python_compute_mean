
a= [1,2,3,4,5]

# reduce !!!!

def mean2(a):
	from operator import add
	return reduce(add,a)/len(a)*1.0

def mean4(a):
	return reduce(lambda x,y: x+y,a)/len(a)*1.0

# another built in on int i did not know about
def mean5(a):
	return reduce(int.__add__,a)/len(a)*1.0
