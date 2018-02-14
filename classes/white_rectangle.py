import pygame
from pygame.locals import *

class RectWhite(pygame.Surface):
    def __init__(self, size, position):
        pygame.Surface.__init__(self, size)
        self.rect = pygame.Rect(position)
        self.position = position
        self.size = size

    def get_rect(self):
        return self.rect