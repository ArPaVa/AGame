import numpy as np
class Map:
    def __init__(self,x,y):
        self.map_matrix = np.zeros(shape=(x,y),dtype=int)
        for i in range(self.map_matrix.shape[0]):
            if i>=  self.map_matrix.shape[1]/2:
                for j in range(self.map_matrix.shape[1]):
                    self.map_matrix[i,j]= 1
        print(self.map_matrix)

    

