import numpy as np
import pygame
import pickle

# NOTA X es vertical y Y horizontaL
class Map:  #have a map

    def __init__(self,x_size,y_size):
        self.map_matrix = np.zeros(shape=(x_size,y_size),dtype=Block)
        for i in range(self.map_matrix.shape[0]):         
            for j in range(self.map_matrix.shape[1]):
                if i>=  self.map_matrix.shape[0]/2:
                    self.map_matrix[i,j]= Dirt()
                else:
                    self.map_matrix[i,j]= Air()
            
        print(self.map_matrix)
    
    
    def valid_posc(self,x,y):
        if x>-1 and x < self.map_matrix.shape[0] and y>-1 and y < self.map_matrix.shape[1]:
            return True
        return False

    def random_non_ocuppied_pos(self):
        #TODO I know
        for i in range(self.map_matrix.shape[0]):
            for j in range(self.map_matrix.shape[1]):
                if isinstance(self.map_matrix[i,j],Air):
                    #return i,j
                    return 0,2
    #TODO Maybe make subscriptable giving the map_matrix thingy

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
        
class Block:
    density = 1
    breakable = True
    directory = None
    def __repr__(self) -> str:
        return self.__str__()

class Dirt (Block):
    density = 1
    breakable = True
    directory = (150,100,100)
    def __str__(self) -> str:
        return 'D'

class Air(Block):
    density = 0
    breakable = False
    directory = (30,30,100)
    def __str__(self) -> str:
        return 'A'
class Game:
    def __init__(self,map_x_size,_map_y_size):
        self.settings = Settings()
        self.map = Map(map_x_size,_map_y_size)
        self.player = Player(*self.map.random_non_ocuppied_pos())
        #self.screen = pygame.display.set_mode(self.settings.provide_settings("resolution"))
        self.move_ticker = 0
    def paint(self,window):
        #window = pygame.Surface(self.settings.provide_settings("resolution"))
        temporal_materials = dict()
        temporal_materials[0] = (30,30,100)
        temporal_materials[1] = (150,100,100)
        temporal_materials[-1]= (150,70,70)
        
        # rect_height = self.settings.provide_settings("resolution")[0]/self.map.map_matrix.shape[0]
        # rect_width = self.settings.provide_settings("resolution")[1]/self.map.map_matrix.shape[1]
        # x_center_of_rect = rect_height/2
        # y_center_of_rect = rect_width/2
        # for x in range(self.map.map_matrix.shape[0]):
        #     for y in range(self.map.map_matrix.shape[1]):
        #         color = temporal_materials[self.map.map_matrix[x,y]]
        #         pygame.draw.rect(window,color,pygame.Rect((x_center_of_rect*x,y_center_of_rect*y),(rect_height,rect_width)))
        rect_height = self.settings.provide_settings("resolution")[1]/self.map.map_matrix.shape[0]
        rect_width = self.settings.provide_settings("resolution")[0]/self.map.map_matrix.shape[1]
       
       
        #drawing the map
        for x in range(self.map.map_matrix.shape[0]):
            for y in range(self.map.map_matrix.shape[1]):
                pygame.draw.rect(window,self.map.map_matrix[x,y].directory,pygame.Rect((rect_height*y,rect_width*x),(rect_height,rect_width)))
        
        
        #drawing the player 
        pygame.draw.rect(window,temporal_materials[-1],pygame.Rect((rect_height*self.player.pos_y,rect_width*self.player.pos_x),(rect_height,rect_width)))
        #pygame.draw.rect(window,(0,0,255),[100,100,400,100],2)
        #self.screen = window
        

    def recieve_input(self,keys):
        if self.move_ticker == 0:
            if keys[pygame.K_LEFT]:
                    self.move_ticker = 2
                    if self.player.pos_y !=0:
                        self.player.pos_y -=1

            if keys[pygame.K_RIGHT]:
                    self.move_ticker = 2  
                    if self.player.pos_y != self.map.map_matrix.shape[1]-1:
                        self.player.pos_y +=1
            
            #### This goes in a world method called player_movement or so, i am putting it here just to test the idea
            if self.map.valid_posc(self.player.pos_x+1,self.player.pos_y) and self.map.map_matrix[self.player.pos_x+1,self.player.pos_y].density < 1:
                self.move_ticker = 2
                self.player.pos_x +=1
        if self.move_ticker > 0:
            self.move_ticker-=1
