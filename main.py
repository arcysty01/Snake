import pygame
import random

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
Delay = 60
RandomX = random.randrange(0, HEIGHT - 20)
RandomY = random.randrange(0, WIDTH - 20)
Visible = True
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if PlayerDirection == "R":
                PlayerDirection = "R"
            else:
                PlayerDirection = "L"
            
        if event.key == pygame.K_RIGHT:
            if  PlayerDirection == "L":
                 PlayerDirection == "L"
            else:
                PlayerDirection = "R"
        if event.key == pygame.K_UP:
            if PlayerDirection == "D":
                PlayerDirection = "D"
            else:
                PlayerDirection = "U"
        if event.key == pygame.K_DOWN:
            if PlayerDirection == "U":
                PlayerDirection == "U"
            else:
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
    player = pygame.draw.rect(screen, "green", pygame.Rect(PlayerX,PlayerY,20,20))   
    
    if Visible == True:
        apple = pygame.draw.rect(screen, "red", pygame.Rect(RandomX, RandomY,20,20)) 
    else:
        RandomY = random.randrange(0, WIDTH - 20)
        RandomX = random.randrange(0, HEIGHT - 20)
        Visible = True


    if PlayerDirection == "L":
        PlayerX -= velocity
    if PlayerDirection == "U":
        PlayerY -=  velocity
    if PlayerDirection == "D":
        PlayerY += velocity
    if PlayerDirection == "R":
        PlayerX += velocity

    

    
    if player.colliderect(apple):
        Visible = False
    

    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.fill("teal")

    clock.tick(30)  # limits FPS to 30

pygame.quit()
