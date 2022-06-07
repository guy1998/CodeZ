import pygame

from pygame import mixer


pygame.init()
run = False
running = True
screen = pygame.display.set_mode((800, 650))




mixer.music.load('Music 2.mp3')
mixer.music.play(-1)

font = pygame.font.Font('freesansbold.ttf', 50)
font1 = pygame.font.Font('freesansbold.ttf', 30)
textX = 285
textY = 10

def showscore(x,y):
    scoree = font.render('OPTIONS ', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

def Music(x,y):
    scoree = font.render('Music: ', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))
def Difucilty(x,y):
    scoree = font.render('Difficulty: ', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

def Speedlevell(x,y):
    scoree = font.render('Speed Level: ', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

def tback(x,y):
    scoree = font1.render('back ', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

def Sound(x,y):
    scoree = font.render('Sound:', True, (255, 255 , 255))
    screen.blit(scoree, (x, y))



i=0
n = 0
arr = ['EASY', 'MEDIUM', 'HARD']
speed_level = ['1','2','3','4','5']
def showlevel(x,y,i):
    scoree = font.render(arr[i], True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

def showspeed(x,y,i):
    scoree = font.render(speed_level[i], True, (255, 255 , 255))
    screen.blit(scoree, (x, y))

class Button(pygame.sprite.Sprite):
        def __init__(self, img, scale, x, y):
            super(Button, self).__init__()

            self.image = img
            self.scale = scale
            self.image = pygame.transform.scale(self.image, self.scale)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.clicked = False

        def update_image(self, img):
            self.image = pygame.transform.scale(img, self.scale)

        def draw(self, win):
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not self.clicked:
                    action = True
                    self.clicked = True

                if not pygame.mouse.get_pressed()[0]:
                    self.clicked = False

            screen.blit(self.image, self.rect)
            return action

home = pygame.image.load('More option.png')
home_btn = Button(home, (50, 50), 600, 50)

#Sounds button
volumeon = pygame.image.load('on-button.png')
volumeoff= pygame.image.load('off-button.png')

volume_btn = Button(volumeon, (70, 70), 550, 100)
check = False


#Game music button
sound_on = pygame.image.load('sound on.png')
sound_off = pygame.image.load('sound off.png')
sound_btn = Button(sound_on, (70, 70), 550, 210)
check_2 = False

#Level button
right = pygame.image.load('right .png')
left = pygame.image.load('left.png')

left_btn = Button(left, (50, 50), 470, 363)

#Back button
back = pygame.image.load('back.png')
back_btn = Button(back, (50, 50), 10, 10)

#Speed game button
speedl_btn = Button(left, (50, 50), 520, 500)
speedR_btn = Button(right, (50, 50), 630, 500)



def options_menu(lol):
    n = 0
    while lol:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lol = False
        while running:
            screen.fill((0, 0, 0))

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    lol = False
            # if event.type == pygame.MOUSEBUTTONDOWN and (mouse[0] >= start_c[0] and mouse[0] <= start_c[1]) and (  mouse[1] >= start_c[2] and mouse[1] <= start_c[3]):
                  #   running = False
                 #    run = True

        if home_btn.draw(screen):
            run = True
            running = False


            pygame.display.update()

        while run:
            if i == 1:
                right_btn = Button(right, (50, 50), 740, 363)
            else:
                right_btn = Button(right, (50, 50), 700, 363)
            screen.fill((10,20,30))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    lol = False





            if volume_btn.draw(screen):
                check = not check

                if check:
                    volume_btn.update_image(volumeon)
                    mixer.music.unpause()
            else:
                    volume_btn.update_image(volumeoff)
                    mixer.music.pause()



            if sound_btn.draw(screen):
                check_2 = not check_2

                if check_2:
                    sound_btn.update_image(sound_on)
                else:
                    sound_btn.update_image(sound_off)
            if right_btn.draw(right) :
                i += 1
                if i>2:
                    i=i-1
            if left_btn.draw(left):
                i -=1
                if i<0:
                    i=i+1
            if speedl_btn.draw(left):
                n -= 1
                if(n<0):
                    n +=1
            if speedR_btn.draw(right):
                n += 1
                if(n>4):
                    n -= 1

        if back_btn.draw(right):
            running = True
            run = False



        showscore(textX,textY)
        showlevel(530,363,i)
        showspeed(585,500,n)
        Sound(240,225)
        Difucilty(200, 363)
        Speedlevell(200,500)
        tback(70,20)
        Music(250,115)

        pygame.display.update()

lol = True

options_menu(lol)
