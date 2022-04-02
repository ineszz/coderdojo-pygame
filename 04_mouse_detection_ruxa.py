# cod prezentat de Ruxandra
import pygame

'''
1. Variables
'''
WIDTH = HEIGHT = 300




'''
2. Objects
'''
window = pygame.display.set_mode((WIDTH, HEIGHT))
rectangle = pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 100))


'''
3. Setup
'''
pygame.init()
pygame.display.set_caption('Crash!')
pygame.display.update()
while True:
    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]
    if rectangle.collidepoint(pos) and pressed1:
        print("You have clicked me!")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
