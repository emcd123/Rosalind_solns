import itertools
n = int(input())
def geneOrder(n):
	seq = [] 
	for i in range(1,n+1):
		seq.append(i)
		seq.append(i*-1)
	print(seq)
	length = len(seq)


geneOrder(n)
