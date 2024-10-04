import os
import sys
import pygame as py
from pygame.locals import QUIT

py.init()

MESSAGE_FONT = py.font.SysFont('Arial', 35)

WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)

message = "Hello World"
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Bagas Sukmanyo")

def draw_window() -> None:
    message_text = MESSAGE_FONT.render(message, True, WHITE)
    screen.blit(message_text, (WIDTH/2 - message_text.get_width()/2, HEIGHT/2 - message_text.get_height()/2))

    py.display.update()

while True:
    for event in py.event.get():
        if type == QUIT:
            py.quit()
            sys.exit()

    draw_window()