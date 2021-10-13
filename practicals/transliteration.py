import sys

text = sys.stdin.read()

#creates a dictionary to read in latin to yiddish letters
trans = {}

#opens and reads a text document thats the transliteration key 
#and creates a dictionary from the list of latin and yiddish letters
dict = open('transliteration.txt','r')
for line in dict:
	line = line.strip('\n')
	parts = line.split('\t')
	latin = parts[0] 
	yiddish = parts[1]
	trans[latin] = yiddish

#finds the correct lines by splitting off non tabbed and too shortones 
for line in text.split('\n'):
	if '\t' not in line:
		print(line)
		continue
	row = line.split('\t')
	if len(row) != 10:
		print(line)
		continue
	#separates words from the rest of their lines
	word = row[1].lower()
	#adds #s to differentiate the start and end of words
	word = '#' + word + '#'
	#replaces the latin charaters for yiddish ones and removes the #s
	for x in trans:
		word = word.replace(x,trans[x])
		word = word.strip('#')
	row[9] = 'yiddish='+word
	print('\t'.join(row))