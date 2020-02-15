import random
import time
import Tkinter

top = Tkinter.Tk()
top.mainloop()

def random_hand():
    random.seed(time.time())
    r = random.randrange(1, 4, 1)

    if (r == 1):
        hand = "kamen"
    elif (r == 2):
        hand = "skarje"
    elif (r == 3):
        hand = "papir"

    print(hand)

random_hand()