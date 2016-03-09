from itertools import permutations

fi = open("data file","r")

data = fi.readlines()
seqData = []
fi.close()
seqData.append(data)

for line in seqData:
    if line.startswith('>'):
        del seqData[line]

resultList = [[]]
motifs = []

def powerset(items):#standard function to find the powerset
        global resultList
        for i in items:
            new = [r+[i] for r in resultList]
            resultList.extend(new)
        return resultList

def longestCommonSubStr(seqData):
    seq1 = seqData[0]
    seq2 = seqData[1]
    powerset(seq1)
    for element in resultList:
      if element in seq2:
        motifs.append(element)
  
  print(motifs)
  
  currentLongestMotif = ''
  for i in seqData:
      for j in motifs:
         if j in i:
            ####have to find some way of checking if its longer than the previous one and keeping an updated
            #counter on the longest motif across the strings
    
