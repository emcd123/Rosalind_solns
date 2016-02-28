import itertools
n = int(input())#integer number ,given
def geneOrder(n):
        seq = []
        for i in range(1,n+1):
            seq.append(i)
            seq.append(i*-1)#add numbers to list and negative counterparts
        seqList = map(list,list(itertools.permutations(seq,n)))#create a list of lists of the permuntations
        resultSeqList = []
        for i in seqList:
            errorCatch =0#like a signal to program on whether to append to list or not,removes unwanted permutations
            for j in i:
                if ((j in i) & ((j*-1) in i)):
                    errorCatch = 1
                    break
            if errorCatch == 0:
                    resultSeqList.append(i)
    
        #create the correct format for answering
        #go through the list to print on idvidual lines
        #join the list together at the spaces 
        # use C function map to convert all the elements from lists to strings
        print(len(resultSeqList))
        for i in resultSeqList:
            print(' '.join(map(str,i)))


geneOrder(n)
