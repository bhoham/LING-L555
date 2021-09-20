import sys

text = sys.stdin.read()

for p in ['!','?','.',',','(',')','"',]:
	text = text.replace(p, ' ' + p + ' ')

text = text.replace(' ','\n')

print(text)