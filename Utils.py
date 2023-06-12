import numpy as np
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
