from part_two import *
from part_three import *

try:
    new_errors(my_packet)
except BrokenConnectionError:
        print("Transmission failed")

