import sys

#reads in the segmented text
text = sys.stdin.read()

#adds in spaces to punctuation so they will be read as separate words
for p in ['!','?','.',',','(',')','"',]:
	text = text.replace(p, ' ' + p + ' ')

#creates a counter variable for sentence id
sent_id = 0

#makes the text a list so it can be read line by line
text = text.split('\n')

#prints out each line, and each words, giving out the number for each
for line in text:
	sent_id = sent_id + 1
	print('\n # sent_id = ' + str(sent_id))
	print('# text = ' + line)
	tokens= line.split(' ')
	token_id=0
	for token in tokens:
		token_id = token_id + 1
		print(str(token_id) + "\t" + token + '\t_\t_\t_\t_\t_\t_\t_\t_\t')
