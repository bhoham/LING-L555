import sys

#creates matrices for the count of each word, each pos, each word to tag, and the count of each tag for each word, and creates a counter for the total number of tokens.
text = sys.stdin.read()
wordcounter = {}
poscounter = {}
wordtagmatrix = {}
wordtagmatrixcount = {}
tokencounter = 0 

#splits up text and looks for the ones separated by tabs, splitting them by tab
for line in text.split('\n'):
	if '\t' not in line:
		continue
	row = line.split('\t')
	#ignores rows that are two short
	if len(row) != 10:
		continue
	#finds the word and part of speech from the file
	word = row[1]
	POS = row[3]
	#adds words and pos's to dictionaries counting the number of each one
	if word not in wordcounter:
		wordcounter[word] = 0
	if POS not in poscounter:
		poscounter[POS] = 0
	#creates a nested dictionary for each word
	if word not in wordtagmatrix:
		wordtagmatrix[word] = {}
	#adds the part of speech of each word in the matrix and a counter value
	if POS not in wordtagmatrix[word]:
		wordtagmatrix[word][POS] = 0
	#adds one to each count being taken
	wordtagmatrix[word][POS]+=1
	wordcounter[word] += 1
	poscounter[POS] += 1
	tokencounter+= 1
#prints label
print('# P\tcount\ttag\tform')
#prints out the counts for each POS as well as their relative frequency
for POS in poscounter:
	print('%.5f'%(poscounter[POS]/tokencounter)+'\t'+ str(poscounter[POS]) + '\t' + POS + '\t_')
#prints out each word in its uses as different parts of speech separately, showing the relative frequency of its use in that way and its overall count
for word in wordtagmatrix:
	for POS in wordtagmatrix[word]:
		print('%.5f'%(wordtagmatrix[word][POS]/wordcounter[word])+'\t'+str(wordcounter[word]) + '\t'+((str(wordtagmatrix[word].keys())).strip("dict_keys(['")).strip("'])")+'\t'+word)
