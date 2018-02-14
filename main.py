import pygame
from pygame.locals import *
import pickle
import os
from classes import block, macGyver, guard, element, white_rectangle
import random

pygame.init()
#all_sprites = pygame.sprite.Group() # ship sprites + player sprite

#FIRST STEP : WE GET THE LABIRYNTHE FROM FILE
field = pygame.display.set_mode((750, 700), RESIZABLE)
background = pygame.Surface((field.get_size()))
background.fill((255, 255, 255))
field.blit(background, (0,0))

labirynthe_file = open("labirynthe.txt", "r")
labirynthe = labirynthe_file.read()

# SECOND STEP : WE INISIALIZ LABIRYNTHE WITH BLOCK AND PLAYER
pos_item_x = 0 #horizontale
pos_item_y = 0 #verticale
block_list = pygame.sprite.Group() # just ship sprites
mac_gyver_list = pygame.sprite.Group()
list_free_place_for_element = []

for level in labirynthe.split("\n"):
    for item_level in level:
        if item_level == '0':
            my_block = block.Block((0, 0, 0), 50, 50, pos_item_x , pos_item_y)
            field.blit(my_block.image, my_block.rect)
            block_list.add(my_block)
        elif item_level == 'M':
            mac_gyver = macGyver.MacGyver('image/macgyver.png', pos_item_x, pos_item_y)
            field.blit(mac_gyver.image, mac_gyver.rect)
            mac_gyver_list.add(mac_gyver)
        elif item_level == 'G':
            my_guard = guard.Guard('image/gardien.png', pos_item_x, pos_item_y)
            field.blit(my_guard.image, my_guard.rect)
        else :
            list_free_place_for_element.append((pos_item_x, pos_item_y))
        pos_item_x += 50
    pos_item_x=0
    pos_item_y += 50
pygame.display.flip()

# THIRD STEP : WE PUT THE TREE ELEMENTS IN FREE PLACE (IN RANDOM WHITE BLOCK)

position_ether = random.choice(list_free_place_for_element)
ether = element.Element('ether', 'image/ether.jpg', position_ether[0], position_ether[1])
field.blit(ether.image, ether.rect)
#I remove this position for be sure to don't have some position for differents elements
list_free_place_for_element.remove(position_ether)

position_needle = random.choice(list_free_place_for_element)
needle = element.Element('aiguille', 'image/aiguille.jpg', position_needle[0], position_needle[1])
field.blit(needle.image, needle.rect)
list_free_place_for_element.remove(position_needle)

position_tube = random.choice(list_free_place_for_element)
tube = element.Element('tube', 'image/tube.jpg', position_tube[0], position_tube[1])
field.blit(tube.image, tube.rect)
list_free_place_for_element.remove(position_tube)
pygame.display.flip()

list_elements = [tube, needle, ether]

pygame.key.set_repeat(400, 50)
rectangle = None
#collided_element = lambda m, l : m.check_collision_element(l)
in_game = True
while in_game:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            break
        if event.type == KEYDOWN:
            old_position = mac_gyver.rect

            if event.key == K_DOWN:
                mac_gyver.rect = mac_gyver.rect.move(0, 10)
                if mac_gyver.check_collision(block_list):
                    mac_gyver.rect = mac_gyver.rect.move(0, -10)
                rectangle = white_rectangle.RectWhite((40, 45), old_position)

            if event.key == K_UP:
                mac_gyver.rect = mac_gyver.rect.move(0, -10)
                if mac_gyver.check_collision(block_list):
                    mac_gyver.rect = mac_gyver.rect.move(0,10)
                rectangle = white_rectangle.RectWhite((40, 45), old_position)

            if event.key == K_LEFT:
                mac_gyver.rect = mac_gyver.rect.move(-10, 0)
                if mac_gyver.check_collision(block_list):
                    mac_gyver.rect = mac_gyver.rect.move(10, 0)
                rectangle = white_rectangle.RectWhite((40, 45), old_position)

            if event.key == K_RIGHT:
                mac_gyver.rect = mac_gyver.rect.move(10, 0)
                if mac_gyver.check_collision(block_list):
                    mac_gyver.rect = mac_gyver.rect.move(-10, 0)
                rectangle = white_rectangle.RectWhite((40, 45), old_position)

            for e in list_elements:
                if  pygame.sprite.collide_rect(mac_gyver, e):
                    if e not in mac_gyver.elements:
                        mac_gyver.add_element(e)

            if pygame.sprite.collide_rect(mac_gyver, my_guard):
                if mac_gyver.check_win():
                    print('felicitation vous avez gagné !')
                else:
                    print('vous avez perdu !')
                in_game = False

            rectangle.fill((255, 255, 255))
            field.blit(rectangle, old_position)
    field.blit(mac_gyver.image, mac_gyver.rect)

    pygame.display.update()
    # Rafraichissement
    pygame.display.flip()
