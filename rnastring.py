import string
seq = open("rosalind_rna.txt", "r")
strseq = list(seq)
Dna_seq = str(strseq)
replacement = str.replace(Dna_seq, "T", "U")
print(replacement)


#in the following ways, the sequence is inputed as a sring rather than from a file
#or
#dna= input()
#print(dna.replace("T","U"))

#could also use functional way
# def transcribe(sequence)
#   return sequence.replace("T","U")
    
