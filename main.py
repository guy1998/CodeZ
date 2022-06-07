import sys
import pygame
import buttons
import scroll

pygame.init()
clock = pygame.time.Clock()

from pygame import mixer
mixer.init()
mixer.music.load("menu.mp3")
mixer.music.set_volume(0.7)

mixer.music.play()

res = (750, 750)
screen = pygame.display.set_mode(res)
pygame.display.set_caption('CODE-Z')
# using this functions to get the screen width and height
width = screen.get_width()
height = screen.get_height()
bg_img = pygame.image.load('Back.png')  # this function gets an image from a file. The parameter is the image name
bg_img = pygame.transform.scale(bg_img, (width, height))  # this function optimizes the image to fit the whole screen
sb = True
speed = 2
bgX = 0
bgX2 = bg_img.get_width()

def fade():
    fade = pygame.Surface(res)
    fade.fill((0, 0, 0))
    for alpha in range (0, 300):
        fade.set_alpha(alpha)
        screen.fill((255, 255, 255))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

while True:


    mouse = pygame.mouse.get_pos()
    # this function just maps the image's top left corner to the coordinate (0, 0)-top left corner of the screen
    screen.blit(bg_img, (0, 0))
    newGame = buttons.button(270, 70, width/3, height/5, mouse, screen, 'New game', 72,  8, 10)
    newGame.draw()
    newGame_coord = newGame.coordinates()
    continueGame = buttons.button(140, 40, width/2.4, height/3, mouse, screen, 'Continue', 35, 15, 10)
    continueGame.draw()
    options = buttons.button(140, 40, width/2.4, height/2.4, mouse, screen, 'Options', 35, 20, 10)
    options.draw()
    quit = buttons.button(140, 40, width/2.4, height/2, mouse, screen, 'Quit', 35, 40, 10)
    quit.draw()
    q_coord = quit.coordinates()
    mute = buttons.button(70, 20, width/15, height/15, mouse, screen, 'Un/Mute', 15, 15, 5)
    mute.draw()
    m_coord = mute.coordinates()
    instruction = buttons.button(140, 40, width/2.4, height/1.7, mouse, screen, 'Instruction', 35,  5, 10)
    instruction.draw()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if q_coord[0] <= mouse[0] <= q_coord[1] and q_coord[2] <= mouse[1] <= q_coord[3]:
                pygame.quit()
            elif m_coord[0] <= mouse[0] <= m_coord[1] and m_coord[2] <= mouse[1] <= m_coord[3] and sb == True:
                mixer.music.pause()
                sb = False
            elif m_coord[0] <= mouse[0] <= m_coord[1] and m_coord[2] <= mouse[1] <= m_coord[3] and sb == False:
                mixer.music.unpause()
                sb = True
            elif newGame_coord[0] <= mouse[0] <= newGame_coord[1] and newGame_coord[2] <= mouse[1] <= newGame_coord[3]:
                mixer.music.pause()
                fade()
                scroll.game_screen(speed)

    #updates the frames of the game
    pygame.display.update()
