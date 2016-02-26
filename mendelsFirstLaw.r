library(combinat)
n=23#recessive
k=30#dominant
m=27#hetero
#hetero is Yy,dominant is YY,recessive is yy
# hetro and recessive mating
#YY,Yy,yY,yy if even one dominant then shows trait so 1/4 is recessive

#heterozygous and passive mating is 1/2
#Yy yy yy Yy 

z = n+k+m#total of organisms
reccessiveMates = (n/z) * ((n-1)/(z-1))#without replacement ,so probability changes
heteroMates = (m/z) * ((m-1)/(z-1))
recessiveHetero = (m/z)*(n/(z-1)) + (n/z)*(m/(z-1))
notDominant = reccessiveMates + (heteroMates * (1/4)) + (recessiveHetero*(1/2))
pDominant = 1-notDominant#basic probability