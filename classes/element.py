import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, name, path_image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect(center=(x, y))

    def __repr__(self):
        return self.name
