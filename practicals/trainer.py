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
	if word not in wordtagmatrix:
		wordtagmatrix[word] = {}
	if POS not in wordtagmatrix[word]:
		wordtagmatrix[word][POS] = 0
	wordtagmatrix[word][POS]+=1
	wordcounter[word] += 1
	poscounter[POS] += 1
	tokencounter+= 1
print('# P\tcount\ttag\tform')
for POS in poscounter:
	print('%.5f'%(poscounter[POS]/tokencounter)+'\t'+ str(poscounter[POS]) + '\t' + POS + '\t_')
for word in wordtagmatrix:
	for POS in wordtagmatrix[word]:
		print('%.5f'%(wordtagmatrix[word][POS]/wordcounter[word])+'\t'+str(wordcounter[word]) + '\t'+((str(wordtagmatrix[word].keys())).strip("dict_keys(['")).strip("'])")+'\t'+word)
