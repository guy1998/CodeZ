import pygame
import os
from utils import read_csv


class saw():
    # TODO : What is saw anyway?
    img = [pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW0.png')), (64, 64)),
           pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW1.png')), (64, 64)),
           pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW2.png')), (64, 64)),
           pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW3.png')), (64, 64))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0
        self.safespot = x

    def draw(self, screen):
        if self.count >= 8:
            self.count = 0
        screen.blit(self.img[self.count // 2], (self.x, self.y))
        self.count += 1

    def update_position(self, change):
        if change == -45:
            # TODO Wtf do you mean with this? safespot = x in init()?
            # TODO God's sake this is under construction bro.
            self.x = self.safespot
        else:
            self.x += change


class Tile():
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(pygame.image.load(image), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, hitbox):
        print('Player Hit-box: ', hitbox)
        print('Tile Rectangle: ', self.rect)
        print()
        if self.rect.x <= hitbox[0] + hitbox[2] <= self.rect.x + 32:
            if hitbox[1] + hitbox[3] > self.rect.y:
                if hitbox[1] < 32 + self.rect.y:
                    return True
        return False


class TileMap():
    def __init__(self, filename):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        #self.load_map()

    def draw_map(self, surface, move_check, screen_scroller):
        for tile in self.tiles:
            if move_check:
                tile.rect.x += screen_scroller
            surface.blit(tile.image, (tile.rect.x, tile.rect.y + 558))

    #def draw_map(self, surface, bgX):
        #surface.blit(self.map_surface, (bgX, 558))

    #def load_map(self):
        #for tile in self.tiles:
            #tile.draw(self.map_surface)

    def load_tiles(self, filename):
        tiles = []
        tile_path = 'Tile (1).png'
        tile_map = read_csv(filename)

        for y, row_map in enumerate(tile_map):
            # Move to next row
            for x, tile in enumerate(row_map):
                # Move to next tile in current row
                if tile == '-1':
                    self.start_x = x * self.tile_size
                    self.start_y = y * self.tile_size
                else:
                    if tile == '1' or tile == '2':
                        tile_path = 'Tile (2).png'
                    elif tile == '0':
                        tile_path = 'Tile (1).png'
                    elif tile == '3' or tile == '6':
                        tile_path = 'Tile (4).png'
                    elif tile == '4' or tile == '7' or tile == '8':
                        tile_path = 'Tile (5).png'
                    tiles.append(Tile(os.path.join('Tiles', tile_path), x * self.tile_size, y * self.tile_size))

        # Store the size of the tile map
        self.map_w, self.map_h = len(tile_map[-1]) * self.tile_size, len(tile_map) * self.tile_size
        return tiles
