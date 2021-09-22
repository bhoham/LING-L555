import sys

text = sys.stdin.read()


for p in ['!','?','.',',','(',')','"',]:
	text = text.replace(p, ' ' + p + ' ')

sent_id = 0

text = text.split('\n')

for line in text:
	sent_id = sent_id + 1
	print('\n # sent_id = ' + str(sent_id))
	print('# text = ' + line)
	tokens= line.split(' ')
	token_id=0
	for token in tokens:
		token_id = token_id + 1
		print(str(token_id) + "\t" + token + '_\t_\t_\t_\t_\t_\t_\t_\t')
