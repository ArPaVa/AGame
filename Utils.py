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
        self.going_up_list = []
        self.digging = False
        self.digging_iter = 10
        self.digging_skill = 1
        self.directory = (150,70,70)
        
        #self.move_ticker = 0

    def move_around(self,keys,map:Map):
        if not self.digging:

            if keys[pygame.K_LEFT]:
                #self.move_ticker = 2
                move = self.actual_movement_coordinates(map,self.pos_x,self.pos_y-1)
                self.pos_x += move[0]
                self.pos_y += move[1]

            if keys[pygame.K_RIGHT]:
                #self.move_ticker = 2  
                move = self.actual_movement_coordinates(map,self.pos_x,self.pos_y+1)
                self.pos_x += move[0]
                self.pos_y += move[1]

        #This just puts in a list the jump to be made it doesnt actually modify the posicion of the player
            if keys[pygame.K_UP]:
                #self.move_ticker = 2
                if map.map_matrix[(self.pos_x + 1),self.pos_y].density == 1:
                    self.going_up_list.clear()
                    self.going_up_list.append(2)
                    self.going_up_list.append(2)
                    self.going_up_list.append(2)
                    self.going_up_list.append(2)
                    self.going_up_list.append(2)
    
    #This is where we actually handle the posicion of the player because is jumping    
        if len(self.going_up_list) > 0:
            jump = self.actual_movement_coordinates(map,(self.pos_x - self.going_up_list[0]),self.pos_y)
            self.pos_x += jump[0]
            self.pos_y += jump[1]
            self.going_up_list.pop(0)

        #Handling the natural fall of the player
        if map.valid_posc(self.pos_x+1,self.pos_y) and map.map_matrix[self.pos_x+1,self.pos_y].density < 1 and not len(self.going_up_list) > 0:
            #self.move_ticker = 2
            self.pos_x +=1
       
    def act_around(self,keys,map):
        important_events = []
        for events in keys:
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP or events.key == pygame.K_DOWN or events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                    if events not in important_events:
                        self.latest_mov_key = events
                        important_events.append(events)
                    
                if events.key == pygame.K_c:
                    if pygame.K_c in important_events:
                        important_events.remove(pygame.K_c)
                    else:
                        important_events.append(pygame.K_c)
        if pygame.K_c in important_events:
            important_events.remove(pygame.K_c)
            if self.digging:
                self.dig_skill()
                self.directory = (150,70,70)
            else:
                if self.latest_mov_key.key==pygame.K_UP:
                    self.dig_skill(map.map_matrix[self.pos_x-1,self.pos_y])
                    self.block_to_break = (self.pos_x-1,self.pos_y)
                    self.directory =(70,70,150)
                if self.latest_mov_key.key==pygame.K_DOWN:
                    self.dig_skill(map.map_matrix[self.pos_x+1,self.pos_y])
                    self.block_to_break = (self.pos_x+1,self.pos_y)
                    self.directory =(70,70,150)
                if self.latest_mov_key.key==pygame.K_LEFT:
                    self.dig_skill(map.map_matrix[self.pos_x,self.pos_y-1])
                    self.block_to_break = (self.pos_x,self.pos_y-1)
                    self.directory =(70,70,150)
                if self.latest_mov_key.key==pygame.K_RIGHT:
                    self.dig_skill(map.map_matrix[self.pos_x,self.pos_y+1])
                    self.block_to_break = (self.pos_x,self.pos_y+1)
                    self.directory =(70,70,150)
                # for events in important_events:      
                #     if events.key==pygame.K_UP:
                #         self.dig_skill(map.map_matrix[self.pos_x-1,self.pos_y])
                #         self.block_to_break = (self.pos_x-1,self.pos_y)
                #         self.directory =(70,70,150)
                #     if events.key==pygame.K_DOWN:
                #         self.dig_skill(map.map_matrix[self.pos_x+1,self.pos_y])
                #         self.block_to_break = (self.pos_x+1,self.pos_y)
                #         self.directory =(70,70,150)
                #     if events.key==pygame.K_LEFT:
                #         self.dig_skill(map.map_matrix[self.pos_x,self.pos_y-1])
                #         self.block_to_break = (self.pos_x,self.pos_y-1)
                #         self.directory =(70,70,150)
                #     if events.key==pygame.K_RIGHT:
                #         self.dig_skill(map.map_matrix[self.pos_x,self.pos_y+1])
                #         self.block_to_break = (self.pos_x,self.pos_y+1)
                        # self.directory =(70,70,150)

        if self.digging and ( self.digging_x_pos != self.pos_x or self.digging_y_pos != self.pos_y):
                self.digging = False
                self.directory =(150,70,70)
        
        if self.digging and self.digging_iter > 0:
            self.digging_iter-=1
        
        if self.digging_iter == 0 and self.digging :
            self.digging = False
            self.directory =(150,70,70)
            return ("break_block",self.block_to_break)
            

    def actual_movement_coordinates(self,map,intended_x,intended_y):
        #TODO Propably is gonna have to change so it can return the posible position on laterall movements too, so in future Dashs or tps, it isnt necessary to make another method
        x = 0
        y = 0
        x_movement_todo = self.pos_x-intended_x
        y_movement_todo = self.pos_y-intended_y

        if x_movement_todo != 0:
            for i in range(min(abs(x_movement_todo),self.pos_x)):
                if x_movement_todo > 0:
                    if  map.map_matrix[(self.pos_x - (i+1)),self.pos_y].density < 1:
                        x-=1
                    else:
                        break
                if x_movement_todo < 0:
                    if  map.map_matrix[(self.pos_x + (i+1)),self.pos_y].density < 1:
                        x+=1
                    else:
                        break
        
        if y_movement_todo != 0:
            for i in range(min(abs(y_movement_todo),self.pos_y)):
                if y_movement_todo > 0:
                    if  map.map_matrix[self.pos_x ,self.pos_y- (i+1)].density < 1:
                        y-=1
                    else:
                        break
                if y_movement_todo < 0:
                    if  map.map_matrix[self.pos_x ,self.pos_y+ (i+1)].density < 1:
                        y+=1
                    else:
                        break
        return x,y

    def dig_skill(self,block=None):
        if not self.digging and block != None:
            if block.density > 0:
                self.digging = True
                self.digging_iter = abs(10*block.density*self.digging_skill)
                self.digging_x_pos = self.pos_x
                self.digging_y_pos = self.pos_y
        else:
            self.digging = False

    def act_pos (self, map:Map):
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
        self.orders = {"break_block":self.break_block}
        #self.screen = pygame.display.set_mode(self.settings.provide_settings("resolution"))
        self.move_ticker = 0
    def paint(self,window):
      
        rect_height = self.settings.provide_settings("resolution")[1]/self.map.map_matrix.shape[0]
        rect_width = self.settings.provide_settings("resolution")[0]/self.map.map_matrix.shape[1]
       
       
        #drawing the map
        for x in range(self.map.map_matrix.shape[0]):
            for y in range(self.map.map_matrix.shape[1]):
                pygame.draw.rect(window,self.map.map_matrix[x,y].directory,pygame.Rect((rect_height*y,rect_width*x),(rect_height,rect_width)))
        
        
        #drawing the player 
        pygame.draw.rect(window,self.player.directory,pygame.Rect((rect_height*self.player.pos_y,rect_width*self.player.pos_x),(rect_height,rect_width)))
        #pygame.draw.rect(window,(0,0,255),[100,100,400,100],2)
        #self.screen = window

    def break_block(self,block_pos):
        self.map.map_matrix[block_pos[0],block_pos[1]] = Air()

    def on_click_dirt(self,mouse_pos_tuple):
        rect_height = self.settings.provide_settings("resolution")[1]/self.map.map_matrix.shape[0]
        rect_width = self.settings.provide_settings("resolution")[0]/self.map.map_matrix.shape[1]
        matrix_x = mouse_pos_tuple[1]//rect_width
        matrix_y = mouse_pos_tuple[0]//rect_height
        if matrix_x == int(matrix_x):
            def_x = int(matrix_x)
        else:
            def_x = int(matrix_x)+1
        if matrix_y == int(matrix_y):
            def_y = int(matrix_y)
        else:
            def_y = int(matrix_y)+1

        self.map.map_matrix[def_x,def_y] = Dirt()  

    def recieve_input_pressed(self,keys):
        player_todo = self.player.move_around(keys,self.map)
        
    def recieve_input_keydown(self,keys):
        player_todo = self.player.act_around(keys,self.map)
        if player_todo != None:
            self.orders[player_todo[0]](player_todo[1])

