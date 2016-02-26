fi = open("data.txt","r")
lines= fi.read().strip()
for i in lines:
	if i == "/n":
		lines = lines.split("/n")
print(lines)
for v in lines[:lines.index("/n")]:
	if lines[v] == (lines.index("/n")+lines[v])
