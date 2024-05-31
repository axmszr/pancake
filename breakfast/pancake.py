
class Pancake:
    def __init__(self, size, *strs):
        if not strs:
            print("No inputs provided. Please try again.")
            return

        num_tiles = size ** 2 - (size // 2) ** 2

        if len(strs[0]) != num_tiles:
            print("Bad current input. Please try again.")
            return

        self.size = size
        self.num_tiles = num_tiles

        upper_init = strs[0].upper()
        self.init = tuple(upper_init)
        self.curr = list(upper_init)
        
        self.move_queue = []

        if len(strs) == 1:
            self.soln = tuple(upper_init)
        elif len(strs[1]) != num_tiles:
            print("Bad solution input. Please try again.")
        else:
            self.soln = tuple(strs[1].upper())

    def get_size(self):
        return self.size

    def get_num_tiles(self):
        return self.num_tiles

    def get_queue(self):
        return self.move_queue
    
    def tile_solved(self, index):
        return self.curr[index] == self.soln[index]

    def is_solved(self):
        for i in range(self.get_num_tiles()):
            if not self.tile_solved(i):
                return False
        return True

    # outdated tech. we do multi-uniques now!
    '''
    def get_unique_letters(self):
        count = {}
        for i in range(self.get_num_tiles()):
            if self.tile_solved(i):
                continue
            
            letter = self.curr[i]
            if letter not in count:
                count[letter] = 0
            count[letter] += 1

        uniques = []
        for letter in count:
            if count[letter] == 1:
                uniques.append(letter)

        return uniques
    '''

    # double swaps is always the shortest way to move
    # both to their final position.
    def queue_double_swaps(self):
        queue = self.get_queue()
        for i in range(self.get_num_tiles() - 1):
            curr_i = self.curr[i]
            soln_i = self.soln[i]

            for j in range(i+1, self.get_num_tiles()):
                curr_j = self.curr[j]
                soln_j = self.soln[j]

                if curr_i == curr_j:
                    continue
                if soln_j == curr_i and curr_j == soln_i:
                    queue.append((i, j, "Double Swap"))

    def get_many_to_ones(self):
        swap_to = {}
        for i in range(self.get_num_tiles()):
            if self.tile_solved(i):
                continue
            wrong = self.curr[i]
            right = self.soln[i]
            if right not in swap_to:
                swap_to[right] = set()
            swap_to[right].add(wrong)

        ones = []
        for right in swap_to:
            if len(swap_to[right]) > 1:
                continue
            (wrong,) = swap_to[right]
            ones.append((right, wrong))

        return ones

    # if all the As want to swap with Bs (not necessarily
    # surjective), there is no change to the overall structure.
    # this includes uniques swaps
    def queue_unique_moves(self):
        queue = self.get_queue()
        ones = self.get_many_to_ones()
        for right, wrong in ones:
            rights = []
            wrongs = []
            for i in range(self.get_num_tiles()):
                if self.tile_solved(i):
                    continue
                if self.curr[i] == right:
                    rights.append(i)
                if self.curr[i] == wrong and self.soln[i] == right:
                    wrongs.append(i)

            if len(rights) == 1:
                queue.append((rights[0], wrongs[0], "Unique"))
            else:
                for i in range(len(rights)):
                    queue.append((rights[i], wrongs[i], "Multi-Unique"))

    def next_move(self):
        queue = self.get_queue()
        while queue:
            move = queue.pop()
            if not (self.tile_solved(move[0]) or self.tile_solved(move[1])):
                return move

        self.queue_double_swaps()
        if queue:
            return queue.pop()
        
        self.queue_unique_moves()
        if queue:
            return queue.pop()

        raise Exception("Welp, need a new algo.")
    
    def do_move(self, move):
        if not move:
            print("Empty move.")
            return

        a = self.curr[move[0]]
        b = self.curr[move[1]]
        self.curr[move[0]], self.curr[move[1]] = b, a

    # Printers
    def stringify_tile(self, tile):
        mod = 2 * self.get_size() - self.get_size() // 2
        row = tile // mod * 2
        col = tile % mod
        if col >= self.get_size():
            row += 1
        if col >= self.get_size():
            col = (col - self.get_size()) * 2
        
        alpha = chr(ord('A') + col)
        bet = str(row + 1)
        return f"{alpha}{bet} [{self.curr[tile]}]"

    def stringify_move(self, move):
        s1 = self.stringify_tile(move[0])
        s2 = self.stringify_tile(move[1])

        if s2 < s1:
            s1, s2 = s2, s1
        return f"{s1} <-> {s2} : {move[2]}!"

    def show_template(tiles):
        print("Pancake is an abstract class; " + \
                "show_template is not defined")

    def show_curr(self):
        self.__class__.show_template(self.curr)

    def show_init(self):
        self.__class__.show_template(self.init)

    def show_soln(self):
        self.__class__.show_template(self.soln)

    def show_index_ref():
        print("Pancake is an abstract class; " + \
                "show_index_ref is not defined")

    def show_tile_ref():
        print("Pancake is an abstract class; " + \
                "show_tile_ref is not defined")

    # Run
    def run(self):
        print()
        self.__class__.show_tile_ref()
        print("Moves:")

        num_moves = 0
        while not self.is_solved():
            move = self.next_move()
            if not move:
                break

            num_moves += 1
            print(f"{num_moves : >2}: {self.stringify_move(move)}")
            self.do_move(move)

        if self.is_solved():
            print("\nDone! Here it is:")
        else:
            print("\nWe're stuck at:")

        self.show_curr()

    def reset(self):
        self.curr = list(self.init)
