import os
import csv
import pygame


def read_csv(filename):
    map = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    return map


def drawRoundedRect(screen, x, y, colour=(128, 128, 128), radius=7, box_w=0, box_h=0):
    pygame.draw.circle(screen, colour, (x + radius, y + radius), radius)  # TL corner
    pygame.draw.circle(screen, colour, (x + box_w - radius - 1, y + radius), radius)  # TR corner
    pygame.draw.circle(screen, colour, (x + radius, y + box_h - radius - 1), radius)  # BL corner
    pygame.draw.circle(screen, colour, (x + box_w - radius - 1, y + box_h - radius - 1), radius)  # BR corner
    # In-fill
    pygame.draw.rect(screen, colour, (x + radius, y, box_w - (2 * radius), box_h))
    pygame.draw.rect(screen, colour, (x, y + radius, box_w, box_h - (2 * radius)))



