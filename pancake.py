
class Pancake:
    def __init__(self, size, *strs):
        if not strs:
            print("No inputs provided. Please try again.")
            return

        if len(strs[0]) != size:
            print("Bad current input. Please try again.")
            return

        self.size = size

        upper_init = strs[0].upper()
        self.init = tuple(upper_init)
        self.curr = list(upper_init)

        if len(strs) == 1:
            self.soln = tuple(upper_init)
        elif len(strs[1]) != size:
            print("Bad solution input. Please try again.")
        else:
            self.soln = tuple(strs[1].upper())

    def tile_solved(self, index):
        return self.curr[index] == self.soln[index]

    def is_solved(self):
        for i in range(self.size):
            if not self.tile_solved(i):
                return False

        return True

    def first_unique_letter(self):
        count = {}

        for i in range(self.size):
            if self.tile_solved(i):
                continue

            letter = self.curr[i]
            if letter not in count:
                count[letter] = 0

            count[letter] += 1

        for letter in count:
            if count[letter] == 1:
                return letter

        return ''

    def next_move(self):
        # unique letter
        u = self.first_unique_letter()
        if u:
            for i in range(self.size):
                if self.tile_solved(i):
                    continue
                if self.curr[i] == u:
                    from_index = i
                if self.soln[i] == u:
                    to_index = i

            return (from_index, to_index, "Unique!")

        # double swap
        for i in range(self.size - 1):
            curr_i = self.curr[i]
            soln_i = self.soln[i]

            for j in range(i+1, self.size):
                curr_j = self.curr[j]
                soln_j = self.soln[j]

                if curr_i == curr_j:
                    continue
                if soln_j == curr_i and \
                        curr_j == soln_i:
                    return (i, j, "Double Swap!")

        # what else?

    def do_move(self, move):
        if not move:
            print("Empty move.")
            return

        a = self.curr[move[0]]
        b = self.curr[move[1]]
        self.curr[move[0]], self.curr[move[1]] = b, a

        # Printers
    def stringify(move):
        s1 = str(move[0])
        if len(s1) == 1:
            s1 = '0' + s1

        s2 = str(move[1])
        if len(s2) == 1:
                        s2 = '0' + s2

        return f"({s1}, {s2}) {move[2]}"

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
        
    # Run
    def run(self):
        self.__class__.show_index_ref()
        print("Moves:")

        num_moves = 0
        while not self.is_solved():
            move = self.next_move()
            if not move:
                break

            num_moves += 1
            print(f"{num_moves : >2}: {Pancake.stringify(move)}")
            self.do_move(move)

        if self.is_solved():
            print("\nDone! Here it is:")
        else:
            print("\nWe're stuck at:")

        self.show_curr()

    def reset(self):
        self.curr = self.init.copy()


class Waffle(Pancake):
    # 00 01 02 03 04
    # 05    06    07
    # 08 09 10 11 12
    # 13    14    15
    # 16 17 18 19 20

    waffle_size = 21

    def __init__(self, *strs):
        super().__init__(Waffle.waffle_size, *strs)

        # Printers
    def show_template(tiles):
        row_1 = ' '.join(tiles[:5]) + '\n'
        row_2 = '   '.join(tiles[5:8]) + '\n'
        row_3 = ' '.join(tiles[8:13]) + '\n'
        row_4 = '   '.join(tiles[13:16]) + '\n'
        row_5 = ' '.join(tiles[16:21]) + '\n'

        print(row_1 + row_2 + row_3 + row_4 + row_5)

    def show_index_ref():
        print("Indices:\n" + \
                "00  01  02  03  04\n" + \
                "05      06      07\n" + \
                "08  09  10  11  12\n" + \
                "13      14      15\n" + \
                "16  17  18  19  20\n")


class Deluxe(Pancake):
    # 00 01 02 03 04 05 06
    # 07    08    09    10
    # 11 12 13 14 15 16 17
    # 18    19    20    21
    # 22 23 24 25 26 27 28
    # 29    30    31    32
    # 33 34 35 36 37 38 39
        
    deluxe_size = 40
        
    def __init__(self, *strs):
        super().__init__(Deluxe.deluxe_size, *strs)

    # Printers
    def show_template(tiles):
        row_1 = ' '.join(tiles[:7]) + '\n'
        row_2 = '   '.join(tiles[7:11]) + '\n'
        row_3 = ' '.join(tiles[11:18]) + '\n'
        row_4 = '   '.join(tiles[18:22]) + '\n'
        row_5 = ' '.join(tiles[22:29]) + '\n'
        row_6 = '   '.join(tiles[29:33]) + '\n'
        row_7 = ' '.join(tiles[33:]) + '\n'

        print(row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7)

    def show_index_ref():
        print("Indices:\n" + \
                "00  01  02  03  04  05  06\n" + \
                "07      08      09      10\n" + \
                "11  12  13  14  15  16  17\n" + \
                "18      19      20      21\n" + \
                "22  23  24  25  26  27  28\n" + \
                "29      30      31      32\n" + \
                "33  34  35  36  37  38  39\n")
