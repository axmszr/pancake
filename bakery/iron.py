from .sieve import *
from .law_school import Painter

def check_file(L, filename):
	with open(filename) as file:
		full_str = file.read()
		words = tuple(w.upper() for w in full_str.split('\n'))

	for word in words:
		if len(word) != L:
			raise Exception(f"Word '{a}' in {filename} does not match length {L}.")

	return words

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
		lst = ['_' for _ in range(self.size ** 2 - (self.size // 2) ** 2)]
		for j in range(len(self.indss)):
			splist = splits[j]
			inds = self.indss[j]
			for i in range(len(inds)):
				if splist[i].isalpha():
					lst[inds[i]] = splist[i]
		
		return ''.join(lst)

	def rust(self, guesses, word_pools):
		not_guessed = []
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
			self.sols.append(tuple(guesses))
			return
		
		# to minimize iterations
		best_i = min(not_guessed, key = lambda i: len(word_pools[i]))
		
		for guess in word_pools[best_i]:
			new_guesses = list(guesses)
			new_guesses[best_i] = guess
			
			FeO = self.reduce(new_guesses)
			Fe2O3 = self.oxidize(FeO)
			
			used_letters = get_letter_counts(FeO)
			new_letters = subtract_letter_counts(self.letter_pool, used_letters)
			new_pools = [() for _ in word_pools]
			for i in not_guessed:
				if i == best_i:
					continue
				new_pools[i] = filter_by_shadow(word_pools[i], Fe2O3[i], new_letters)
			
			self.rust(Fe2O3, new_pools)

		return self.sols

	def solve(self, word_pool):
		# need to (guess -> update pool -> refilter -> guess -> ...)
		
		new_pool = filter_by_letters(word_pool, self.letter_pool)
		
		lets = self.oxidize(self.tiles)
		cols = self.oxidize(self.colours)

		# this filter is incorrect because intersection letters may apply to either word
		#word_pools = [filter_by_colouring(new_pool, lets[i], cols[i]) for i in range(self.size + 1)]
		word_pools = [filter_by_green(new_pool, lets[i], cols[i]) for i in range(self.size + 1)]

		blank_guesses = ['_' * self.size for i in range(self.size + 1)]
		
		self.rust(blank_guesses, word_pools)
		
		return self.sols

	# we don't rigorously use the colouring, so we might as well check
	def verify_solutions(self):
		lets = self.oxidize(self.tiles)

		new_sols = []
		for sol in self.sols:
			sol_cols = [Painter.colour(lets[i], sol[i]) for i in range(self.size + 1)]
			
			# need to turn R into _ to account for overlap
			sol_cols = list(map(R_to_U, sol_cols))
			sol_colours = U_to_R(self.reduce(sol_cols))
			
			if sol_colours == self.colours:
				new_sols.append(sol)
		self.sols = new_sols
		return self.sols
