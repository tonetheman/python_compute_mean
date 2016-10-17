
# straight forward first
a= [1,2,3,4,5]

# this is how I would do it
def mean1(a):
	total = 0.0
	for num in a:
		total = total + num
	return total/len(a)*1.0

# this uses array indexing
def mean13(a):
	total = 0
	for i in range(len(a)):
		total = total + a[i]
	return total/len(a) * 1.0

# a stinky while loop
def mean9(a):
	index = 0
	total = 0
	while index<len(a):
		total = total + a[index]
		index = index + 1
	return total/len(a)*1.0
