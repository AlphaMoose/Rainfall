# File: gameFunctions.py
# Date:    Mon Mar  1 10:27:50 2021
# By:      Matt Myers
#
# ELECTRONIC SIGNATURE
# Matt Myers
#
# The electronic signature above indicates the script
# is my individual work, and I have a general understanding
# of all aspects of its development and execution.
#
# Description: All functions for the game 2048

import pygame,sys,os,statistics
from Tile import Tile
from Text import Text

# Function to create the game screen
def makeScreen(title, screen_size, icon, resizable):
    # Create pygame screen
    screen = pygame.display.set_mode(screen_size, resizable)
    pygame.display.set_caption(title)
    icon = pygame.image.load(icon)
    pygame.display.set_icon(icon)

    # Return window
    return screen

# Function to create grid and score counter
def makeGrid(screen):
    # Create array to store grid values in
    # [row[column]]
    gridArray = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    # Create rectangle on the screen
    #grid = pygame.draw.rect(screen)

    #return grid

# Function to convert pixels to a coordinate system based on the coordinate resolution
def coords(screen, coordinate_resolution, x, y):
    newx = x*(screen.get_width()/coordinate_resolution) - (screen.get_width()/(2*coordinate_resolution))
    newy = y*(screen.get_height()/coordinate_resolution) - (screen.get_height()/(2*coordinate_resolution))

    return newx, newy

# Function to check events
def checkEvents(cloudmap):
    for event in pygame.event.get():
        # Other
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        # Keydowns
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up arrow pressed")
            elif event.key == pygame.K_DOWN:
                print("Down arrow pressed")
            elif event.key == pygame.K_LEFT:
                print("Left arrow pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow pressed")
            elif event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        # Keyups
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Up arrow released")
            elif event.key == pygame.K_DOWN:
                print("Down arrow released")
            elif event.key == pygame.K_LEFT:
                print("Left arrow released")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow released")

# Function to update the window
def updateScreen(screen, settings, queue):
    screen.fill(settings.bg_color)
    for i in queue:
        i.prep()
        i.display()
    pygame.display.flip()

# Function to add a tile
def makeTile(value, screen, settings, queue, position, color):
    tile = Tile(value, screen, settings, queue, position, color)
    tile.queueMe()

    text = Text("{0}".format(value), screen, settings, queue, position)
    text.queueMe()

# Function to delete a tile

# Function to check if two tiles add up
    # Iterate over all tiles, if they match then add them
