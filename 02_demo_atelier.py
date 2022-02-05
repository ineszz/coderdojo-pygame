import pygame

pygame.init()

# 1. definesc screen
screen = pygame.display.set_mode([800,600])

#definesc titlul afisat pe ecran
pygame.display.set_caption("Primul joc in python @ CoderDojo Bucuresti")


ORANGE =  (224, 224, 235) 
BLUE  = (0, 0, 255)
GREEN = (0, 153, 0) 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
radius = 100
circ_pos = (100,100)

screen.fill( ORANGE )

# bucla joc
keep_going = True
# adaug poza
pic = pygame.image.load("CrazySmile.bmp")


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             keep_going = False

    #elemente grafice
    pygame.draw.line(screen, BLUE, (350,230), (350,270))
    pygame.draw.line(screen, BLUE, (450,230), (450,270))
    pygame.draw.line(screen, GREEN, (130,170), (170,170))
    pygame.draw.circle(screen, WHITE, (100,50), 100)
    pygame.draw.circle(screen, BLACK, (200,50), 30)
    pygame.draw.rect(screen, RED, (100, 200, 100, 50), 2)
    pygame.draw.rect(screen, RED, (200, 400, 200, 105), 20)
    pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))
    pygame.draw.circle(screen, GREEN, circ_pos, radius)
    # text simplu afisat pe ecran 
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Python Bucharest Coder Dojo Team", True, GREEN)
    screen.blit(text, [350, 50])


    screen.blit(pic, (350,250))
    pygame.display.update()

pygame.quit() # Exit game
