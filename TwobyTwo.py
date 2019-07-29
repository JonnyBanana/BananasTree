from christmastree import ChristmasTree
from time import sleep



def zero(leds):
    for led in [0, 1]:
        leds[led].on()

def one(leds):
    for led in [2, 3]:
        leds[led].on()
        
def two(leds):
    for led in [4, 5]:
        leds[led].on()
        
def three(leds):
    for led in [6, 7]:
        leds[led].on()
        
def four(leds):
    for led in [8, 9]:
        leds[led].on()
        
        
tree = ChristmasTree()
tree.star.on()
leds = tree.leds



while True:
    
    
    
    #step 1: down to up 300 ms
    tree.baubles.off()
    sleep(.3)
    four(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    three(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    two(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    one(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    zero(leds)
    sleep(.3)
                
    #step 2: down to up 300 ms
    tree.baubles.off()
    sleep(.3)
    zero(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    one(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    two(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    three(leds)
    sleep(.3)
    tree.baubles.off()
    sleep(.3)
    four(leds)
    sleep(.3)
    
    #step 3: down to up 200 ms
    tree.baubles.off()
    sleep(.2)
    four(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    three(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    two(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    one(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    zero(leds)
    sleep(.2)
    
    #step 4: down to up 200 ms
    tree.baubles.off()
    sleep(.2)
    zero(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    one(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    two(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    three(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    four(leds)
    sleep(.2)
    
    #step 5: down to up 100 ms
    tree.baubles.off()
    sleep(.2)
    four(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    three(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    two(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    one(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    zero(leds)
    sleep(.2)
            
    #step 6: down to up 100 ms
    tree.baubles.off()
    sleep(.2)
    zero(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    one(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    two(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    three(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.2)
    four(leds)
    sleep(.2)
    