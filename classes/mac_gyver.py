"""
Contain the class for initialize macgyver on the labyrinth.
"""

import pygame
from constante import LEFT, RIGHT, UP, DOWN


class MacGyver(pygame.sprite.Sprite):
    """
    Class MacGyver
    """

    def __init__(self, path_image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.equipment = []
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def check_collision(self, sprites_group):
        """
        This method check if macGyver is collided with wall
        :param sprites_group:
        :return: boolean
        """
        for sprite in sprites_group:
            if pygame.sprite.collide_rect(self, sprite):
                return True
        return False

    def check_collision_element(self, list_elements):
        """
        This method check if macGyver is collided with a element
        :param list_elements:
        :return: element
        """
        for element in list_elements:
            if pygame.sprite.collide_rect(self, element):
                return element
        return False

    def check_all_elements(self):
        """
        this method check if macgyver have all elements for kill the guard
        :return: boolean
        """
        if len(self.equipment) == 3:
            print('Vous avez tout les elements necessaire pour tuer le guardien')
            return True
        return False

    def add_element(self, element):
        """
        add a element on the equipment of macgyver
        :param element:
        :return: None
        """
        self.equipment.append(element)

    def move(self, direction, block_list):
        """
        This methid is used for move macgyver on the field
        :param direction:
        :param block_list:
        :return: None
        """
        new_position = (0, 0)
        old_position = (0, 0)
        if direction == RIGHT:
            new_position = (50, 0)
            old_position = (-50, 0)

        elif direction == LEFT:
            new_position = (-50, 0)
            old_position = (50, 0)

        elif direction == UP:
            new_position = (0, -50)
            old_position = (0, 50)

        elif direction == DOWN:
            new_position = (0, 50)
            old_position = (0, -50)

        self.rect = self.rect.move(new_position[0], new_position[1])
        if self.check_collision(block_list):
            self.rect = self.rect.move(old_position[0], old_position[1])
