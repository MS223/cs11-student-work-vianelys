def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)

#Nothing happens when you run this code. I dont know what the result s because nothing showed up.

import random
def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
print mystery_function(1, 2)
