import sys
import pygame
import buttons

pygame.init()

from pygame import mixer
mixer.init()
mixer.music.load("menu.mp3")
mixer.music.set_volume(0.7)

mixer.music.play()

res = (750, 705)
screen = pygame.display.set_mode(res)

# using this functions to get the screen width and height
width = screen.get_width()
height = screen.get_height()

bg_img = pygame.image.load('cyberstuff.jpg')  # this function gets an image from a file. The parameter is the image name
bg_img = pygame.transform.scale(bg_img, (width, height))  # this function optimizes the image to fit the whole screen
sb = True

while True:


    mouse = pygame.mouse.get_pos()

    # this function just maps the image's top left corner to the coordinate (0, 0)-top left corner of the screen
    screen.blit(bg_img, (0, 0))
    newGame = buttons.button(270, 70, width/3, height/5, mouse, screen, 'New game', 72,  8, 10)
    newGame.draw()
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

    #updates the frames of the game
    pygame.display.update()
