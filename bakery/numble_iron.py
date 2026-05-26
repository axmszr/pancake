
class NumbleIron():
    # 00 01 02 03 04 05 06
    # 07    08    09    10
    # 11 12 13 14 15 16 17
    # 18    19    20    21
    # 22 23 24 25 26 27 28
    # 29    30    31    32
    # 33 34 35 36 37 38 39
    
    SIZE = 7
    INDSS = []

    def make_indss():
        size = NumbleIron.SIZE
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
        NumbleIron.INDSS = tuple(indss)

    def compass_to_ids(num, compass):
        size = NumbleIron.SIZE
        odd_row = size // 2
        num_odd = num // odd_row
        match compass:
            case 'N':
                return 2 * num + 1 + (odd_row + 2) * num_odd
            case 'W':
                return num + size * (num_odd + 1) + num_odd
            case 'E':
                return num + (size + 1) * (num_odd + 1)
            case 'S':
                return 2 * num + 2 + (odd_row + 2) * num_odd + odd_row + size
        
    def __init__(self, tiles, colours, sums):
        num_tiles = NumbleIron.SIZE ** 2 - (NumbleIron.SIZE // 2) ** 2
        if len(tiles) != num_tiles:
            print("Bad tiles input. Please try again.")
            return
        if len(colours) != num_tiles:
            print("Bad colours input. Please try again.")
            return
        
        sum_strs = sums.split()
        if len(sum_strs) != (NumbleIron.SIZE // 2) ** 2:
            print("Bad sums input. Please try again.")
            return

        self.tiles = []
        # so far pool not necessary but just in case
        self.number_pool = {i : 0 for i in range(1, NumbleIron.SIZE+1)}
        self.poss = {}
        for i in range(num_tiles):
            tile = int(tiles[i])
            if colours[i] == '1':
                self.tiles.append(tile)
            elif colours[i] == '0':
                self.tiles.append(0)
                self.number_pool[tile] += 1
                self.poss[i] = (1 << tile) | 1
            else:
                print(f"Bad colour: {colours[i]}")

        NumbleIron.make_indss()
    
        # (idx, idx, sum)
        sums = []
        for i in range(len(sum_strs)):
            sum_str = sum_strs[i]
            id1 = NumbleIron.compass_to_ids(i, sum_str[0])
            id2 = NumbleIron.compass_to_ids(i, sum_str[1])
            s = int(sum_str[2:])
            sums.append((id1, id2, s))
        self.sums = tuple(sums)

    def rust(self):
        # check completed sums first
        for i in range(len(self.sums)):
            id1, id2, s = self.sums[i]
            if self.tiles[id1] + self.tiles[id2] == 0:
                continue
            
            if self.tiles[id1] != 0:
                self.tiles[id2] = s - self.tiles[id1]
                self.number_pool[self.tiles[id2]] -= 1
                self.poss.pop(id2, None)
                #print(f"Sum: [{id2}] -> {self.tiles[id2]}")
            else:
                self.tiles[id1] = s - self.tiles[id2]
                self.number_pool[self.tiles[id1]] -= 1
                self.poss.pop(id1, None)
                #print(f"Sum: [{id1}] -> {self.tiles[id1]}")
            self.sums = self.sums[:i] + self.sums[i+1:]
            return True            

        # split and make masks
        for inds in NumbleIron.INDSS:
            mask = 0
            for i in inds:
                mask |= 1 << self.tiles[i]
            for i in inds:
                if i in self.poss:
                    self.poss[i] |= mask

        # check sums
        for id1, id2, s in self.sums:
            start = s - NumbleIron.SIZE
            if start < 1:
                start = 1
            end = s - 1
            if end > NumbleIron.SIZE:
                end = NumbleIron.SIZE
            for x in range(start, end + 1):
                # if one tile cannot be x, the other cannot be s-x
                if self.poss[id1] & (1 << x):
                    self.poss[id2] |= 1 << (s - x)
                if self.poss[id2] & (1 << x):
                    self.poss[id1] |= 1 << (s - x)
        '''
        # check needs
        for inds in NumbleIron.INDSS:
            for x in range(1, NumbleIron.SIZE + 1):
                found = False
                unique = False
                winner = -1
                for i in inds:
                    if self.tiles[i] == x:
                        found = True
                        break
                    if i in self.poss and not (self.poss[i] & (1 << x)):
                        if unique:
                            unique = False
                            break
                        winner = i
                        unique = True
                if found or not unique:
                    continue
                self.poss[winner] = (1 << x) ^ (2 ** (NumbleIron.SIZE + 1) - 1)
        '''
        to_pop = []
        for i in self.poss:
            bility = self.poss[i] ^ (2 ** (NumbleIron.SIZE + 1) - 1)
            for x in range(1, NumbleIron.SIZE + 1):
                if bility == 1 << x:
                    self.tiles[i] = x
                    self.number_pool[x] -= 1
                    to_pop.append(i)
                    #print(f"Only: [{i}] -> {x}")
                    break
        
        for i in to_pop:
            self.poss.pop(i)

        return bool(to_pop)

    def solve(self):
        while self.poss:
            if not self.rust():
                print("Stuck!")
                break
        return ''.join(map(str, self.tiles))
