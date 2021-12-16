#imports a library that is useful later in letting us sort the card count matrix by the value and key figuring out which hand has high card value
import operator

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

#defines variables that allow the probability of the player (hero) making the better hand to be calculated
herowins = 0
totalsimulations = 0
#defines the full or partial hands the user assigns to themselves and their opponent - if a given card is unknown a player can input x instead and the program will calculate possible outcomes
heroshand = ['5c','4c','4d','2h','x']
villainshand = ['5d','4h','4s','2c','2s']
#lets the user input any cards they know to be out of play such as discarded cards and removes them from the deck 
deadcards = []
for x in deck:
	if x in deadcards:
		deck.remove(x)

#sends an error message if the user gives hero and villain the exact same card
for x in heroshand:
		if x in villainshand:
			print("Not a possible combination, hero and villain can't both have the exact same card!")

#removes cards in hands from deck so the draw can be simulated later on (not sure why but only works right with two separate loops)
for x in deck:
	if x in villainshand:
		deck.remove(x)
for x in deck:
	if x in heroshand:
		deck.remove(x)	

#separates the numberical value of the cards from the suit - this lets us check for full houses, pairs, etc
def handcardnumbers(showdownhand):
	numberoutput = []
	for x in range(0,5):
		#removes the suit information and makes the facecards into numbers for each card in the hand and outputs a new list with only that information
		givencard = showdownhand[x]
		givencard = str(givencard)
		givencard = givencard.replace('c','')
		givencard = givencard.replace('d','')
		givencard = givencard.replace('h','')
		givencard = givencard.replace('s','')
		givencard = givencard.replace('J','11')
		givencard = givencard.replace('Q','12')
		givencard = givencard.replace('K','13')
		givencard = givencard.replace('A','14')
		givencard = int(givencard)			
		numberoutput = numberoutput + [givencard]
	return numberoutput

#creates a matrix of card numbers to how many there are of them in a hand
def showdownhandcardcountsmatrix(showdownhand):
	showdownhandcardcounts = {}
	showdowncardnumbers = handcardnumbers(showdownhand)
	for x in showdowncardnumbers:
		if x not in showdownhandcardcounts:
			showdownhandcardcounts[x] = 0
		showdownhandcardcounts[x] = showdownhandcardcounts[x] + 1
	return showdownhandcardcounts
	
#creates a function to recognize if a hand is a straight 
def is_straight(showdownhand):
	straight = False
	showdowncardnumbers = handcardnumbers(showdownhand)
	#tests if all 5 cards are in a sequential order and therefore a straight
	firstcard = min(showdowncardnumbers)
	secondcard = firstcard + 1
	if secondcard in showdowncardnumbers:
		thirdcard = secondcard + 1
		if thirdcard in showdowncardnumbers:
			fourthcard = thirdcard + 1
			if fourthcard in showdowncardnumbers:
				fifthcard = fourthcard + 1
				if fifthcard in showdowncardnumbers:
					straight = True
	#for straights an Ace can be high or low - this covers the case where its low
	if sorted(showdowncardnumbers) == [2,3,4,5,14]:
		straight = True
	return straight

#creates a function to see if a hand is a flush
def is_flush(showdownhand):
	flush = False
	#removes hand value information just to see card suits
	showdowncardsuits = []
	for x in showdownhand:
		x = list(x)[-1]
		showdowncardsuits.append(x)
	#tests if all of the suits match
	firstcard = showdowncardsuits[0]
	secondcard = showdowncardsuits[1]
	if secondcard == firstcard:
		thirdcard = showdowncardsuits[2]
		if thirdcard == firstcard:
			fourthcard = showdowncardsuits[3]
			if fourthcard == firstcard:
				fifthcard = showdowncardsuits[4]
				if fifthcard == firstcard:
					flush = True
	return flush

#creates a function to see if a hand is a straight flush
def is_straightflush(showdownhand):
	straightflush = False
	if is_flush(showdownhand) == True:
		if is_straight(showdownhand) == True:
			straightflush = True
	return straightflush

#creates a function to see if a hand is four of a kind or 'quads'
def is_quads(showdownhand):
	quads = False
	#separates cards into purely their numerical values
	showdowncardnumbers = handcardnumbers(showdownhand)
	#checks if there are four of a kind
	showdownhandcardcounts = showdownhandcardcountsmatrix(showdownhand)
	for x in showdownhandcardcounts:
		if showdownhandcardcounts[x] == 4:
			quads = True
		else: 
			continue
	return quads

#creates a function to see if a hand is a full house
def is_fullhouse(showdownhand):
	fullhouse = False
	showdowncardnumbers = handcardnumbers(showdownhand)	
	showdownhandcardcounts = showdownhandcardcountsmatrix(showdownhand)
	#if a five card hand has only two values of cards it must either be a full house or four of a kind; this uses that to identify full houses
	if len(showdownhandcardcounts) == 2:
		if is_quads(showdownhand) == False:
				fullhouse = True
	return fullhouse

