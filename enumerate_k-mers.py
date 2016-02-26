
import itertools
n = input()
size = input()
def kmers(n,size):
	formatN = n.replace(" ","")
	list_enu =([x for x in itertools.product(formatN, repeat=size)]) 
	for i in list_enu:
		print("".join(map(str, i)))

kmers(n,size)
