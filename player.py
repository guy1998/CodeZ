import pygame
import os

class player(object):

    run = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Run (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    jump = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Jump (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    walk = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Walk (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    idle = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Idle (' + str(x) + ').png')), (75, 75)) for x in range(1, 9)]
    runBack = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'RunBack (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    attack = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Attack (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]

    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.jumpCount = 0
        self.jumpCount = 0
        self.running = False
        self.runningBack = False
        self.runCount = 0
        self.idleCount = 0
        self.walking = False
        self.walkCount = 0
        self.hit_box = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.attacking = False
        self.attCount = 0
        self.coolDown = True

    def draw(self, screen):
            if self.attacking and self.coolDown:
                if self.attCount > 42:
                    self.attCount = 0
                screen.blit(self.attack[self.attCount // 6], (self.x, self.y))
                self.attCount += 1
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 13))
                self.coolDown = False
            elif self.jumping:
                self.y -= self.jumpList[self.jumpCount] * 1.2
                screen.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
                self.jumpCount += 1
                if self.jumpCount > 108:
                    self.jumpCount = 0
                    self.jumping = False
                    self.runCount = 0
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))

            elif self.running:
                if self.runCount > 42:
                    self.runCount = 0
                screen.blit(self.run[self.runCount // 6], (self.x, self.y))
                self.runCount += 1
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 13))

            elif not(self.running) and not(self.runningBack) and not(self.walking):
                if self.idleCount > 42:
                    self.idleCount = 0
                screen.blit(self.idle[self.idleCount // 6], (self.x, self.y))
                self.idleCount += 1

            elif self.runningBack:
                if self.runCount > 42:
                    self.runCount = 0
                screen.blit(self.runBack[self.runCount // 6], (self.x, self.y))
                self.runCount += 1
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))

            elif self.walking:
                if self.walkCount > 42:
                    self.walkCount = 0
                screen.blit(self.walk[self.walkCount // 6], (self.x, self.y))
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))
                self.walkCount += 1

    def get_hits(self, tiles):
        hits = []
        new_tiles = filter(lambda tile: self.hit_box[0]+self.hit_box.width >= tile.rect.x >= self.hit_box[0] and tile.rect.y < 159, tiles)
        for new_tile in list(new_tiles):
            new_tile.rect[1] += 558
            if self.hit_box.colliderect(new_tile.rect):
                hits.append(new_tile.rect)
            new_tile.rect[1] -= 558
        return hits

    def checkCollisionsx(self, collisions):
        for tile in collisions:
            # Hit tile moving right
            # Fixme
            if self.x < tile.x and (self.walking or self.running):
                self.x = self.x
            # Hit tile moving left
            elif self.runningBack:
                self.x = self.x

    def checkCollisionsy(self, collisions):
        for tile in collisions:
            if self.jumpList[self.jumpCount] * 1.2 < 0:  # Hit tile from the top
                self.jumping = False
                self.y = tile.y - self.height + 598
            '''
            # Hit tile from the bottom
            elif self.y > tile.y - 10:
                self.y = self.height + 548
                self.jumping = False
            '''

    def checkCollisions(self, tiles):
        collisions = self.get_hits(tiles)
        if len(collisions) == 0 and not self.jumping and (self.walking or self.running or self.runningBack):
            self.y = tiles[-1].rect.y - self.height + 598  # self.height + 548
            return
        if self.jumping:
            self.checkCollisionsy(collisions)
        elif self.walking or self.running or self.runningBack:
            self.checkCollisionsx(collisions)

    def update(self, tiles, screen):
        self.draw(screen)
        self.checkCollisions(tiles)


class zombie(object):


    walk = [pygame.transform.scale(pygame.image.load(os.path.join("zombies", 'Walk (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    walk_back = [pygame.transform.scale(pygame.image.load(os.path.join("zombies", 'Walk_back (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]

    def __init__(self, x, y, c1, c2):
        self.x = x
        self.y = y
        self.walking = True
        self.walking_back = False
        self.range = [c1, c2]
        self.dead = False
        self.walkCount = 0

    def walking_dead(self, screen, screen_scroller, boolean):
        if boolean:
            speed = 0.2
        else:
            speed = 1

        if self.walking:
            if self.x > self.range[1]:
                self.walking = False
                self.walking_back = True
                self.walkCount = 0
            if self.walkCount > 42:
                self.walkCount = 0
            screen.blit(self.walk[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1
            self.x = self.x + speed + screen_scroller
            self.range[0] += screen_scroller
            self.range[1] += screen_scroller

        if self.walking_back:
            if self.x < self.range[0]:
                self.walking_back = False
                self.walking = True
                self.walkCount = 0
            if self.walkCount > 42:
                self.walkCount = 0
            screen.blit(self.walk_back[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1
            self.x = self.x - speed + screen_scroller
            self.range[0] += screen_scroller
            self.range[1] += screen_scroller