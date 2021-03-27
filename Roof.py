# File: Roof.py
# Date:    Wed Mar 24 18:06:10 2021
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
# Roof class for Rainfall

class Roof():
    def __init__(self, size, xa, xb, ya, yb, angle):
        self.size = size
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.angle = angle

    def updatePosition(self, x, y):
        self.x = x
        self.y = y

    # Encapsulation
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y
    def getAngle(self):
        return self.angle
    def setAngle(self, angle):
        self.angle = angle


