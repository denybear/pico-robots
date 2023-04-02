# library from: https://github.com/blaz-r/pi_pico_neopixel
import gradient
import time
import random
#from neopixel import Neopixel
from neopixel import Neopixel
# number of pixels
numpix = 9
# state machine 0, GPIO 0
pixels = Neopixel(numpix, 0, 0, "GRB")

red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
chartreuse = (128,255,0)
green = (0, 255, 0)
spring = (0,255,128)
cyan = (0,255,255)
azure = (0,128,255)
blue = (0, 0, 255)
violet = (128, 0, 255)
magenta = (255, 0, 255)
rose = (255,0,128)
colors = [red, orange, yellow, chartreuse, green, spring, cyan, azure, blue, violet, magenta, rose, red]

"""
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)

Examples
pixels.set_pixel(5, (10, 0, 0))
pixels.set_pixel_line(5, 7, (0, 10, 0))
pixels.fill((20, 5, 0))

rgb1 = (0, 0, 50)
rgb2 = (50, 0, 0)
pixels.set_pixel(42, (0, 50, 0))
pixels.set_pixel_line(5, 7, rgb1)
pixels.set_pixel_line_gradient(0, 13, rgb1, rgb2)

For new settings to take effect you write:
pixels.show()

howBright parameter for lightness (0 to 255)
pixels.set_pixel(5, (10, 0, 0), howBright)
"""

def EffetUnie(debut,fin):
    brightness = random.choice(([85, 170, 255],[255, 255, 255],[255, 170, 85]))
    for i in range (debut, fin):

        colorGradient = gradient.gradient(colors[(i)%12], colors[(i+1)%12],numpix*2)
        
        for couleur in colorGradient:

            for j in range(numpix):
                pixels.set_pixel(j,couleur, brightness[j%3])
            pixels.show()

            time.sleep(0.1)

def EffetPulse(debut,fin):
    for i in range (debut, fin):
        
        colorGradient = gradient.gradient(colors[(i)%12], colors[(i+1)%12],5)
        compteur = 0
        #setup=random.sample(range(9),9)

        setup=[]
        rand = random.randint(0,numpix-1)
        
        for k in range(numpix):
            while rand in setup:
                rand = random.randint(0,numpix-1)
            setup.append(rand)
        
        for couleur in colorGradient:
            for j in setup[0:compteur]:
                for h in range(9):
                    pixels.set_pixel(j,couleur, h*(255/9))
                    pixels.show()
                    time.sleep(0.03)
                time.sleep(0.02)
            time.sleep(0.4)
            for j in setup[0:compteur]:
                for h in range(9,-1,-1):
                    pixels.set_pixel(j,couleur, h*(255/9))
                    pixels.show()
                    time.sleep(0.03)
            compteur+=2
            

def EffetSerpent(debut,fin):
    path = random.choice(([0,1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1,0]))
    for i in range (debut,fin):

        colorGradient = gradient.gradient(colors[(i)%12], colors[(i+1)%12],18)
        compteur = 0
        for couleur in colorGradient:
            
            for j in range(numpix):
                pixels.set_pixel(path[(compteur-j)%numpix],couleur, 255-(int(255/9)*j))
            
            pixels.show()

            compteur+=1
            time.sleep(0.15)

def EffetLigne(debut,fin):
    path = random.choice((([0,1,2],[3,4,5],[6,7,8]),([0,3,6],[1,4,7],[2,5,8])))
    for i in range (debut,fin):

        colorGradient = gradient.gradient(colors[(i)%12], colors[(i+1)%12],3)
        compteur = 0
        for couleur in colorGradient:

            for h in path[compteur%len(path)]:
                pixels.set_pixel(h,couleur, 255)
            
                pixels.show()
                time.sleep(0.025)
                
            for h in range(16):
                for k in path[compteur%len(path)]:
                    pixels.set_pixel(k,couleur, 255-int(255/16)*(h+2))
                pixels.show()
                time.sleep(0.05)

            compteur+=1

def EffetVague(debut,fin):
    brightness = random.choice(([20, 255, 255],[20,20,255]))
    for i in range (debut,fin):
        colorGradient = gradient.gradient(colors[i%12], colors[(i+1)%12],15)
        compteur = 0

        for couleur in colorGradient:
            for j in range(numpix):
                pixels.set_pixel(j,couleur, brightness[(compteur-j)%3])    
            pixels.show()

            compteur+=1
            time.sleep(0.15)
            
def EffetProgressBar(debut,fin):
    for i in range (debut,fin):
        colorGradient = gradient.gradient(colors[i%12], colors[(i+1)%12],18)
        compteur = 8
        for couleur in colorGradient[0:int(len(colorGradient)/2)]:
            for k in range(compteur+1):
                for h in range(compteur+1):
                    pixels.set_pixel(h,couleur, 0)
                pixels.set_pixel(k,couleur, 255)
                pixels.show()
                time.sleep(0.05)

            for j in range(numpix-1,compteur, -1):
                pixels.set_pixel(j,couleur, 255)
            pixels.show()

            compteur-=1
            time.sleep(0.3)
        compteur = 1
        for couleur in colorGradient[int(len(colorGradient)/2):-1]:
            for k in range(0, 9):
                for h in range(9-compteur):
                    pixels.set_pixel(h,couleur, 255)
                pixels.set_pixel(k,couleur, 0)
                pixels.show()
                time.sleep(0.05)

            compteur+=1
            time.sleep(0.3)

def EffetAleatoire(debut,fin):
    #pixOn = random.sample(range(9),9)
    pixOn=[]
    rand = random.randint(0,numpix-1)
    
    for k in range(numpix):
        while rand in pixOn:
            rand = random.randint(0,numpix-1)
        pixOn.append(rand)
    
    compteur = 0
    for i in range (debut,fin):
        colorGradient = gradient.gradient(colors[i%12], colors[(i+1)%12],3)
        for couleur in colorGradient:
            for h in range(numpix):
                pixels.set_pixel(pixOn[compteur%numpix], couleur, 255-int(255/numpix)*(h))
                pixels.show()
                time.sleep(0.05)
            pixels.set_pixel(pixOn[compteur%numpix], couleur, 0)
            compteur+=1           
            
def Transition():
    #Rentre les fonctions dans une liste pour les choisir de maniere random
    fonctions = [EffetAleatoire, EffetLigne, EffetSerpent, EffetUnie, EffetVague, EffetPulse, EffetProgressBar]
    #fonctions=[EffetAleatoire]
    last = EffetUnie
    a = random.choice([3,6])
    for i in range(0,len(colors)-1, a):
        #Bout de code pour ne pas tomber plusieur fois sur le meme effet d'affile
        r=random.choice(fonctions)
        while r == last:
            r=random.choice(fonctions)

        r(i,i+(a))
        last=r
        #Fait un effet degrade pour switch d'effet
        for h in range(18):
            for j in range(numpix):
                pixels.set_pixel(j,colors[(i+a)%12], abs(255-int(255/18)*(h+1)))
            pixels.show()
            time.sleep(0.05)
        for j in range(numpix):
            pixels.set_pixel(j,colors[(i+a)%12], 0)
        pixels.show()
        time.sleep(0.05)
        a = random.choice([3,6,9])
        time.sleep(1)

while True:
    Transition()
