# File: Cloudmap.py
# Date:    Tue Mar 23 16:38:32 2021
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
# Cloudmap class for Rainfall

import random
import math

class Cloudmap():
    def __init__(self, seed, cloudmap_resolution, settings):
        self.seed = seed # Must be an integer greater than 1
        self.cloudmap_resolution = cloudmap_resolution
        self.settings = settings
        self.map = []

    def generate(self): # Function to generate a cloudmap
        # Threshold median, cloud present if within certain range of this value
        threshold_median = 1 / self.seed
        r = math.sqrt(threshold_median)

        # Iterate over the area to produce 2d list to represent cloud cover
        for i in range(0, self.cloudmap_resolution):
            row = []
            for j in range(0, self.settings.roof_size):
                # Generate random
                n = random.random()

                # If n is within range of threshold median, that space has a cloud over it
                if n > threshold_median + 2*r or n < threshold_median - 2*r:
                    row.append(1)
                else:
                    row.append(0)
            self.map.append(row)

    def getMap(self): # Function to return entire cloudmap
        return self.map

    def getValue(self, j, i): # Function to return the value of the cloudmap at (j, i)
        return self.map[i-1][j-1]













