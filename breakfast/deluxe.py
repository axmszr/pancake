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
                "A1  A2  A3  A4  A5  A6  A7\n" + \
                "B1      B3      B5      B7\n" + \
                "C1  C2  C3  C4  C5  C6  C7\n" + \
                "D1      D3      D5      D7\n" + \
                "E1  E2  E3  E4  E5  E6  E7\n" + \
                "F1      F3      F5      F7\n" + \
                "G1  G2  G3  G4  G5  G6  G7\n")
