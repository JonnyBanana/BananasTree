from christmastree import ChristmasTree
from time import sleep

tree = ChristmasTree()
tree.star.on()
leds = tree.leds

def all_leds(leds):
    for led in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        leds[led].on()


    

while True:
    
    tree.baubles.off()
    sleep(.5)
    all_leds(leds)
    sleep(.5)
    
