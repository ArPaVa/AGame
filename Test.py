import pygame
import Utils
import time

pygame.init()

#a = Utils.Map(8,8)
#b = Utils.Player(*a.random_non_ocuppied_pos())
c = Utils.Game(90,160)
screen = pygame.display.set_mode(c.settings.provide_settings("resolution"))
while True:
    dump = pygame.event.get() #FUCKING PYGAME AND WINDOWS FUCKINGLE THINK PYGAME IS NOT RESPONDING IF YOU DONT INTERACT WITH THE EVENTS FOR TOO LONG
    time.sleep(0.3)
    keys = pygame.key.get_pressed()
    c.recieve_input(keys)
    c.paint(screen)
    pygame.display.flip()
