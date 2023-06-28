import pygame
import Utils
import time

pygame.init()

#a = Utils.Map(8,8)
#b = Utils.Player(*a.random_non_ocuppied_pos())
c = Utils.Game(90,160)
gaming = True
screen = pygame.display.set_mode(c.settings.provide_settings("resolution"))
while gaming:
    events = pygame.event.get() #FUCKING PYGAME AND WINDOWS FUCKINGLE THINK PYGAME IS NOT RESPONDING IF YOU DONT INTERACT WITH THE EVENTS FOR TOO LONG
    time.sleep(0.05)

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            gaming = False

    if gaming:
        keys_pressed = pygame.key.get_pressed()     
        c.recieve_input_pressed(keys_pressed)
        c.recieve_input_keydown(events)
        c.paint(screen)
        check = pygame.mouse.get_pressed()
        if check[0]:
            c.on_click_dirt(pygame.mouse.get_pos())
        pygame.display.flip()
