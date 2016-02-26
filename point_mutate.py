def hamm(str1, str2):
	#2 equal length strings, find #of mismatches in them

	mutations = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			mutations +=1
	return mutations
