from .sieve import *

def check_file(L, filename):
    with open(filename) as file:
        full_str = file.read()
        words = tuple(w.upper() for w in full_str.split('\n'))

    for word in words:
        if len(word) != L:
            raise Exception(f"Word '{a}' in {filename} does not match length {L}.")

    return words

FIVES = "../fridge/possible_words.txt"
SEVENS = ""

class Iron:
	def __init__(self, size, tiles, colours):
		# skipping validity checks
		
		self.size = size
		self.tiles = tiles.upper()
		self.colours = colours.upper()
		self.letter_pool = get_letter_counts(self.tiles)
		self.sols = []
		
		# creating indices reference
		indss = []
		
		row_jump = size + size // 2 + 1
		for r in range(size // 2 + 1):
			row_start = r * row_jump
			row_inds = tuple(range(row_start, row_start + size))
			indss.append(row_inds)

		column_e2o = size
		column_o2e = size // 2 + 1
		for c in range(size // 2 + 1):
			curr_i = c * 2
			column_inds = [curr_i]
			for _ in range(size // 2):
				curr_i += column_e2o
				column_inds.append(curr_i)
				
				curr_i += column_o2e
				column_inds.append(curr_i)
			
			indss.append(tuple(column_inds))
			column_e2o -= 1
			column_o2e += 1
		
		self.indss = tuple(indss)
		
	# big string -> rows (top to bottom) and columns (left to right)
	def oxidize(self, strs):
		splits = []
		for inds in self.indss:
			splist = [strs[i] for i in inds]
			splits.append(''.join(splist))
		
		return tuple(splits)
	
	# rows and columns -> big string
	def reduce(self, splits):
		lst = [None for _ in range(self.size ** 2 - (size // 2) ** 2)]
		for j in range(len(self.indss)):
			splist = splits[j]
			inds = self.indss[j]
			for i in range(len(inds)):
				lst[inds[i]] = splist[i]
		
		return ''.join(lst)

	def redox(self, splits):
		return self.oxidize(self.reduce(splits))

	def rust(self, guesses, word_pools):
		not_guessed = []
		new_pools = []
		for i in range(len(guesses)):
			if guesses[i].isalpha():
				# already guessed
				continue
			if word_pools[i] == ():
				# not yet guessed and no candidates
				# prune this branch
				return
			not_guessed.append(i)
		
		if not_guessed == []:
			# successfully completed guess
			self.sols.append(tuple(guess))
			return
		
		# to minimize iterations
		best_i = min(not_guessed, lambda i: len(word_pools[i]))
		
		for guess in word_pools[best_i]:
			new_guesses = guesses.copy()
			new_guesses[best_i] = match
			
			FeO = self.reduce(new_guesses)
			Fe2O3 = self.oxidize(FeO)
			
			new_letters = get_letter_counts(FeO)
			new_pools = [() for _ in word_pools]
			for i in not_guessed:
				if i == best_i:
					continue
				new_pools[i] = filter_by_shadow(word_pools[i], Fe2O3[i], new_letters)
			
			self.rust(new_guesses, new_pools)

		return self.sols

	def solve(self, word_pool):
		# need to (guess -> update pool AND colouring -> refilter -> guess -> ...)
		
		new_pool = filter_by_letters(word_pool, self.letter_pool)
		
		lets = self.oxidize(self.tiles)
		cols = self.oxidize(self.colours)
		word_pools = [filter_by_colouring(new_pool, lets[i], cols[i]) for i in range(self.size + 1)]
		
		blank_guesses = ['_' * self.size for i in range(size + 1)]
		
		self.rust(blank_guesses, word_pools)
		
		return self.sols
