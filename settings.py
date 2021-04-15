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
import pygame
import random
import math
from math import *

class Settings():
    def __init__(self):
        # System settings
        self.monitor = pygame.display.Info()
        self.monitor_width = self.monitor.current_w
        self.monitor_height = self.monitor.current_h

        # Screen settings
        self.screen_scale = 0.5
        self.screen_height = 540 #int(self.screen_scale * self.monitor_height)
        self.screen_width = int(1.25 * self.screen_height)
        self.screen_size = (self.screen_width, self.screen_height)
        self.resizable = pygame.RESIZABLE
        self.coordinate_resolution = 600 # Default coordinate plane resolution
        self.bg_color = (30,30,30)
        self.text_color = (250,250,250)
        self.font_size = 48
        self.font = pygame.font.Font("fonts/VT323-Regular.ttf", self.font_size)
        self.tile_color = (90,90,90)
        self.tile_width = (self.screen_width / self.coordinate_resolution) - (0.25 * (self.screen_width / self.coordinate_resolution))
        self.tile_height = (self.screen_height / self.coordinate_resolution) - (0.25 * (self.screen_height / self.coordinate_resolution))

        # Other simulation settings
        self.cloudmap_resolution = self.coordinate_resolution
        self.rain_density = 1.0 # Drops / meter^2
        self.roof_size = random.randrange(7,15) # Meters, values chosen because their squares fall within the range of average house sizes in Kabul, Afghanistan
        self.cycle_length = 1 # Seconds
        self.drop_volume = .0005 # Liters
        self.average_annual_rainfall = 0.327 # Meters / meter^2



















