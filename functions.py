# File: functions.py
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
# Description: All functions for the Rainfall simulator

# Function to convert pixels to a coordinate system based on the coordinate resolution
def coords(screen, coordinate_resolution, x, y):
    newx = x*(screen.get_width()/coordinate_resolution) - (screen.get_width()/(2*coordinate_resolution))
    newy = y*(screen.get_height()/coordinate_resolution) - (screen.get_height()/(2*coordinate_resolution))

    return newx, newy