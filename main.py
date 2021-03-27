# File: rainfall.py
# Date:    Tue Mar 23 15:24:35 2021
# By:      Matt Myers
# Section: Your Section
# Team:    85
#
# ELECTRONIC SIGNATURE
# Matt Myers
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# A program to simulate rainfall on a slanted metal roof, given rain , wind, and roof angle.

# Take user arguments for roof angle, roof size, Initial drop diameter median, Drops per second median, Duration of rainstorm, Initial wind velocity, Cloud cover seed

# Imports
import math
import random
from Cloudmap import Cloudmap
import pygame,sys,os,statistics
import functions
from settings import Settings
from Text import Text
from Tile import Tile
from Roof import Roof

# Cycle
#def cycle(roof_angle, roof_size, diameter, dps, wind, cloud_cover):
    # Change each cycle:
        # Wind velocity
            # 10(sin(x)/x) ?
            # Each cycle randomly decide how much remaining duration the wind has, favor dying out
        # Number of drops hitting roof
            # Random number within range from drops per second median
        # Median drop diameter
            # Random number within range from drop diameter

def main():
    # Initialize simulation
    pygame.init()
    settings = Settings()
    screen = functions.makeScreen("Cloudmap", settings.screen_size, "Images/icon.png", settings.resizable)
    queue = []
    cloudmap_resolution = settings.cloudmap_resolution
    seed = random.randint(50,200)
    print(seed)
    clouds = Cloudmap(seed, cloudmap_resolution)
    clouds.generate()

    #roof = Roof(settings.roof_size, settings.coordinate_resolution / 2, 1, settings.roof_angle)

    # Display cloudmap
    for i in range(0,cloudmap_resolution+1):
        for j in range(0, cloudmap_resolution+1):
            n = clouds.getValue(j,i)
            if n == 1:
                functions.makeTile("", screen, settings, queue, (j,i), "WHITE")
            else:
                functions.makeTile("", screen, settings, queue, (j,i), "BLACK")

    # Cycle
    while True:
        functions.checkEvents(clouds.getMap())

        functions.updateScreen(screen, settings, queue)

main()















