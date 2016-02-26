data = [19221,17901,18348,17689,16607,17552]
modData = []
#sum=[]
average = []
for i in data:
    Data = i*2
    modData.append(Data)
print(modData)

#for i in modData:
#    sum += i
#print(sum)

for j in range(0,len(modData)): 
    if j == 0:
        average.append(modData[j]*(1))
    if j == 1:
        average.append(modData[j]*(1))
    if j == 2:
        average.append(modData[j]*(1))
    if j == 3:
        average.append(modData[j]*(3/4.0))
    #print(average)
    if j == 4:
        average.append(modData[j]*(1/2.0))
    if j == 5:
        average.append(0)
    #else:
     #   average += modData[j]*1
print(sum(average))
