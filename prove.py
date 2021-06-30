from math import log, ceil, floor, sqrt
from itertools import count, islice
import math
# Allora se num < 0, skip, altrimenti se num == prime allora lui stesso, num non prime closest number power of 2

list_numbers = [9, 15, 33]
# is_prime = lambda n: x > 1 and all(x % i for i in islice(count(2), int(sqrt(x)-1)))
def next_power_of_2(x):  
    return 1 if x == 0 else 2**(x - 1).bit_length()

solve = lambda l: [x if x > 1 and all(x % i for i in islice(count(2), int(sqrt(x)-1))) else 2**min(floor(log(x, 2)), ceil(log(x, 2)), key= lambda z: abs(x-2**z)) for x in l if x > 0]

print(solve(list_numbers))