from .iron import *

class WaffleIron(Iron):
    # 00 01 02 03 04
    # 05    06    07
    # 08 09 10 11 12
    # 13    14    15
    # 16 17 18 19 20

    SIZE = 5
    FILE = "fridge/possible_words.txt"

    def __init__(self, tiles, colours):
        super().__init__(WaffleIron.SIZE, tiles, colours)

    def solve(self):
        super().solve(check_file(WaffleIron.SIZE, WaffleIron.FILE))
        return super().verify_sols()
