import tkinter
import math
import random
from data_structure import *

tilesize = 80
padding = 10
canvas_pad = 20
boardsize = 4*padding + 4*tilesize
canvassize = boardsize + canvas_pad


def init_gui():
    global gui  ## board = tkinter gui
    window = tkinter.Tk()
    gui = tkinter.Canvas(window,width=canvassize,height=canvassize,bg='#BBADA0')
    gui.pack()
    update_board()
    window.bind('<Up>',up)
    window.bind('<Down>',down)
    window.bind('<Left>',left)
    window.bind('<Right>',right)

def update_board():
    global data
    global board
    for i in range(4):
        for j in range(4):
            xtopleft = canvas_pad*0.5+(j+1)*padding + j*tilesize
            ytopleft = canvas_pad*0.5+(i+1)*padding + i*tilesize
            gui.create_polygon(getCoord(xtopleft,ytopleft),fill=getColor(data.get_value(i,j)))
            if(data.get_value(i,j)!=0):
                gui.create_text(xtopleft+tilesize/2,ytopleft+tilesize/2,text=data.get_value(i,j))

def getCoord(x,y):
    coord = x,y,x+tilesize,y,x+tilesize,y+tilesize,x,y+tilesize
    return coord

def getColor(value):
    color = ['#CDC1B4','#EEE4DA','#EDE0C8','#F3B179','#F59563','#ED785E','#F55D3C','#EDCE72','#EDCB61','#ECC750','#EDC440','#EDC12B','#FF3D3B','#FF1E1F','#FF1E20','#FF1E1F','#FF1E1F','#FF1E1E']
    if value == 0:
        return color[0]
    else:
        return color[int(math.log(value,2))]

def up(event):
    global data
    data.new_tile()
    update_board()
    print("Pressed UP")

def down(event):
    global data
    new_tile()
    update_board()
    print("Pressed DOWN")

def left(event):
    global table
    print("Pressed LEFT")

def right(event):
    global table
    print("Pressed RIGHT")

if __name__ == "__main__":
    global data
    data = board()
    init_gui()
    