#creates a function to see if a hand is three of a kind 'trips'
def is_trips(showdownhand):
	trips = False
	showdowncardnumbers = handcardnumbers(showdownhand)	
	showdownhandcardcounts = showdownhandcardcountsmatrix(showdownhand)
	#since both full houses and trips contain 3 identical cards removing full houses from consideration lets us just search for three of a kind
	if is_fullhouse(showdownhand) == False:
		for x in showdownhandcardcounts:
			if showdownhandcardcounts[x] == 3:
				trips = True
			else: 
				continue
	return trips

#creates a function to spot two pair
def is_twopair(showdownhand):
	twopair = False
	showdowncardnumbers = handcardnumbers(showdownhand)	
	showdownhandcardcounts = showdownhandcardcountsmatrix(showdownhand)
	#in a 5 card hand the only ways for there to be only 3 different values are for there to be three of a kind or two pair - this eliminates three of a kind
	if is_trips(showdownhand) == False:
		if len(showdownhandcardcounts) == 3:
			twopair = True
	return twopair

#creates a function to identify one pair hands
def is_onepair(showdownhand):
	onepair = False
	showdowncardnumbers = handcardnumbers(showdownhand)
	showdownhandcardcounts = showdownhandcardcountsmatrix(showdownhand)
	#if number of different values is 4 exactly one should repeat making it a one pair hand
	if len(showdownhandcardcounts) == 4:
		onepair = True
	return onepair

#creates a function to identify which hand has higher cards in it if both are the same type of hand
def is_herohashighercards(heroshand, villainshand):
	herohashighercards = False
	heroshandcounts = showdownhandcardcountsmatrix(heroshand)
	heroshandcounts = sorted(heroshandcounts.items(), key=operator.itemgetter(1))
	villainshandcounts = showdownhandcardcountsmatrix(villainshand)
	villainshandcounts = sorted(villainshandcounts.items(), key=operator.itemgetter(1))
	#checks cards from highest to lowest to see if hero has a higher card - if the highest card is the same it moves on to the next one
	if heroshandcounts[-1][0] == villainshandcounts[-1][0]:
		if heroshandcounts[-2][0] == villainshandcounts[-2][0]:
			if len(heroshandcounts) >= 3:
				if heroshandcounts[-3][0] == villainshandcounts[-3][0]:
					if len(heroshandcounts) >= 4:
						if heroshandcounts[-4][0] == villainshandcounts[-4][0]:
							if len(heroshandcounts) >= 5:
								if heroshandcounts[-5][0] >= villainshandcounts[-5][0]:
									herohashighercards = True
						else:
							if heroshandcounts[-4][0] >= villainshandcounts[-4][0]:
								herohashighercards = True
				else:
					if heroshandcounts[-3][0] >= villainshandcounts[-3][0]:
						herohashighercards = True
		else:
			if heroshandcounts[-2][0] >= villainshandcounts[-2][0]:
				herohashighercards = True
	else:
		if heroshandcounts[-1][0] >= villainshandcounts[-1][0]:
			herohashighercards = True
	return herohashighercards

#creates a function to identify if hero and villlains hands tie - splitting the pot - this operates essentially the same way as is_herohashighercards() but checks if all 5 cards have the same value in each hand instead
def is_splitpot(heroshand, villainshand):
	splitpot = False
	heroshandcounts = showdownhandcardcountsmatrix(heroshand)
	heroshandcounts = sorted(heroshandcounts.items(), key=operator.itemgetter(1))
	villainshandcounts = showdownhandcardcountsmatrix(villainshand)
	villainshandcounts = sorted(villainshandcounts.items(), key=operator.itemgetter(1))
	if heroshandcounts[-1][0] == villainshandcounts[-1][0]:
		if heroshandcounts[-2][0] == villainshandcounts[-2][0]:
			if heroshandcounts[-3][0] == villainshandcounts[-3][0]:
				if len(heroshandcounts) == 3:
					splitpot = True
				else:
					if heroshandcounts[-4][0] == villainshandcounts[-4][0]:
						if len(heroshandcounts) == 4:
							splitpot = True	
						else:
							if heroshandcounts[-5][0] == villainshandcounts[-5][0]:
								splitpot = True
	return splitpot

#creates a function assigns a numerical value to both hero and villains hands by their type with higher numbers being better
def find_handclass(givenhand):
	#the default is 9 as that is simply "high card value" which is a type defined by not being any other
	handclass = 9
	if is_quads(givenhand) == True:
		handclass = 2
	if is_fullhouse(givenhand) == True:
		handclass = 3
	if is_flush(givenhand) == True:
		handclass = 4
	if is_straight(givenhand) == True:
		handclass = 5
	#straightflush is put after straight and flush to overwrite the previous values
	if is_straightflush(givenhand) == True:
		handclass = 1
	if is_trips(givenhand) == True:
		handclass = 6
	if is_twopair(givenhand) == True:
		handclass = 7
	if is_onepair(givenhand) == True:
		handclass = 8	
	return handclass

