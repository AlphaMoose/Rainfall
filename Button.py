# File: Button.py
# Date:    Wed Apr  7 12:59:59 2021
# By:      Matt Myers
# Section: Your Section
# Team:    085
#
# ELECTRONIC SIGNATURE
# Matt Myers
#
# The electronic signature above indicates the script
# is my individual work, and I have a general understanding
# of all aspects of its development and execution.
#
# Description: Button class for Rainfall

import pygame
from Text import Text
import functions

class Button():
    def __init__(self, msg, screen, settings, queue, position, color):
        # Initialize object attributes
        self.msg = msg
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.queue = queue
        self.x = functions.coords(screen, settings.coordinate_resolution, position[0], position[1])[0]
        self.y = functions.coords(screen, settings.coordinate_resolution, position[0], position[1])[1]
        self.color = color

        self.width = len(self.msg) * settings.font_size
        self.height = settings.tile_height

        self.surface = pygame.Surface((self.width, self.height))

    def queueMe(self):
        # Add tile to rendering queue
        self.queue.append(self)
        #self.value_text.queueMe()

    def prep(self):
        # Turn the tile into a rendered image
        self.surface.fill(self.color)

        # Position the tile
        self.tile_rect = self.surface.get_rect()
        self.tile_rect.centerx = self.x
        self.tile_rect.centery = self.y

    def display(self):
        # Draw tile to screen
        self.screen.blit(self.surface, self.tile_rect)

    # Encapsulation
    def getPosition(self):
        return self.x, self.y

    def setPosition(self, position):
        self.position = position

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value








