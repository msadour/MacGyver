"""
Here we where we run the game
"""

from classes import main

if __name__ == "__main__":
    MAIN = main.Main()
    MAIN.run()

# import pygame
# from pygame.locals import *
# from classes import mac_gyver, guard, element, white_rectangle, door, mur, message
# import random
# import constante
# import time
#
#
# pygame.init()
#
# # FIRST STEP : WE GET THE LABIRYNTHE FROM FILE
#
# field = pygame.display.set_mode((750, 750), RESIZABLE)
# background = pygame.Surface(field.get_size())
# background.fill(constante.WHITE)
# field.blit(background, (0, 0))
#
# labirynthe_file = open("labirynthe.txt", "r")
# labirynthe = labirynthe_file.read()
#
# # SECOND STEP : WE INISIALIZ LABIRYNTHE WITH WALL AND PLAYER
#
# pos_item_x = 0 # horizontale
# pos_item_y = 0 # verticale
# wall_list = pygame.sprite.Group()
# # list_free_place_for_element is used to have a list with free position (white case) on the field
# # for put elements
# list_free_place_for_element = []
#
# for level in labirynthe.split("\n"):
#     for item_level in level:
#         if item_level == '0':
#             my_wall = mur.Wall(pos_item_x, pos_item_y)
#             field.blit(my_wall.image, my_wall.rect)
#             wall_list.add(my_wall)
#         elif item_level == 'M':
#             mac_gyver = mac_gyver.MacGyver('image/macgyver.png', pos_item_x, pos_item_y)
#             field.blit(mac_gyver.image, mac_gyver.rect)
#         elif item_level == 'G':
#             my_guard = guard.Guard('image/gardien.png', pos_item_x, pos_item_y)
#             field.blit(my_guard.image, my_guard.rect)
#         elif item_level == 'P':
#             my_door = door.Door('image/porte-ouverte.jpg', pos_item_x, pos_item_y+20)
#             field.blit(my_door.image, my_door.rect)
#         else:
#             list_free_place_for_element.append((pos_item_x, pos_item_y))
#         pos_item_x += 50
#     pos_item_x = 0
#     pos_item_y += 50
# pygame.display.flip()
#
# # THIRD STEP : WE PUT THE TREE ELEMENTS IN FREE PLACE (IN RANDOM WHITE BLOCK)
#
# tube = element.Element('tube', 'image/tube.jpg')
# needle = element.Element('aiguille', 'image/aiguille.jpg')
# ether = element.Element('ether', 'image/ether.jpg')
#
# list_elements = [tube, needle, ether]
#
# for e in list_elements:
#     position = random.choice(list_free_place_for_element) #get a random position on the field
#     e.rect = e.image.get_rect(center=(position[0], position[1]))
#     field.blit(e.image, e.rect)
#     # remove the random position for not have 2 elements in same place
#     list_free_place_for_element.remove(position)
#     pygame.display.flip()
#
# # FOURTH STEP : STARTING THE GAME
#
# backgroud_music = pygame.mixer.Sound("musique_fond.wav")
# level_sound = 0.05
# backgroud_music.set_volume(level_sound)
# backgroud_music.play(loops=100)
#
# pygame.key.set_repeat(400, 50)
# rectangle = None # This rectangle is used to avoid repetitions of macgyver drawing after moving
# in_game = True
# while in_game:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             break
#         if event.type == KEYDOWN:
#             old_position = mac_gyver.rect
#             mac_gyver.move(event.key, wall_list)
#
#             # we check if macgyver is collided with a element on the field
#             for e in list_elements:
#                 if  pygame.sprite.collide_rect(mac_gyver, e):
#                     if e not in mac_gyver.equipment:
#                         mac_gyver.add_element(e)
#                         print('Vous possedez desormais : ' + e.name)
#                         noise = pygame.mixer.Sound("bruit.wav")
#                         noise.play(loops=0)
#
#             # we check if macgyver is collided with the guard
#             if pygame.sprite.collide_rect(mac_gyver, my_guard):
#                 if mac_gyver.check_all_elements():
#                     pass
#                 else:
#                     my_message = message.Message()
#                     my_message.add_rect()
#                     my_message.add_text('vous avez perdu !')
#                     time.sleep(5)
#                     in_game = False
#
#             # we check if macgyver is open the door. In this case, you win
#             if pygame.sprite.collide_rect(mac_gyver, my_door):
#                 if len(mac_gyver.equipment) == 3:
#                     my_message = message.Message()
#                     my_message.add_rect()
#                     my_message.add_text('vous avez gagné !')
#                     time.sleep(5)
#                     in_game = False
#
#             rectangle = white_rectangle.RectWhite((40, 45), old_position)
#             rectangle.fill(constante.WHITE)
#             field.blit(rectangle, old_position)
#     field.blit(mac_gyver.image, mac_gyver.rect)
#
#     pygame.display.flip()
