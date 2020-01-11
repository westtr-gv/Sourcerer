import pygame, sys

pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))

black = (0, 0, 0)

# Caption and Icon
pygame.display.set_caption('Sourcerer')
icon = pygame.image.load('./sprites/adventurer-cast-00.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./sprites/adventurer-cast-00.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg,(100,100))

# Game Loop
running = True
while running:
    screen.fill(black) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 
            quit()


    player()
    pygame.display.flip()