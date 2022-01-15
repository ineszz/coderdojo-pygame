import pygame

pygame.init()

BACKGROUND_COL = [0,0,255]
# definesc screen display
SIZE = [800, 600]
screen = pygame.display.set_mode(SIZE)
# definesc titlul afisat pe ecran
pygame.display.set_caption("Primul joc in python @ CoderDojo Bucuresti")

keep_going = True
# add image
pic = pygame.image.load("CrazySmile.bmp")

# game event
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             keep_going = False
    screen.fill(BACKGROUND_COL)
    screen.blit(pic, (350,100))
    pygame.display.update()

pygame.quit() # Exit game
