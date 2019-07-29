from christmastree import ChristmasTree
from time import sleep


tree = ChristmasTree()
tree.star.off()
leds = tree.leds


def all_leds(leds):
    for led in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        leds[led].on()

def zero(leds):
    for led in [0]:
        leds[led].on()

def one(leds):
    for led in [1]:
        leds[led].on()
        
def two(leds):
    for led in [2]:
        leds[led].on()
        
def three(leds):
    for led in [3]:
        leds[led].on()
        
def four(leds):
    for led in [4]:
        leds[led].on()
        
def five(leds):
    for led in [5]:
        leds[led].on()
        
def six(leds):
    for led in [6]:
        leds[led].on()
                
def seven(leds):
    for led in [7]:
        leds[led].on()
                
def eight(leds):
    for led in [8]:
        leds[led].on()
                
def nine(leds):
    for led in [9]:
        leds[led].on()
        
def m1(leds):
    for led in [0, 4]:
        leds[led].on()
        
def m2(leds):
    for led in [1, 5]:
        leds[led].on()
        
def m3(leds):
    for led in [2, 6, 8]:
        leds[led].on()
        
 #ever wih christmas sar       
def m4(leds):
    for led in [3, 7, 9]:
        leds[led].on()
        
        
while True:
 
    tree.baubles.off()
    sleep(.1)
    zero(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    four(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    one(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    five(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    two(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    six(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    eight(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    three(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    seven(leds)
    sleep(.1)
    tree.baubles.off()
    sleep(.1)
    nine(leds)
    sleep(.1)
    
    #chrismas star
    tree.star.on()
    sleep(.3)
    tree.star.off()
   
    tree.baubles.off()
    sleep(.1)
    m1(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m2(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m3(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m4(leds)
    sleep(.2)
    
    #christmas star
    tree.star.on()
    sleep(.4)
    tree.star.off()
    
    #all leds on!
    all_leds(leds)
    sleep(.5)
    
     #christmas star
    tree.star.on()
    sleep(.4)
    tree.star.off()
    
    
    
    tree.baubles.off()
    sleep(.1)
    m1(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m2(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m3(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m4(leds)
    sleep(.2)
    
    #christmas star
    tree.star.on()
    sleep(.4)
    tree.star.off()
    
    tree.baubles.off()
    sleep(.1)
    m1(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m2(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m3(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m4(leds)
    sleep(.2)
    
    #christmas star
    tree.star.on()
    sleep(.4)
    tree.star.off()
    
    tree.baubles.off()
    sleep(.1)
    m1(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m2(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m3(leds)
    sleep(.2)
    tree.baubles.off()
    sleep(.1)
    m4(leds)
    sleep(.2)
    
    #christmas star
    tree.star.on()
    sleep(.4)
    tree.star.off()
    
    
    
    
    