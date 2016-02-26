
dna_1 = list(input())
dna_2 = list(input())
#print(len(dna_2)," ",len(dna_2))
li = (set(dna_1).intersection(dna_2))
li = list(li)
new_list=[]
#for i in dna_1:
 #   if i in dna_2:
  #      new_list.append(i)
print(len(li))
