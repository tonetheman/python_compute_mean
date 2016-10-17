
a= [1,2,3,4,5]

# this is how I would do it
def mean1(a):
	total = 0.0
	for num in a:
		total = total + num
	return total/len(a)*1.0

# another way using reduce and operator
def mean2(a):
	from operator import add
	return reduce(add,a)/len(a)*1.0

# there is a built in called sum who knew?
def mean3(a):
	return sum(a)/len(a)*1.0

# lambda version
def mean4(a):
	return reduce(lambda x,y: x+y,a)/len(a)*1.0

# another built in on int i did not know about
def mean5(a):
	return reduce(int.__add__,a)/len(a)*1.0

# wut?
def mean6(a):
	P = []
	for j in [0]:
		for i in a:
			for j in [j+i]:
				P.append(j)
	return P[-1]/len(a)*1.0

# one liner version of 6 really
def mean7(a):
	return [j for j in [0] for i in a for j in [j+i]][-1]/len(a)*1.0

# added this one cause it is better on the denom
def mean8(a):
	return sum(a)/max(len(a),1)*1.0

# with a while loop
def mean9(a):
	index = 0
	total = 0
	while index<len(a):
		total = total + a[index]
		index = index + 1
	return total/len(a)*1.0

# with a range part2
def mean10(a):
	total = 0
	for i in range(len(a)):
		total = total + a[i]
	return total/len(a)*1.0

# with recursion and inner function and accumlator
def mean11(a):
	def _mean11(a,acc):
		if len(a)==0:
			return acc
		acc = acc + a[0]
		return _mean11(a[1:],acc)
	return 	_mean11(a,0)/len(a)*1.0

def mean12(a):
	def _mean12(a):
		if len(a)==1:
			return a[0]
		else:
			return a[0] + mean12(a[1:])
	return _mean12(a)/len(a) * 1.0

def mean13(a):
	total = 0
	for i in range(len(a)):
		total = total + a[i]
	return total/len(a) * 1.0

print "mean1", mean1(a)
print "mean2", mean2(a)
print "mean3", mean3(a)
print "mean4", mean4(a)
print "mean5", mean5(a)
print "mean6", mean6(a)
print "mean7", mean7(a)
print "mean8", mean8(a)
print "mean9", mean9(a)
print "mean10", mean10(a)
print "mean11", mean11(a)
print "mean12", mean12(a)
print "mean13", mean13(a)
