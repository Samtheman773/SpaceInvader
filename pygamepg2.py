import pygame


#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anyhting from last frame
    screen.fill("green")

    #RENDER YOUR GAME HERE
    # flip() the display to put work on screen
    pygame.display.flip()

    clock.tick()
