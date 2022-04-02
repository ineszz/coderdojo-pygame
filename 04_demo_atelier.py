import pygame
import os
'''
1. Variables
'''
BLACK = (0,0,0)
WHITE = (255,255,255)

keepGoing = True

picx = 0
picy = 0
speedx = 5
speedy = 5
picw = 100
pich = 100

paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550

points = 0
lives = 5

'''
2. Objects
'''

'''
3. Setup
'''
pygame.init() # Setup
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Jumping Pong")

pic = pygame.image.load(os.path.join('img_folder', 'p1_jump.png'))
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)

timer = pygame.time.Clock()
font = pygame.font.SysFont("Times", 24)


'''
4. Main Loop
'''
while keepGoing:    # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0:
        speedy = -speedy
    if picy >= 500:
        lives -= 1
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))

    # Draw paddle
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))

    # Check for paddle bounce
    if picy + pich >= paddley and picy + pich <= paddley + paddleh \
       and speedy > 0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + \
           paddlew:
            points += 1
            speedy = -speedy

    # Draw text on screen
    draw_string = "Lives: " + str(lives) + " Points: " + str(points)

    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)

pygame.quit()      # Exit
