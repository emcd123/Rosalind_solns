seq = open("rosalind_dna.txt", "r")
strseq = seq.read()
Dna_seq = list(strseq)

countA = Dna_seq.count("A")
countG = Dna_seq.count("C")
countC = Dna_seq.count("G")
countT = Dna_seq.count("T")

print(countA,countC,countG,countT)
