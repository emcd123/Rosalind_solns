
seq = input().upper()
motif = input().upper()
def dnaMotif(seq,motif):
	n = len(motif)
	result = []
	for i in range(0,len(seq)):#loop through the sequence
		if motif in [seq[i:i+n]]:#if motif matches  list of seq of length motif, append result with index of sequence where motif starts
			result.append(i+1)
	print(li)

dnaMotif(seq,motif)
