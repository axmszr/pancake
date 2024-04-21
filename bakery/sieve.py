
# Letter Pool Stuff

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


# Pool Filters

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
	
	space = [i for i in range(len(template)) if not template[i].isalpha()]
	output = []
	for word in new_pool:
		cut_word = ''.join(word[i] for i in space)
		if fits_in_pool(cut_word, letter_pool):
			output.append(word)
	return tuple(output)

def filter_by_green(word_pool, g, col):
        templist = [g[i] if col[i] == 'G' else '_' for i in range(len(g))]
        template = ''.join(templist)
        return filter_by_template(word_pool, template)


# Colouring

def colour(g, a):
        l = len(g)
        new_g = g.upper()
        new_a = a.upper()

        match = tuple(new_g[i] == new_a[i] for i in range(l))
        remain = [new_a[i] for i in range(l) if not match[i]]

        out = []
        for i in range(l):
            if match[i]:
                out.append('G')
            elif new_g[i] in remain:
                out.append('Y')
                remain.remove(new_g[i])
            else:
                out.append('R')

        return ''.join(out)

def R_to_U(col):
        U_list = ['_' if c == 'R' else c for c in col]
        return ''.join(U_list)

def U_to_R(col):
        R_list = ['R' if c == '_' else c for c in col]
        return ''.join(R_list)
