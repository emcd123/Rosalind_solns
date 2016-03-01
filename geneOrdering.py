import itertools
n = int(input())
def geneOrder(n):
	seq = [] 
	for i in range(1,n+1):
		seq.append(i)
	seqList = map(list,list(itertools.permutations(seq,n)))
	resultSeqList = []
	for i in seqList:
		signalFlag=1
		for j in i:
			if ((j in i) & ((j*-1) in i)):
                    signalFlag = 1
                    break
            if signalFlag == 0:
                    resultSeqList.append(i)

	print(len(resultSeqList))
	for i in resultSeqList:
		print(' '.join(map(str,i)))


geneOrder(n)
