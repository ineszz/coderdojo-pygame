import pygame

pygame.init()


# definesc screen display
screen = pygame.display.set_mode([800,600])

# definesc culorile 
# unde gasesc informatii despre culor? https://www.pygame.org/docs/ref/color.html
# color picker tool: https://www.w3schools.com/colors/colors_picker.asp

GREEN = (0,255,0)    # RGB color triplet for GREEN
RED =  (255, 0, 0)   # Red
WHITE =  (255, 255, 255)

screen.fill( GREEN )  # Green
pygame.display.update()

#variabila booleana activare event inchidere fereastra
keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             keep_going = False
     

pygame.quit() # Exit game
