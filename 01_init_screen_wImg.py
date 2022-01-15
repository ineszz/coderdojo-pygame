import pygame

pygame.init()
#define screen display
screen = pygame.display.set_mode([800,600])

keep_going = True
# add image
pic = pygame.image.load("CrazySmile.bmp")
# add background
ground = pygame.image.load("sky.png")

# game event
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             keep_going = False
    screen.blit(ground, (0,0))
    screen.blit(pic, (100,100))
    pygame.display.update()

pygame.quit() # Exit game

