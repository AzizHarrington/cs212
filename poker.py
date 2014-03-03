import random


mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
	return [random.sample(mydeck, n) for x in xrange(0, numhands)]


def poker(hands):
	"Return a list of winning hands: poker([hand,...]) => [hand,...]"
	return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable."
	key = key or (lambda x: x)
	m = max(iterable, key=key)
	return [x for x in iterable if key(x) >= key(m)]


def hand_rank(hand):
	"Return a value indicating the ranking of a hand."
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks)) # 23456 (8, 6) 6789T (8, 10)
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks)) # 99993 (7, 9, 3)
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif two_pair(ranks):
		return (2, two_pair(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)


def card_ranks(hand):
	"Returns list of ranks - [10, 9, 5, 6, 5]"
	ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
	ranks.sort(reverse=True)
	if ranks == [14, 5, 4, 3, 2]:
		return [5, 4, 3, 2, 1]
	return ranks


def straight(ranks):
	"Return True if the ordered ranks for a 5-card straight"
	r = [n for n in range(min(ranks), max(ranks)+1)]
	r.sort(reverse=True)
	return ranks == r


def flush(hand):
	"Return True if all the cards have the same suit."
	suit = hand[0][1]
	for card in hand:
		if card[1] != suit:
			return False
	return True


def kind(n, ranks):
	"""
	Input => list of ranks, ie [6, 6, 5, 5, 4].
	Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand.
	"""
	for rank in set(ranks):
		if ranks.count(rank) == n:
			return rank
	return None


def two_pair(ranks):
	"""
	Input => list of ranks, ie [6, 6, 5, 5, 4].
	If there are two pair, return the two ranks as a tuple:
	(highest, lowest); otherwise return None.
	"""
	pairs = []
	for r in set(ranks):
		if ranks.count(r) == 2:
			pairs.append(r)
	if len(pairs) == 2:
		return max(pairs), min(pairs)
	return None


def test():
	"Test cases for the functions in poker program."
	sf = "6C 7C 8C 9C TC".split() # straight flush
	fk = "9D 9H 9S 9C 7D".split() # four of a kind
	fh = "TD TC TH 7C 7D".split() # full house
	tp = "5S 5D 9H 9C 6S".split() # two pair
	s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
	s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
	ah = "AS 2S 3S 4S 6C".split() # A high
	sh = "2S 3S 4S 6C 7D".split() # 7 high
	assert poker([s1, s2, ah, sh]) == [s2]
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
	assert kind(4, fkranks) == 9
	assert kind(3, fkranks) == None
	assert kind(2, fkranks) == None
	assert kind(1, fkranks) == 7
	assert two_pair(fkranks) == None
	assert two_pair(tpranks) == (9, 5)
	assert straight([9, 8, 7, 6, 5]) == True
	assert straight([8, 9, 9, 3, 2]) == False
	assert flush(sf) == True
	assert flush(fk) == False
	assert card_ranks(sf) == [10, 9, 8, 7, 6]
	assert card_ranks(fk) == [9, 9, 9, 9, 7]
	assert card_ranks(fh) == [10, 10, 10, 7, 7]
	assert poker([sf, fk, fh]) == [sf]
	assert poker([fk, fh]) == [fk]
	assert poker([fh, fh]) == [fh, fh]
	assert poker([fh]) == [fh]
	assert poker(99*[fk]+[sf]) == [sf]
	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7)
	return "tests pass"


print test()


hand_names = {0:'high card',1:'pair',2:'two pair',3:'3 of a kind',4:'straight',5:'flush',6:'full house',7:'4 of a kind',8:'straight flush'}

def hand_percentages(n=700*1000):
	"Sample n random hands and print a table of percentages for each type of hand."
	counts = [0] * 9
	for i in range(n/10):
		for hand in deal(10):
			ranking = hand_rank(hand)[0]
			counts[ranking] += 1
	for i in reversed(range(9)):
		print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)


# alternate implementation courtesy of peter norvig
# beware crazy looking python!

def alt_hand_rank(hand):
	"Return a value indicating how hight the hand ranks."
	# counts is the count of each rank; ranks lists corresponding ranks
	# E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
	groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
	counts, ranks = unzip(groups)
	if ranks == (14, 5, 4, 3, 2):
		ranks = (5, 4, 3, 2, 1)
	straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
	flush = len(set([s for r,s in hand])) == 1
	return (9 if (5,) == counts else
			8 if straight and flush else
			7 if (4, 1) == counts else
			6 if (3, 2) == counts else
			5 if flush else
			4 if straight else
			3 if (3, 1, 1) == counts else
			2 if (2, 2, 1) == counts else
			1 if (2, 1, 1, 1) == counts else
			0), ranks


def group(items):
	"Return a list of [(count, x)...], highest count first, then highest x first."
	groups = [(items.count(x), x) for x in set(items)]
	return sorted(groups, reverse=True)


def unzip(pairs): return zip(*pairs)


def alt_alt_hand_rank(hand):
	"Return a value indicating how high the hand ranks"
	# counts is the count of each rank; ranks lists corresponding ranks
	# E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
	groups = group(['--23456789TJQKA'.index(r) for r in r,s in hand])
	counts, ranks = unzip(groups)
	if ranks == (14, 5, 4, 3, 2):
		ranks = (5, 4, 3, 2, 1)
	straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
	flush =len(set([s for r,s in hand])) == 1
	return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5, ):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
				  (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}
