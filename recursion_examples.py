
#recursion

def mean11(a):
	def _mean11(a,acc):
		if len(a)==0:
			return acc
		acc = acc + a[0]
		return _mean11(a[1:],acc)
	return 	_mean11(a,0)/len(a)*1.0
