from .iron import *

class DeluxeIron(Iron):
    # 00 01 02 03 04 05 06
    # 07    08    09    10
    # 11 12 13 14 15 16 17
    # 18    19    20    21
    # 22 23 24 25 26 27 28
    # 29    30    31    32
    # 33 34 35 36 37 38 39
        
    SIZE = 7
    FILE = None
    
    def __init__(self, tiles, colours):
        super().__init__(DeluxeIron.SIZE, tiles, colours)

    def solve(self):
        super().solve(check_file(DeluxeIron.SIZE, DeluxeIron.FILE))
        return super().verify_sols()

