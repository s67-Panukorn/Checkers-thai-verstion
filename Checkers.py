from tkinter import *

class GameCheckers:
    def __init__(self, root) :
        self.root = root
        self.root.title("Checkers")
        self.square_size = 100
        self.canvas = Canvas(self.root,width=self.square_size*8,height=self.square_size*8)
        self.canvas.pack()
        
        # สร้างตารางและตัวหมาก
        for i in range(8):
            for j in range(8):
                if ((i+j)%2 == 0):
                    color = "#DAC6A3"
                else:
                    color = "#95561E"
                self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill=color)
                
                if(((i==0 or i==1) or (i==6 or i==7)) and (i+j)%2 != 0):
                    if(i < 3):
                        self.canvas.create_oval(j*self.square_size+5,i*self.square_size+5,j*self.square_size+self.square_size-5,i*self.square_size+self.square_size-5,fill="#000000")
                    else:
                        self.canvas.create_oval(j*self.square_size+5,i*self.square_size+5,j*self.square_size+self.square_size-5,i*self.square_size+self.square_size-5,fill="#ffffff")
                
root = Tk()
game = GameCheckers(root)
root.mainloop()