#creates a function to see if heros hand is the winning one by comparing hand classes/high card value
def does_hero_win(heroshand, villainshand):
	hero_win = False
	heroshandclass = find_handclass(heroshand)
	villainshandclass = find_handclass(villainshand)
	if heroshandclass >= villainshandclass:
		hero_win = True	
	if heroshandclass == villainshandclass:
		if is_herohashighercards(heroshand,villainshand) == False:
			if is_splitpot(heroshand,villainshand) == False:
				hero_win = True
	return hero_win

#creates a function that when x is input instead of a card it calculates all possible hands where remaining cards in the deck substitute x and puts it in a list of lists
def find_possible_hands(givenhand):
	possible_hands = []
	#this identifies if x is in the hand
	if 'x' in givenhand:
		#for every card in the deck this creates a possible hand for the first iteration of x
		for card1 in deck:	
			possiblehand = [] + givenhand
			possiblehand.remove('x')
			possiblehand.append(card1)
			possible_hands.append(possiblehand)
			#if more than one card is unknown this loops again to see all the possibilies for the second card given the first
			if 'x' in possiblehand:
				for card2 in deck:
					possiblehand_squared = [] + possiblehand
					possiblehand_squared.append(card2)
					possiblehand_squared.remove('x')
					possible_hands.append(possiblehand_squared)
					#there are three more loops of this so it is hypothetically possible but not reccomended to calculate all possible hands for all 5 cards
					if 'x' in possiblehand_squared:
						for card3 in deck:
							possiblehand_cubed = [] + possiblehand_squared
							possiblehand_cubed.append(card3)
							possiblehand_cubed.remove('x')
							possible_hands.append(possiblehand_cubed)
							if 'x' in possiblehand_cubed:
								for card4 in deck:
									possiblehand_4thpwr = [] + possiblehand_cubed
									possiblehand_4thpwr.append(card4)
									possiblehand_4thpwr.remove('x')
									possible_hands.append(possiblehand_4thpwr)
									if 'x' in possiblehand_4thpwr:
										for card5 in deck:
											possiblehand_5thpwr = [] + possiblehand_4thpwr
											possiblehand_5thpwr.append(card5)
											possiblehand_5thpwr.remove('x')
											possible_hands.append(possiblehand_5thpwr)		
		#creates a copy of the list of possible hands to loop over and remove any hands that contain cards that reoccur twice or still have x in them
		copyofpossible_hands = [] + possible_hands
		for x in copyofpossible_hands:
			if 'x' in x:
				possible_hands.remove(x)
		for x in copyofpossible_hands:
			for z in range(0,4):
				for y in range(z+1,5):
					if x[z] == x[y]:
						if x in possible_hands:
							possible_hands.remove(x)
	#makes the list of possible hands only one entry if x is not in the hand
	else:
		possible_hands.append(givenhand)
	return possible_hands

#creates a matrix of all possible combinations of heros hand and villains hand
possible_showdowns = {}
for x in find_possible_hands(heroshand):
	villains_possible_hands = find_possible_hands(villainshand)
	#loops through villains possible hands and removes possible combinations where hero and villain have the same card in their hand
	for y in x:
		for z in villains_possible_hands:
			if y in z:
				if z in villains_possible_hands:
					villains_possible_hands.remove(z)
	#makes heros hand a string so it can be put into the matrix - this gets corrected for later
	x = str(x)
	possible_showdowns[x] = villains_possible_hands

#goes through the possible showdown matrix and counts how many times hero wins and how many pairings there are to calculate heros win percentage
for x in possible_showdowns:
	#turns heros hand back into a list so the hands value can be analyzed
	heros_possible_hand = x
	heros_possible_hand = heros_possible_hand.replace(' ','')
	heros_possible_hand = heros_possible_hand.replace("'",'')
	heros_possible_hand = heros_possible_hand.replace('[','')
	heros_possible_hand = heros_possible_hand.replace(']','')
	heros_possible_hand = heros_possible_hand.split(',')
	#loops through each possible hand villain can have for each hand hero can have
	for y in range(0,len(possible_showdowns[x])):
		#TEMPORARY
		print(heros_possible_hand, possible_showdowns[x],find_handclass(heros_possible_hand),find_handclass(possible_showdowns[x][y]))	
		#counts combinations
		totalsimulations = totalsimulations + 1
		#counts heros wins
		if does_hero_win(heros_possible_hand, possible_showdowns[x][y]) == True:
			print('hero wins')
			herowins = herowins + 1
		#counts ties
		else:
			if is_splitpot(heros_possible_hand, possible_showdowns[x][y]) == True:
				herowins = herowins + .5

print("Hero wins " + str(100*(herowins/totalsimulations)) + " percentage of the time, winning " + str(herowins) + " number of times out of " + str(totalsimulations) + " total possible outcomes.")
