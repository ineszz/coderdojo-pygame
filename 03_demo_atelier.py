
import pygame
import os
'''
1. Variables
'''

x = 960
y = 520
main = True

'''
2. Objects
'''
# definim player
playerImg = pygame.image.load('img_folder/p1_jump.png')
playerX = 370
playerY = 300
def player(x,y):
    screen.blit(playerImg, (x, y) )   

'''
3. Setup
'''
pygame.init()
screen = pygame.display.set_mode([x, y])
# screen = pygame.display.set_mode([x, y], pygame.RESIZABLE)
pygame.display.set_caption("Primul joc in python @ CoderDojo Bucuresti")
#
backdrop = pygame.image.load(os.path.join('img_folder', 'bg2.jpg')).convert()
backdropbox = screen.get_rect()
#
icon = pygame.image.load(os.path.join('img_folder', 'cd_buc.png')).convert()
iconbox = icon.get_rect(center=(55, y-55))

'''
4. Main Loop
'''
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # add player movements    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] :
                playerX += 20
        if keys[pygame.K_LEFT] :
                playerX -= 20
        if keys[pygame.K_UP] :
                playerY -= 20
        if keys[pygame.K_DOWN] :
                playerY += 20

    screen.blit(backdrop, backdropbox)
    screen.blit(icon, iconbox)
    player(playerX, playerY)
    pygame.display.update()
    

pygame.quit() # Exit game
