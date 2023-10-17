import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

while True:
    for event in pygame.event.get(): # looks out for any event (interaction happening )
        if event.type == pygame.QUIT: # QUIT = Synonymous to the quit button on the window
            pygame.quit() # opposite of pygame.init(). Closes the entire program.
            exit() 
    
    # draw all of our elements
    # update everything

    pygame.display.update()

