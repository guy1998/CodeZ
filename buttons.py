import pygame

def drawRoundedRect(screen, x, y, colour=(128,128,128), radius=7, box_w=0, box_h=0):
    pygame.draw.circle(screen, colour, (x+radius, y+radius), radius)                  # TL corner
    pygame.draw.circle(screen, colour, (x+box_w-radius-1, y+radius), radius)          # TR corner
    pygame.draw.circle(screen, colour, (x+radius, y+box_h-radius-1), radius)         # BL corner
    pygame.draw.circle(screen, colour, (x+box_w-radius-1, y+box_h-radius-1), radius)  # BR corner
    # In-fill
    pygame.draw.rect(screen, colour, (x+radius, y, box_w-(2*radius), box_h))
    pygame.draw.rect(screen, colour, (x, y+radius, box_w, box_h-(2*radius)))


class button:
    def __init__(self, width, height, x, y, mouse, screen, text, size, margins_x, margins_y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.mouse = mouse
        self.screen = screen
        self.text = text
        self.margins_x = margins_x
        self.margins_y = margins_y
        self.size = size

    def draw(self):
        Font = pygame.font.SysFont('Calibre', self.size)
        txt = Font.render(self.text, True, (255, 255, 255))
        if self.x <= self.mouse[0] <= self.x + self.width and self.y <= self.mouse[1] <= self.y + self.height:
            drawRoundedRect(self.screen, self.x, self.y, (0, 153, 153), radius=7, box_w=self.width, box_h=self.height)
        else:
            drawRoundedRect(self.screen, self.x, self.y, (0, 204, 204), radius=7, box_w=self.width, box_h=self.height)

        self.screen.blit(txt, (self.x + self.margins_x, self.y + self.margins_y))

    def coordinates(self):
        coord = [self.x, self.x+self.width, self.y, self.y + self.height]
        return coord

