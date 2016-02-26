
complement={'A': 'T', 'T':'A','C':'G','G':'C'}
Dna_str = input()
reverse_complement = "".join(complement.get(base,base) for base in reversed(Dna_str))
print(reverse_complement)
