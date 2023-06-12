import pygame
import Utils

a = Utils.Map(8,8)
b = Utils.Player(*a.random_non_ocuppied_pos())
print(b)