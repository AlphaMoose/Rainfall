# File: gameSettings.py
# Date:    Fri Mar  5 14:51:45 2021
# By:      Matt Myers
#
# ELECTRONIC SIGNATURE
# Matt Myers
#
# The electronic signature above indicates the script
# is my individual work, and I have a general understanding
# of all aspects of its development and execution.
#
# Description: All settings for the game 2048
import random

class Settings():
    def __init__(self):
        # Simulation settings
        self.cloudmap_resolution = 600
        self.rain_density = 1.0 # Drops / meter^2
        self.roof_size = random.randrange(7,15) # Meters, values chosen because their squares fall within the range of average house sizes in Kabul, Afghanistan
        self.cycle_length = 1 # Seconds
        self.drop_volume = .0005 # Liters
        self.average_annual_rainfall = 0.327 # Meters / meter^2



















