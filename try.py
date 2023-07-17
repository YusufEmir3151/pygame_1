import pygame

pygame.init()

WIDTH_HEIGHT = (500, 500)

window = pygame.display.set_mode(WIDTH_HEIGHT)


start = True
while start:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            start = False