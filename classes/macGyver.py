import pygame

class MacGyver(pygame.sprite.Sprite):

    def __init__(self, path_image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_image).convert_alpha()
        self.elements = []
        self.is_win = False
        self.rect = self.image.get_rect(center=(x,y))
        self.elements = []

    def check_collision(self, sprites_group):
        for sprite in sprites_group:
            if pygame.sprite.collide_rect(self, sprite):
                return True
        return False

    def check_collision_element(self, list_elements):
        for e in list_elements:
            if pygame.sprite.collide_rect(self, e):
                return e
        return False

    def check_win(self):
        if len(self.elements) == 3:
            return True
        else:
            return False

    def add_element(self, element):
        self.elements.append(element)