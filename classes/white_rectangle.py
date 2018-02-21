"""
Contain the class for initialize a white rectangle when macgyver move.
"""

import pygame


class RectWhite(pygame.Surface):
    """
    Class RectWhite
    """

    def __init__(self, size, position):
        """
        Initalize a white rectangle.
        :param size:
        :param position:
        """
        pygame.Surface.__init__(self, size)
        self.rect = pygame.Rect(position)
        self.position = position
        self.size = size

    def get_rect(self):
        """
        Get rect attribute of rectangle.
        :return:
        """
        return self.rect

    def get_position(self):
        """
        Get position attribute of rectangle.
        :return:
        """
        return self.position

    def get_size(self):
        """
        Get size attribute of rectangle.
        :return:
        """
        return self.size
