def fibnum(n, k):
	if n is 0 or n is 1:
		return 1
	else:
		return(fibnum(n-1, k) +k *fibnum(n-2, k))

#this is a recursive function
#will work for n<40 and k<5
#for any n you want to find you must minus 1 from it here in this code


#this is a multinacci sequence!
