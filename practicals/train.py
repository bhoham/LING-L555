import sys

text = sys.stdin.read()
wordcounter = {}
poscounter = {}
wordtagmatrix = {}
wordtagmatrixcount = {}
tokencounter = 0 

for line in text.split('\n'):
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	word = row[1]
	POS = row[3]
	if word not in wordcounter:
		wordcounter[word] = 0
	if POS not in poscounter:
		poscounter[POS] = 0
	wordtagmatrix[word] = POS
	wordcounter[word] = wordcounter[word] + 1
	poscounter[POS] = poscounter[POS] + 1
	tokencounter = tokencounter + 1
wordposcombolist = []
for word in wordtagmatrix:
	wordposcombo = word + ' ' + wordtagmatrix[word]
	wordposcombolist.append(wordposcombo)
for wordposcombo in wordposcombolist:
	if wordposcombo not in wordtagmatrixcount:
		wordtagmatrixcount[wordposcombo] = 0
	wordtagmatrixcount[wordposcombo] = wordtagmatrixcount[wordposcombo] + 1


print('# P\tcount\ttag\tform')
for POS in poscounter:
	print(str(poscounter[POS]/tokencounter) + '\t'+ str(poscounter[POS]) + '\t' + POS + '\t_')
for word in wordtagmatrixcount:
	splitword = word.split(' ')[0] 
	if splitword in wordcounter:
		wordnumber = wordcounter[splitword]
		print(str(wordtagmatrixcount[word]/wordnumber)+'\t'+str(wordtagmatrixcount[word])+'\t'+word.split(' ')[1]+'\t'+splitword)