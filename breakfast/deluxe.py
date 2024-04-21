from .pancake import Pancake

class Deluxe(Pancake):
    # 00 01 02 03 04 05 06
    # 07    08    09    10
    # 11 12 13 14 15 16 17
    # 18    19    20    21
    # 22 23 24 25 26 27 28
    # 29    30    31    32
    # 33 34 35 36 37 38 39
        
    SIZE = 7
        
    def __init__(self, *strs):
        super().__init__(Deluxe.SIZE, *strs)

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
        print("Tiles:\n" + \
                "00  01  02  03  04  05  06\n" + \
                "07      08      09      10\n" + \
                "11  12  13  14  15  16  17\n" + \
                "18      19      20      21\n" + \
                "22  23  24  25  26  27  28\n" + \
                "29      30      31      32\n" + \
                "33  34  35  36  37  38  39\n")

    def show_tile_ref():
        print("Tiles:\n" + \
                "A1  B1  C1  D1  E1  F1  G1\n" + \
                "A2      C2      E2      G2\n" + \
                "A3  B3  C3  D3  E3  F3  G3\n" + \
                "A4      C4      E4      G4\n" + \
                "A5  B5  C5  D5  E5  F5  G5\n" + \
                "A6      C6      E6      G6\n" + \
                "A7  B7  C7  D7  E7  F7  G7\n")
