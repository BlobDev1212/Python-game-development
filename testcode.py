import pygame, sys

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('cool game')
icon = pygame.image.load("downloads/New folder/red square.jpg")
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()