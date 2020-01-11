import pygame
from Player import Player

# Settings
SIZE = WIDTH, HEIGHT = 800, 600  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('grey')  # The background colod of our window
FPS = 30  # Frames per second


def handle_keys(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        # generate bounds
        if player.x > 0:
            player.move_left()
    elif keys[pygame.K_d]:
        if player.x < WIDTH:
            player.move_right()
    if keys[pygame.K_w]:
        if player.y > 0:
            player.move_up()
    elif keys[pygame.K_s]:
        if player.y < HEIGHT:
            player.move_down()


def main():
    pygame.init()
    pygame.display.set_caption('Sourcerer')
    screen = pygame.display.set_mode(SIZE)
    icon = pygame.image.load('./assets/adventurer-die-00.png')
    pygame.display.set_icon(icon)

    # create the player
    player = Player()
    my_group = pygame.sprite.Group(player)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # handle any movement made by the user
        handle_keys(player)

        # animate player
        my_group.update()

        screen.fill(BACKGROUND_COLOR)

        player.draw(screen)

        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
