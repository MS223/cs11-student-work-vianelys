list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def find_odds(input):
    for whatever in input:
        if whatever % 2 == 1:
            print whatever
            find_odds(input)
