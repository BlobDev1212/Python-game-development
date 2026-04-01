import pygame
import sys
import os

def helper(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    return os.path.join(base, relative)


pygame.init()

icon = "assets/red square.jpg"
logo = pygame.image.load(helper(icon))
pygame.display.set_icon(logo)

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()