from .pancake import Pancake

class Waffle(Pancake):
    # 00 01 02 03 04
    # 05    06    07
    # 08 09 10 11 12
    # 13    14    15
    # 16 17 18 19 20

    SIZE = 5

    def __init__(self, *strs):
        super().__init__(Waffle.SIZE, *strs)

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

    def show_tile_ref():
        print("Tiles:\n" + \
                "A1  A2  A3  A4  A5\n" + \
                "B1      B3      B5\n" + \
                "C1  C2  C3  C4  C5\n" + \
                "D1      D3      D5\n" + \
                "E1  E1  E3  E4  E5\n")
