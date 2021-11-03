import sys

text = sys.stdin.read()

#creates a dictionary that maps words to their part of speech tag from the language model
word2pos = {}
#makes a frequency variable to find the most common pos
freq = 0 

#opens the language model and breaks each row into parts
model = open('model.tsv','r')
for line in model:
	line = line.strip('\n')
	line = line.split('\t')
	word = line[3]
	POS = line[2]
	#goes through the first few rows that rank frequency of each pos and finds the most frequent one
	if word == '_':
		if float(line[0]) > float(freq):
			freq = line[0]
			freqpos = POS
			continue
		else:
			continue
	#ignores the label row
	if word == 'form':
		continue
	#adds in new words to the dictionary
	if word not in word2pos:
		word2pos[word] = POS


#finds the correct lines by splitting off non tabbed and too short ones 
for line in text.split('\n'):
	if '\t' not in line:
		print(line)
		continue
	row = line.split('\t')
	if len(row) != 10:
		print(line)
		continue
	#separates words from the rest of their lines
	word = row[1]
	#fills in the pos to the word if the pos is known
	if word in word2pos:
		row[3] = word2pos[word]
	#fills in the most frequent pos if the pos of the word isn't in the model	
	else:
		row[3] = freqpos
	#rejoins and prints the row
	row = '\t'.join(row)
	print(row)
