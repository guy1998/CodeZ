import pygame
import time
import player
import game_obj as object
from CodeRun import *

bg_img = pygame.image.load('BG.png')
res = (750, 705)
screen = pygame.display.set_mode(res)
spaceChange = 0

speed = 5
# TODO: YOu do not move thi knight - static position
# TODO: You do not move the tiles - static position
# TODO: How would two non moving objects collide?
# But you move the saww :)

knight = player.player(125, 648, 100, 100)
zombie1 = player.zombie(450, 648, 300, 600)
zombie2 = player.zombie(1050, 648, 900, 1200)
zombie3 = player.zombie(1650, 490, 1640, 1750)
map = object.TileMap('game_map.csv')
saww = object.saw(750, 560, 64, 64)


def redrawWindow(screen, bgX, move_check, screen_scroller):
    screen.blit(bg_img, (bgX, 0))
    map.draw_map(screen, move_check, screen_scroller)
    saww.draw(screen)
    knight.update(map.tiles, screen)
    zombie1.walking_dead(screen, screen_scroller, False)
    zombie2.walking_dead(screen, screen_scroller, False)
    zombie3.walking_dead(screen, screen_scroller, True)
    pygame.display.update()  # updates the screen


def game_screen(speed):
    bg_img = pygame.image.load('BG.png')
    bgX = 0
    beg = 0
    start = time.time()
    while True:

        Font = pygame.font.SysFont('Calibre', 75)
        text = Font.render('Level 1', True, (255, 255, 255))
        screen.blit(text, (res[0] / 5, res[1] / 2))
        pygame.display.update()
        end = time.time()
        if end - start > 2:
            break

    while True:
        move_check = False
        screen_scroller = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



        keys = pygame.key.get_pressed()


        if keys[pygame.K_a] and not (keys[pygame.K_d]) and not (bgX >= 125):
            screen_scroller += speed
            #map.draw_map(screen, speed)
            saww.x += speed
            knight.runningBack = True
            move_check = True
        if keys[pygame.K_d] and not (keys[pygame.K_a]):
            if not (keys[pygame.K_RSHIFT]) or knight.jumping:
                if not (bgX <= -1700):
                    screen_scroller -= speed
                    saww.x -= speed
                    #map.draw_map(screen, -1 * speed)
                    move_check = True
                knight.walking = True
            else:
                if not (bgX <= -1700):
                    screen_scroller -= 3 * speed
                    saww.x += 3 * speed
                    #map.start_x -= 3 * speed
                    move_check = True
                knight.running = True

        if keys[pygame.K_w]:  # If user hits w
            if not knight.jumping:  # If we are not already jumping
                knight.jumping = True

        if keys[pygame.K_z]:
            RunCode()

        bgX += screen_scroller
        redrawWindow(screen, bgX, move_check, screen_scroller)
        knight.attacking = False
        knight.running = False
        knight.runningBack = False
        knight.walking = False
