"""
Contain the class for run the game
"""

import random
import pygame
from pygame.locals import RESIZABLE, QUIT, KEYDOWN, MOUSEBUTTONUP
from . import mac_gyver, garde, element, white_rectangle, porte, mur, menu


class Main:
    """
    Class Main
    """

    @staticmethod
    def run():
        """
        Run the game
        :return:
        """
        pygame.init()

        # FIRST STEP : WE CREATE A EMPTY FIELD

        field = pygame.display.set_mode((750, 750), RESIZABLE)
        background = pygame.Surface(field.get_size())
        background.fill((255, 255, 255))
        field.blit(background, (0, 0))

        # SECOND STEP : WE INITIALIZE LABYRINTH WITH WALL AND PLAYER

        labyrinth_file = open("labyrinthe.txt", "r")
        labyrinth = labyrinth_file.read()
        pos_item_x = 0  # horizontale
        pos_item_y = 0  # verticale
        wall_list = pygame.sprite.Group()
        # list_free_place_for_element is used to have a list with free position (white case)
        # on the field for put elements
        list_free_place_for_element = []

        for level in labyrinth.split("\n"):
            for item_level in level:
                if item_level == '0':
                    my_wall = mur.Wall(pos_item_x, pos_item_y)
                    field.blit(my_wall.image, my_wall.rect)
                    wall_list.add(my_wall)
                elif item_level == 'M':
                    macgyver = mac_gyver.MacGyver('image/macgyver.png', pos_item_x, pos_item_y)
                    field.blit(macgyver.image, macgyver.rect)
                elif item_level == 'G':
                    my_guard = garde.Guard('image/gardien.png', pos_item_x, pos_item_y)
                    field.blit(my_guard.image, my_guard.rect)
                elif item_level == 'P':
                    my_door = porte.Door('image/porte-ouverte.jpg', pos_item_x, pos_item_y - 40)
                    field.blit(my_door.image, my_door.rect)
                else:
                    list_free_place_for_element.append((pos_item_x, pos_item_y))
                pos_item_x += 50
            pos_item_x = 0
            pos_item_y += 50
        pygame.display.flip()

        # THIRD STEP : WE PUT THE TREE ELEMENTS IN FREE PLACE (IN RANDOM WHITE BLOCK)

        tube = element.Element('tube', 'image/tube.jpg')
        needle = element.Element('aiguille', 'image/aiguille.jpg')
        ether = element.Element('ether', 'image/ether.jpg')

        list_elements = [tube, needle, ether]

        for a_element in list_elements:
            # get a random position on the field
            position = random.choice(list_free_place_for_element)
            a_element.rect = a_element.image.get_rect(center=(position[0], position[1]))
            field.blit(a_element.image, a_element.rect)
            # remove the random position for avoid to have 2 elements in same place
            list_free_place_for_element.remove(position)
            pygame.display.flip()

        # FOURTH STEP : STARTING THE GAME

        backgroud_music = pygame.mixer.Sound("musique_fond.wav")
        level_sound = 0.05
        backgroud_music.set_volume(level_sound)
        backgroud_music.play(loops=100)
        in_game = True
        pygame.key.set_repeat(400, 50)
        while in_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    break
                if event.type == KEYDOWN:
                    old_position = macgyver.rect
                    macgyver.move(event.key, wall_list)

                    # we check if macgyver is collided with a element on the field
                    for a_element in list_elements:
                        if pygame.sprite.collide_rect(macgyver, a_element):
                            if a_element not in macgyver.equipment:
                                macgyver.add_element(a_element)
                                print('Vous possedez desormais : ' + a_element.name)
                                noise = pygame.mixer.Sound("bruit.wav")
                                noise.play(loops=0)

                    # we check if macgyver is collided with the guard
                    if pygame.sprite.collide_rect(macgyver, my_guard):
                        if not macgyver.check_all_elements():
                            answer = Main.ending_menu(text='vous avez perdu !')
                            in_game = False

                    # we check if macgyver is open the door. In this case, you win
                    if pygame.sprite.collide_rect(macgyver, my_door):
                        answer = Main.ending_menu(text='vous avez gagné !')
                        in_game = False

                    rectangle = white_rectangle.RectWhite((40, 45), old_position)
                    rectangle.fill((255, 255, 255))
                    field.blit(rectangle, old_position)
            field.blit(macgyver.image, macgyver.rect)

            pygame.display.flip()
        if answer == 'recommencer':
            backgroud_music.stop()
            Main.run()

    @staticmethod
    def ending_menu(text):
        """
        This method create the ending menu for choose if we want play again or exit.
        :param text: depend if we win or lose.
        :return:
        """
        my_message = menu.Menu()
        my_message.add_rect()
        my_message.add_text(text)
        choice_choosed = False
        while not choice_choosed:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if event.pos[1] in range(204, 228):
                        if event.pos[0] in range(99, 225):
                            # On recommence
                            return 'recommencer'
                        elif event.pos[0] in range(395, 460):
                            # On quitte
                            return None
