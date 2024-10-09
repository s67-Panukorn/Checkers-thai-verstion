from tkinter import *

class GameCheckers:
    def __init__(self, root) :
        self.root = root
        self.root.title("Checkers (Thai version)")
        self.square_size = 100
        self.canvas = Canvas(self.root,width=self.square_size*8,height=self.square_size*8)
        self.canvas.pack()
        self.data = [["0","B","0","B","0","B","0","B"],
                     ["B","0","B","0","B","0","B","0"],
                     ["0","1","0","1","0","1","0","1"],
                     ["1","0","1","0","1","0","1","0"],
                     ["0","1","0","1","0","1","0","1"],
                     ["1","0","1","0","1","0","1","0"],
                     ["0","W","0","W","0","W","0","W"],
                     ["W","0","W","0","W","0","W","0"]]
        self.trun = "white"
        self.createTable()
        
    def createTable(self): #สร้างตารางและตัวหมาก
        for i in range(8):
            for j in range(8):
                if (self.data[i][j] == "0"):
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#DAC6A3",tags=f"Chanel{i}{j}",state="disabled")
                else:
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#95561E",tags=f"Chanel{i}{j}",state="disabled")
                
                if (self.data[i][j] == "B"):
                    self.canvas.create_oval(j*self.square_size+10,i*self.square_size+10,j*self.square_size+self.square_size-10,i*self.square_size+self.square_size-10,width=0,fill="black",tags=f"Pawn{i}{j}",state="disabled")
                    self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>",lambda event, i=i,j=j,team='black':self.hilighte_chanel(i, j, team))
                elif (self.data[i][j] == "W"):
                    self.canvas.create_oval(j*self.square_size+10,i*self.square_size+10,j*self.square_size+self.square_size-10,i*self.square_size+self.square_size-10,width=0,fill="white",tags=f"Pawn{i}{j}",state="disabled")
                    self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>",lambda event, i=i,j=j,team='white':self.hilighte_chanel(i, j, team))
                    
                if (self.trun == "white"):
                    if self.data[i][j] == "W":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")
                else:
                    if self.data[i][j] == "B":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")       

    def hilighte_chanel(self, i, j, team):
        self.reset_widget()
        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="green",width=3)
        if (team == "black"):
            # กรณีเดินปกติ เช็คขวา-ซ้าย
            if (i < 7 and j < 7 and self.data[i+1][j+1] == "1"):
                self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#39E75F" ,state="normal") 
                self.canvas.tag_bind(f"Chanel{i+1}{j+1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1, chanel_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team))
            if (i < 7 and j > 0 and self.data[i+1][j-1] == "1"):
                self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#39E75F" ,state="normal")
                self.canvas.tag_bind(f"Chanel{i+1}{j-1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1, chanel_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team))
            # กรณีที่สามารถกินได้ เช็คขวา-ซ้าย
            if (i < 7 and j < 6 and (self.data[i+1][j+1] == "W" or self.data[i+1][j+1] == "HW") and self.data[i+2][j+2] == "1"):
                self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#EB4343")
                self.canvas.itemconfigure(f"Chanel{i+2}{j+2}",fill="#39E75F" ,state="normal")
            if (i < 7 and j > 1 and (self.data[i+1][j-1] == "W" or self.data[i+1][j-1] == "HW") and self.data[i+2][j-2] == "1"):
                self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#EB4343")
                self.canvas.itemconfigure(f"Chanel{i+2}{j-2}",fill="#39E75F" ,state="normal")
        else:
            # กรณีเดินปกติ เช็คขวา-ซ้าย
            if (i > 1 and j < 7 and self.data[i-1][j+1] == "1"):
                self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#39E75F" ,state="normal")
                self.canvas.tag_bind(f"Chanel{i-1}{j+1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1, chanel_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team))
            if (i > 1 and j > 0 and self.data[i-1][j-1] == "1"):
                self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#39E75F" ,state="normal")
                self.canvas.tag_bind(f"Chanel{i-1}{j-1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1, chanel_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team))
            # กรณีที่สามารกินได้ เช็คขวา-ซ้าย
            if (i > 1 and j < 6 and (self.data[i-1][j+1] == "B" or self.data[i-1][j+1] == "HB") and self.data[i-2][j+2] == "1" ):
                self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#EB4343")
                self.canvas.itemconfigure(f"Chanel{i-2}{j+2}",fill="#39E75F" ,state="normal")
            if (i > 1 and j > 1 and (self.data[i-1][j-1] == "B" or self.data[i-1][j-1] == "HB") and self.data[i-2][j-2] == "1"):
                self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#EB4343")
                self.canvas.itemconfigure(f"Chanel{i-2}{j-2}",fill="#39E75F" ,state="normal")
                        
    def move_pawn(self, pawn_i, pawn_j, chanel_i, chanel_j, team):
        # สร้างวงกลมใหม่ในช่องที่กด
        self.canvas.create_oval(chanel_j*self.square_size+10,chanel_i*self.square_size+10,chanel_j*self.square_size+self.square_size-10,chanel_i*self.square_size+self.square_size-10,width=0,fill=team,tags=f"Pawn{chanel_i}{chanel_j}")
        self.canvas.tag_bind(f"Pawn{chanel_i}{chanel_j}","<Button-1>",lambda event, i=chanel_i,j=chanel_j,team=team:self.hilighte_chanel(i, j, team))
        # สลับค่าใน array 
        temp = self.data[pawn_i][pawn_j]
        self.data[pawn_i][pawn_j] = self.data[chanel_i][chanel_j]
        self.data[chanel_i][chanel_j] = temp
        # ลบวงกลมอันเก่าแล้วสลับเทิร์น
        self.canvas.delete(f"Pawn{pawn_i}{pawn_j}")
        self.reset_widget(self.trun)
                          
    def reset_widget(self, turn = ""):
        # รีเช็ตให้ทุก Widget ทุกตัวกลับสู่สภาพปกติ
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0)
                self.canvas.itemconfigure(f"Chanel{i}{j}",fill="#DAC6A3" if self.data[i][j] == "0" else "#95561E" ,state="disable") 
                self.canvas.tag_bind(f"Chanel{i}{j}","<Button-1>")
        # หากมีการส่งพารามิเตอร์ turn มาด้วยจะทำการสลับเทิร์นหากไม่มีจะทำงานแค่ลูปด้านบน
        if (turn == "black"):
            for row in range(8):
                for column in range(8):
                    if (self.data[row][column] == "B"):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif (self.data[row][column] == "W"):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.trun = "white"
        elif (turn == "white"):
            for row in range(8):
                for column in range(8):
                    if (self.data[row][column] == "W"):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif (self.data[row][column] == "B"):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.trun = "black"
        
                 
root = Tk()
game = GameCheckers(root)
root.mainloop()
