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
import random
from Cloudmap import Cloudmap
from settings import Settings

# Cycle
def cycle():
    # Initialize simulation
    settings = Settings()
    cloudmap_resolution = settings.cloudmap_resolution
    seed = random.randint(50,200)
    clouds = Cloudmap(seed, cloudmap_resolution, settings)
    clouds.generate()

    # Initialize accumulated drops at 0
    drops = 0
    # Iterate over cloudmap, add collected drops for each cloud-covered section of roof
    for row in clouds.map:
        for i in row:
            if i == 1:
                drops += settings.rain_density * settings.cycle_length

    return drops

def main():
    # Initialize accumulated water to 0
    water = 0
    # Perform 100 cycles to represent 100 roofs, new roof dimensions and cloudmap each cycle
    for j in range(0, 100):
        # Increase water by amount collected by the current roof
        water += cycle()

    # Output results
    """file = open("Results.txt", "a+")
    file.write("Accumulated water: {0}\n".format(water))
    file.write("Water per person in 8-member household: {0}\n".format(water / 800))
    file.write("Days of water: {0}\n".format((water / 800) / 59))
    file.close()"""
    print("\nDuring the simulated rainstorm which lasted 10 hours, among 100 houses of random sizes within the range of the average roof size in Kabul, {0} L of water was collected.".format(water))

    print("If each house has Afghanistan's average number of people living in it, which is 8, then this amount of water would provide {0} L of water per person, enough for {1} days.".format(water / 800, (water / 800) / 59))

main()















