import pygame

from pygame.sprite import Sprite

from random import randint

class Stars(Sprite):
    """A class represent one star on the screen."""


    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.rect = self.image.get_rect()

        # Start all the new star at ramdom place.
        self.rect.x = randint(self.rect.width, 1200)
        self.rect.y = randint(self.rect.height, 800)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

