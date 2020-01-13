import pygame


class World(pygame.sprite.Sprite):
    def __init__(self):
        super(World, self).__init__()

        self.spritesheet = pygame.image.load('./assets/tiles.png')
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        self.block_size = 16

        self.ground = get_image(0, 90, 50, 50, self.spritesheet)

    def draw(self, screen):
        # screen.blit(self.spritesheet, (0, 0))

        for i in range(0, self.screen_width, 50):
            for j in range(0, self.screen_height, 50):
                screen.blit(self.ground, (i, j))
                print(i, j)


def get_image(posx, posy, width, height, sprite_sheet):
    """Extracts image from sprite sheet"""
    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))

    return image
