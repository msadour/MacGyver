import pygame

class Element(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, name, path_image, x, y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load(path_image).convert_alpha()
       self.name = name
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect(center=(x, y))


    def __repr__(self):
        return self.name


    # def apply_transparency(self):
    #     self.copy_image = self.image.copy()
    #     self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)