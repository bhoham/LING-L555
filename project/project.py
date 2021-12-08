#creates a model of the deck with each card (2-10 or AKQJ representing the value, c,d,s, or h representing the suit)
deck = []
for x in range(2,11):
	deck.append(str(x)+'c')
	deck.append(str(x)+'d')
	deck.append(str(x)+'s')
	deck.append(str(x)+'h')
facecards = ['J', 'Q', 'K', 'A']
for x in facecards:
	deck.append(x+'c')
	deck.append(x+'d')
	deck.append(x+'s')
	deck.append(x+'h')

herowins = 0
totalsimulations = 0

heroshand = ['2d','2c','2s','5h','5h']

villainshand = ['3s','4s', '5s', '6s', '7s']

showdownhand = []

for x in heroshand:
	if x in villainshand:
		print("Not a possible combination, hero and villain can't both have the exact same card!")


def is_straight(s):
	straight = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	cardnumber = {}
	for x in range(2,11):
		cardnumber[x] = x
	facecardorder = 10
	for x in facecards:
		facecardorder = facecardorder + 1
		cardnumber[x] = facecardorder		
	firstcard = min(showdowncardnumbers)
	for x in range (1,5):
		nextcard = firstcard + x
		if nextcard not in showdowncardnumbers:
			continue
		straight = True
	return straight


if is_straight(heroshand) == True:
	print(fuck)

def is_flush(s):
	flush = False
	showdowncardsuits = []
	for x in showdownhand:
		x = list(x)[-1]
		showdowncardsuits.append(x)
	for x in range(1,5):
		if showdowncardsuits[0] != showdowncardsuits[x]:
			continue
		else:
			flush = True
	return flush

def is_straightflush(s):
	straightflush = False
	if is_flush(s) == True:
		if is_straight(s) == True:
			straightflush = True
	return straightflush


def is_quads(s):
	quads = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	showdownhandcardcounts = {}
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	for x in showdownhandcardcounts:
		if showdownhandcardcounts[x] == 4:
			quads = True
		else: 
			continue
	return quads

def is_fullhouse(s):
	fullhouse = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	showdownhandcardcounts = {}
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	if len(showdownhandcardcounts) == 2:
		for x in showdownhandcardcounts:
			if showdownhandcardcounts[x] != 1 or 4:
				fullhouse = True
	return fullhouse


def is_trips(s):
	trips = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	showdownhandcardcounts = {}
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	if is_fullhouse(s) == False:
		for x in showdownhandcardcounts:
			if showdownhandcardcounts[x] == 3:
				trips = True
			else: 
				continue
	return trips

def is_twopair(s):
	twopair = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	showdownhandcardcounts = {}
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	if is_trips(s) == False:
		if len(showdownhandcardcounts) == 3:
			twopair = True
	return twopair

def is_onepair(s):
	onepair = False
	showdowncardnumbers = []
	for x in showdownhand:
		x = x.replace('c','')
		x = x.replace('d','')
		x = x.replace('h','')
		x = x.replace('s','')
		x = int(x)
		showdowncardnumbers.append(x)
	showdownhandcardcounts = {}
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	if len(showdownhandcardcounts) == 4:
		onepair = True
	return onepair
def is_highcard(s):
	highcard = False
	if is_quads == False:
		if is_flush == False:
			if is_fullhouse == False:
				if is_straight == False:
					if is_trips == False:
						if is_twopair == False:
							if is_onepair == False:
								highcard = True
	return highcard

showdownhand = heroshand
if is_quads(heroshand) == True:
	heroshandclass = 1
if is_fullhouse(heroshand) == True:
	heroshandclass = 3
if is_flush(heroshand) == True:
	heroshandclass = 4
if is_straight(heroshand) == True:
	heroshandclass = 5
if is_straightflush(heroshand) == True:
	heroshandclass = 2
if is_trips(heroshand) == True:
	heroshandclass = 6
if is_twopair(heroshand) == True:
	heroshandclass = 7
if is_onepair(heroshand) == True:
	heroshandclass = 8
if is_highcard(heroshand) == True:
	heroshandclass = 9
print(heroshandclass)
""""
villainshand = showdownhand
if x is straightflush:
	villainshandclass = 0
if x is quads:
	villainshandclass = 1
if x is fullhouse:
	villainshandclass = 2
if x is flush:
	villainshandclass = 3
if x is straight:
	villainshandclass = 4
if x is trips:
	villainshandclass = 5
if x is twopair:
	villainshandclass = 6
if x is onepair:
	villainshandclass = 7
else:
	villainshandclass = 8
if heroshandclass >= villainshandclass:
	herowins = herowins + 1
	totalsimulations = totalsimulations + 1
if heroshandclass <= villainshandclass:
	totalsimulations = totalsimulations + 1
##if heroshandclass == villainshandclass:
		##this is gonna be way harder
		#simple high card function - good for flush, straightflush, straight, high card
		#find same cards make matrix and find highest in matrix - quads, fullhouse, trips, twopair, onepair
"""
def is_highcardvalue(s):
	heroshand = showdownhand
	heroshandcounts = showdownhandcardcounts
	heroshand.sort(reverse=True)
	villainshand = showdownhand
	villainshandcounts = showdownhandcardcounts
	heroshand.sort(reverse=True)
	###PUT A PRINT STATEMENT HERE TO TEST THIS OUT??
	for x in range(0,5):
		if heroshand[x] <= villainshand[x]:
			herowins = herowins + 1
			totalsimulations = totalsimulations + 1
			continue
		if heroshand[x] >= villainshand[x]:
			totalsimulations = totalsimulations + 1
			continue
	if heroshand[4] == villainshand [4]:
			herowins = herowins + .5
			totalsimulations = totalsimulations + 1




