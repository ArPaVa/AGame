import pygame
import Utils

pygame.init()
#a = Utils.Map(8,8)
#b = Utils.Player(*a.random_non_ocuppied_pos())
c = Utils.Game(8,8)
while True:
    c.paint()
    pygame.display.update()