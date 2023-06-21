import numpy as np
import pygame
import pickle


class Map:  #have a map
    def __init__(self,x_size,y_size):
        self.map_matrix = np.zeros(shape=(x_size,y_size),dtype=int)
        for i in range(self.map_matrix.shape[0]):
            if i>=  self.map_matrix.shape[1]/2:
                for j in range(self.map_matrix.shape[1]):
                    self.map_matrix[i,j]= 1
        print(self.map_matrix)
    def random_non_ocuppied_pos(self):
        #TODO I know
        for i in range(self.map_matrix.shape[0]):
            for j in range(self.map_matrix.shape[1]):
                if self.map_matrix[i,j]==0:
                    return i,j

class Player:
    def __init__(self,initial_x, initial_y):
        self.pos_x = initial_x
        self.pos_y = initial_y
    def act_map (self, map:Map):
        #not sure if is going to work that way
        pass
    def __str__(self):
        return f"{self.pos_x},{self.pos_y}"
    
class Settings:
    def __init__(self):
        try:
            file = open("settings.bin","rb")
            settings = pickle.load(file)
            if self.corrupted_settings(settings):
                file.close()
                self.initialize_settings()
                file = open("settings.bin","rb")
                settings = pickle.load(file)
            self.settings = settings
            file.close() 
        except:
            try:
                file.close()
            except:
                pass
            self.initialize_settings()
            file = open("settings.bin","rb")
            settings = pickle.load(file)
            self.settings = settings
            file.close() 
            
    def initialize_settings(self):
        settings = dict()
        settings["resolution"]=(1280,720)
        file = open("settings.bin","wb")
        pickle.dump(settings,file)
        file.close()

    def provide_settings(self,especific_setting):
        return self.settings[especific_setting]

    def corrupted_settings ():
        #TODO Checking if the settings are valid
        return True
        

class Game:
    def __init__(self,map_x_size,_map_y_size):
        self.settings = Settings()
        self.map = Map(map_x_size,_map_y_size)
        self.player = Player(*self.map.random_non_ocuppied_pos())
    def paint(self):
        pygame.init()
        window = pygame.display.set_mode(self.settings.provide_settings("resolution"))
        window.fill((255,255,255))
        pygame.draw.rect(window,(0,0,255),[100,100,400,100],2)
        return window

