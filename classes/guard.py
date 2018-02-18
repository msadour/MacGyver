"""
Contain the class for initalize the guard on the labirynthe.
"""

import pygame


class Guard(pygame.sprite.Sprite):
    """
    Class Guard
    """

    def __init__(self, path_image, pos_x, pos_y):
        """
        Initialize a guard.
        :param path_image:
        :param pos_x:
        :param pos_y:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def set_image(self, path_image):
        """
        set image of guard when he die.
        :param path_image:
        :return:
        """
        self.image = pygame.image.load(path_image).convert_alpha()

    def get_image(self):
        """
        Get image attribute of guard.
        :return: image
        """
        return self.image

    def get_rect(self):
        """
        Get rect attribute of rectangle.
        :return:
        """
        return self.rect
