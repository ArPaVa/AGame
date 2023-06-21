import pygame
import Utils
import time

pygame.init()

#a = Utils.Map(8,8)
#b = Utils.Player(*a.random_non_ocuppied_pos())
c = Utils.Game(8,8)

while True:
    time.sleep(1)
    c.paint()
    pygame.display.update()