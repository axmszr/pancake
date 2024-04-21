#from .law_school import Painter

def check_file(L, filename):
    with open(filename) as file:
        full_str = file.read()
        words = tuple(w.upper() for w in full_str.split('\n'))

    for word in words:
        if len(word) != L:
            raise Exception(f"Word '{a}' in {filename} does not match length {L}.")

    return words

FIVES = "./fridge/possible_words.txt"
SEVENS = ""

def get_matches(g, col, words):
	if not len(g) == len(col):
		raise Exception(f"String '{g}' and Colouring '{col}' not of same length.")
	
	l = len(g)
	
	matches = []
	for word in words:
		if len(word) != l:
			raise Exception(f"Word {word} in checking set not of length {l}.")
		if Painter.is_match(g, word, col):
			matches.append(word)
	
	return tuple(matches)

def split_up(size, strs):
	num_tiles = size ** 2 - (size // 2) ** 2
	if len(strs) != num_tiles:
		raise Exception(f"Expected {num_tiles} tiles, got {len(strs)}.")
	
	words = []
	
	row_jump = size + size // 2 + 1
	for i in range(size // 2 + 1):
		row_start = i * row_jump
		row_word = strs[row_start : row_start + size]
		words.append(row_word)

	column_e2o = size
	column_o2e = size // 2 + 1
	for i in range(size // 2 + 1):
		column_i = i * 2
		column_word = strs[column_i]
		for j in range(size // 2):
			column_i += column_e2o
			column_word += strs[column_i]
			
			column_i += column_o2e
			column_word += strs[column_i]
		
		words.append(column_word)
		
		column_e2o -= 1
		column_o2e += 1
	
	return words
