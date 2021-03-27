# File: Drop.py
# Date:    Tue Mar 23 16:07:01 2021
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
# Raindrop class for Rainfall
import math

class Drop():
    def __init__(self, diameter, position):
        self.diameter = diameter
        self.position = position
        self.volume = (4/3) * math.pi * ((diameter / 2))^3

    # Encapsulation
    def getDiameter(self):
        return self.diameter
    def setDiameter(self, diameter):
        self.diameter = diameter
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getVolume(self):
        return self.volume
    def setVolume(self, volume):
        self.volume = volume