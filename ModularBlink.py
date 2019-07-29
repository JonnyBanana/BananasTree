from christmastree import ChristmasTree
from time import sleep

def red_down(leds):
    for led in [1, 3]:
        leds[led].on()
        
def red_middle(leds):
    for led in [4, 6]:
        leds[led].on()
        
def red_up(leds):
    for led in [8]:
        leds[led].on()
        
def green_down(leds):
    for led in [0, 2]:
        leds[led].on()
        
def green_middle(leds):
    for led in [5, 7]:
        leds[led].on()
        
def green_up(leds):
    for led in [9]:
        leds[led].on()

tree = ChristmasTree()
tree.star.off()
leds = tree.leds

try:
    tree.star.off()
    while True:
        #reds down to up
        tree.baubles.off()
        sleep(.5)
        red_down(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        red_middle(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        red_up(leds)
        sleep(.5)
        #greens down to up
        tree.baubles.off()
        sleep(.5)
        green_down(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        green_middle(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        green_up(leds)
        sleep(.5)
        #christmas star
        tree.star.on()
        sleep(.7)
        tree.star.off()
        #greens up o down
        tree.baubles.off()
        sleep(.5)
        green_middle(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        green_down(leds)
        sleep(.5)
        # reds up o down
        tree.baubles.off()
        sleep(.5)
        red_up(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        red_middle(leds)
        sleep(.5)
        tree.baubles.off()
        sleep(.5)
        red_down(leds)
        sleep(.5)
        #christmas star
        tree.star.on()
        sleep(.7)
        tree.star.off()
        
except:
        tree.off
        tree.close()
