import random

class board:
    def __init__(self):
        self.data = [ [0 , 0 , 0 , 0] ,
                      [0 , 0 , 0 , 0] ,
                      [0 , 0 , 0 , 0] ,
                      [0 , 0 , 0 , 0] ]
        self.new_tile()
        self.new_tile()
        print("Initialize Board: \n" + self.__str__())

    def __repr__(self):
        return [item for item in self.data]
        
    def __str__(self):
        return 'my_board = ' + str([item for item in self.data])
    
    def new_tile(self):
        row = random.randint(0,3)
        column = random.randint(0,3)
        while self.data[row][column] !=0:
            row = random.randint(0,3)
            column = random.randint(0,3)
        value = self.return_value()
        self.data[row][column] = value

    def return_value(self):
        value = random.randint(1,5)
        if(value==1):
            return 4
        else:
            return 2

    def get_value(self,row,column):
        return self.data[row][column]


    def up(self):
        
