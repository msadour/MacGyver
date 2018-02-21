"""
Contain the class for initialize a message on a rectangle.
"""

import pygame


class Menu(object):
    """
    Class Message
    """

    def __init__(self):
        """
        Initalize a message.
        :return:
        """
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600, 400), 0, 32)
        self.screen.fill((255, 255, 255))
        pygame.display.update()
        self.rect = None

    def add_rect(self):
        """
        create white rectangle.
        :return:
        """
        self.rect = pygame.draw.rect(self.screen, (0, 0, 0), (175, 75, 200, 100), 2)
        pygame.display.update()

    def add_text(self, text):
        """
        Add a text in rectangle.
        :param text:
        :return:
        """
        self.screen.blit(self.font.render(text, True, (255, 0, 0)), (200, 100))
        self.screen.blit(self.font.render('recommencer', True, (255, 0, 0)), (100, 200))
        self.screen.blit(self.font.render('quitter', True, (255, 0, 0)), (400, 200))
        pygame.display.update()
