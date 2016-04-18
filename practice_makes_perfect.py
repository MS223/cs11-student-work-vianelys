def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print is_even(18)
# this one works because I put 17 and it said false and with 18 it said true.
def is_int(x):
    if int:
        return True
    else:
        return False
print is_int(7.0)
# this one doesn't work because I put 7.5 and it said true. It also said true for 7.0 though.
