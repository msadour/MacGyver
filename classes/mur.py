"""
Contain the class for initialize a wall on the labyrinth.
"""

import pygame


class Wall(pygame.sprite.Sprite):
    """
    Class Wall
    """

    def __init__(self, pos_x=0, pos_y=0):
        """
        Initalize a wall.
        :param pos_x:
        :param pos_y:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/mur.jpg').convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def get_image(self):
        """
        Get image attribute of wall.
        :return: image
        """
        return self.image

    def get_rect(self):
        """
        Get rect attribute of rectangle.
        :return: rect
        """
        return self.rect
