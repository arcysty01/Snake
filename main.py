import pygame

# pygame setup
pygame.init()
HEIGHT = 800
WIDTH = 600
StartX = HEIGHT / 2
StartY = WIDTH / 2
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Uma")
font = pygame.font.SysFont("Comic Sans MS", 30)
napis = font.render("Umamusume", False, [255,255,255])
pygame.display.flip()
clock = pygame.time.Clock()
running = True
PlayerX = StartX
PlayerY = StartY
PlayerDirection = "L"
velocity = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            PlayerDirection = "L"
        if event.key == pygame.K_RIGHT:
            PlayerDirection = "R"
        if event.key == pygame.K_UP:
            PlayerDirection = "U"
        if event.key == pygame.K_DOWN:
            PlayerDirection = "D"
            
    screen.blit(napis, [330,210])  
    if PlayerY < 0 or PlayerY > WIDTH - 20:
        PlayerY = StartY
        PlayerX = StartX
    if PlayerX < 0 or PlayerX > HEIGHT - 20:
        PlayerX = StartX
        PlayerY = StartY

    helios = pygame.image.load("daitaku.png")   
    screen.blit(helios, [0,0])
    pygame.draw.rect(screen, "red", pygame.Rect(PlayerX,PlayerY,20,20))   
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    if PlayerDirection == "L":
        PlayerX -= velocity
    if PlayerDirection == "U":
        PlayerY -=  velocity
    if PlayerDirection == "D":
        PlayerY += velocity
    if PlayerDirection == "R":
        PlayerX += velocity
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.fill("black")

    clock.tick(30)  # limits FPS to 30

pygame.quit()