import random

def iota():
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    ID = ""
    while counter < 81:
        x = random.randint(0,10)
        if x > 0:
            ID += str(table[random.randint(0,25)])
        else:
            ID += "9"
        counter += 1
    return ID
    
    