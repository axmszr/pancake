from .law_school import Painter

# Pool Filters

def filter_by_colouring(word_pool, g, col):
	return tuple(filter(lambda word: Painter.is_match(g, word, col), word_pool))

def get_letter_counts(word):
	counts = {}
	for letter in word:
		if not letter.isalpha():
			continue
		let = letter.upper()
		if let not in counts:
			counts[let] = 0
		counts[let] += 1
	return counts

# dict of "aabcd" - "ad" -> "abc"
# must have bet <= alpha (subset)
def subtract_letter_counts(alpha, beta):
	gamma = alpha.copy()
	for b in beta:
		gamma[b] -= beta[b]
	return gamma

def fits_in_pool(word, letter_pool):
	counts = get_letter_counts(word)
	for letter in counts:
		if letter not in letter_pool:
			return False
		if counts[letter] > letter_pool[letter]:
			return False
	else:
		return True

def filter_by_letters(word_pool, letter_pool):
	output = []
	return tuple(filter(lambda word: fits_in_pool(word, letter_pool), word_pool))

# "_" for blanks
def filter_by_template(word_pool, template):
	tem = template.upper()
	alphas = [i for i in range(len(tem)) if tem[i].isalpha()]
	output = []
	for word in word_pool:
		for i in alphas:
			if word[i].upper() != tem[i]:
				break
		else:
			output.append(word)
	return tuple(output)

# 'T____' with {T : 0, ...} will accept 'TAXES' but not 'TITAN'
def filter_by_shadow(word_pool, template, letter_pool):
	new_pool = filter_by_template(word_pool, template)
	
	space = [i for i in range(len(tem)) if not template[i].isalpha()]
	output = []
	for word in new_word:
		cut_word = ''.join(word[i] for i in space)
		if fits_in_pool(cut_word, letter_pool):
			output.append(word)
	return tuple(output)
