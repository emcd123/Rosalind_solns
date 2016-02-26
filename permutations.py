
def permutations(n):
	fact =1
	for i in range(1,n+1):
		fact = fact*i
	return fact

def perm_generate(n):
        import itertools
        z = itertools.permutations(range(n))
        li = list(z)
        
        
