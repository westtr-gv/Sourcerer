import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        # adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('./assets/adventurer-run-00.png'))
        self.images.append(pygame.image.load('./assets/adventurer-run-01.png'))
        self.images.append(pygame.image.load('./assets/adventurer-run-02.png'))
        self.images.append(pygame.image.load('./assets/adventurer-run-03.png'))
        self.images.append(pygame.image.load('./assets/adventurer-run-04.png'))
        self.images.append(pygame.image.load('./assets/adventurer-run-05.png'))

        # index value to get the image from the array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        self.x = 15

        self.y = 100

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(self.x, self.y, 50, 37)

    def update(self):
        # when the update method is called, we will increment the index
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]

    def move_right(self):
        print('right')
        self.x += 10

    def move_left(self):
        self.x -= 10
        print(self.x)

    def move_up(self):
        self.y += 10
        print(self.y)

    def move_down(self):
        print('down')
        self.y -= 10
