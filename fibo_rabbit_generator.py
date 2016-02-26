def fibnumber(n, k):
	a, b = 1, 1
	for i in range(2, n ):
		a, b = b, k*a+b
	return b


#this example you can use the true value of n. 

#this is way faster than recursion
		
