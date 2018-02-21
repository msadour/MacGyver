"""
Contain the class for initialize a element on the labyrinth.
"""

import pygame


class Element(pygame.sprite.Sprite):
    """
    Class Element
    """
    def __init__(self, name, path_image, pos_x=0, pos_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def get_name(self):
        """
        Get name attribute of element.
        :return: image
        """
        return self.name

    def get_image(self):
        """
        Get image attribute of element.
        :return: image
        """
        return self.image

    def __repr__(self):
        return self.name
