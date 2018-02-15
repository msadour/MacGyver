import pygame


class Guard(pygame.sprite.Sprite):
    def __init__(self, path_image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.elements = []
        self.rect = self.image.get_rect(center=(x, y))
