# Import necessary libraries
import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Create a resizable game window with dimensions
screen = pygame.display.set_mode((400, 400), RESIZABLE)

# Set the caption for the game window
pygame.display.set_caption("OpenSims Tech Demo")

# Load the image from the specified file path
image = pygame.image.load('terrain/mapdemo.png')

# Flag to control the game loop
game_running = True

# Flag to check if blue button should be displayed
blue_button_visible = False

# Load the button image
button_image = pygame.image.load("MediumAdultMale.png")

# Get the original dimensions of the image
original_width, original_height = button_image.get_size()

# Calculate the aspect ratio
aspect_ratio = original_width / original_height

# Set the desired button size (50x50)
button_width, button_height = 50, 50

# Scale the image while preserving the aspect ratio
if aspect_ratio > 1:
    # Image is wider than it is tall, scale by width
    new_width = button_width
    new_height = int(button_width / aspect_ratio)
else:
    # Image is taller than it is wide, scale by height
    new_height = button_height
    new_width = int(button_height * aspect_ratio)

button_image = pygame.transform.scale(button_image, (new_width, new_height))

# Red button position and size
red_button_rect = pygame.Rect(200, 200, 50, 50)

# Initialize font for text rendering
pygame.font.init()
font = pygame.font.SysFont(None, 24)

# Main game loop
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if red_button_rect.collidepoint(event.pos):
                # Toggle the visibility of the blue button when red is pressed
                blue_button_visible = not blue_button_visible

    # Draw the image on the screen at the top-left corner (0, 0)
    screen.blit(image, (0, 0))

    # Draw the red button
    red_button = pygame.Surface((50, 50))
    red_button.fill((255, 0, 0))
    screen.blit(red_button, red_button_rect.topleft)

    # Calculate the position to center the scaled image inside the red button
    centered_x = red_button_rect.x + (red_button_rect.width - new_width) // 2
    centered_y = red_button_rect.y + (red_button_rect.height - new_height) // 2

    # Draw the scaled button image, centered inside the red button area
    screen.blit(button_image, (centered_x, centered_y))

    # If the red button is pressed, toggle the blue button and show text 'Interact'
    if blue_button_visible:
        blue_button = pygame.Surface((50, 50))
        blue_button.fill((0, 0, 255))
        screen.blit(blue_button, (red_button_rect.left - 60, red_button_rect.top))
        
        # Render the text 'Interact' on the blue button
        text = font.render('Interact', True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=(red_button_rect.left - 60 + 25, red_button_rect.top + 25))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
