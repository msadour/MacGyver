"""
Contain the class for initialize a door on the labyrinth.
"""

import pygame


class Door(pygame.sprite.Sprite):
    """
    Class Door
    """

    def __init__(self, path_image, pos_x, pos_y):
        """
        Init a door.
        :param path_image:
        :param pos_x:
        :param pos_y:
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def get_door_image(self):
        """
        Get image attribute of door.
        :return: image
        """
        return self.image

    def get_door_rect(self):
        """
        Get rect attribute of door.
        :return:
        """
        return self.rect
