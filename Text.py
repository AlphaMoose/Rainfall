# File: Text.py
# Date:    Tue Mar  9 13:24:15 2021
# By:      Matt Myers
#
# ELECTRONIC SIGNATURE
# Matt Myers
#
# The electronic signature above indicates the script
# is my individual work, and I have a general understanding
# of all aspects of its development and execution.
#
# Description: Text class for the game 2048
import functions

class Text():
    def __init__(self, text, surface, settings, queue, position):
        # Initialize object attributes
        self.text = text
        self.surface = surface
        self.surface_rect = self.surface.get_rect()
        self.settings = settings
        self.queue = queue
        self.x = functions.coords(surface, settings.coordinate_resolution, position[0], position[1])[0]
        self.y = functions.coords(surface, settings.coordinate_resolution, position[0], position[1])[1]

        # Initialize text settings
        self.font = settings.font
        self.text_color = settings.text_color

    def queueMe(self):
        # Add text to render queue
        self.queue.append(self)

    def prep(self):
        # Turn the text into a rendered image
        self.text_image = self.font.render(self.text, True, self.text_color)

        # Position the text
        self.text_rect = self.text_image.get_rect()
        self.text_rect.centerx = self.x
        self.text_rect.centery = self.y

    def display(self):
        # Draw text to screen
        self.surface.blit(self.text_image, self.text_rect)

    # Encapsulation
    def getPosition(self):
        return self.x, self.y

    def setPosition(self, position):
        self.position = position

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value