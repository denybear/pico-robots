# library from: https://github.com/blaz-r/pi_pico_neopixel

import gradient
import time
#from neopixel import Neopixel
from neopixel import Neopixel

# number of pixels
numpix = 3
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

while True:
    for i in range (0, len(colors)-1):
        # 16 steps between initial color and target color
        colorGradient = gradient.gradient (colors[i], colors[i+1],16)
        
        for couleur in colorGradient:
            # assign color to pixel, and show at different brightness
            for j in range (0, numpix):
                pixels.set_pixel(j,couleur, (255/numpix)*(j+1))
            pixels.show()
            # sleep for 0.1 sec
            time.sleep(0.1)
    
