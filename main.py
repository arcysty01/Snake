import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    helios = pygame.image.load("daitaku.png")   
    screen.blit(helios, [0,0])
    pygame.draw.rect(screen, [162,203,000], pygame.Rect(150,200,150,150))   
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    
    
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
