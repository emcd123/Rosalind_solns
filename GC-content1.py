x = input().upper()
x = x.strip()
total = len(x)
print(total)
c = x.count("C")
g= x.count("G")

gc_tot = g+c

gc_content = gc_tot/total

print(gc_content)
