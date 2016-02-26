
seq = input().upper()

def GC(seq):
	count = 0 
	total = len(seq)
	for i in seq:
		if i == "G" or i == "C":
			count += 1
	print((count/total)*100)
GC(seq) 
