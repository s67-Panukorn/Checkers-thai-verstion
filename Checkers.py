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
    
    
    def createPawn(self, i, j, team, state="disable"): # method ใช้สร้างตัวหมากโดยไม่ต้องเขียนยาว
        self.canvas.create_oval(j*self.square_size+10,i*self.square_size+10,j*self.square_size+self.square_size-10,i*self.square_size+self.square_size-10,width=0,fill=team,tags=f"Pawn{i}{j}",state=state)
        self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>",lambda event, i=i,j=j,team=team:self.hilighte_chanel(i, j, team))

    
    def createTable(self): # method ใช้สร้างตารางและตัวหมาก
        for i in range(8):
            for j in range(8):
                # สร้างตาราง
                if (self.data[i][j] == "0"):
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#DAC6A3",tags=f"Chanel{i}{j}",state="disabled")
                else:
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#95561E",tags=f"Chanel{i}{j}",state="disabled")
                
                # สร้างตัวหมาก
                if (self.data[i][j] == "B"):
                    self.createPawn(i, j, "black")
                elif (self.data[i][j] == "W"):
                    self.createPawn(i, j, "white")
                
                # ทำให้สถานะ(state)ของตัวหมากสามารถกดได้ปกติ หากเป็นเทิร์นของฝ่ายนั้น
                if (self.trun == "black"):
                    if self.data[i][j] == "B":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")
                else:
                    if self.data[i][j] == "W":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")       


    def hilighte_chanel(self, i, j, team):
        self.reset_widget()
        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="green",width=3)
        if (team == "black"):
            if (self.data[i][j]=="B"): # ตัวหมากธรรมดา
                # กรณีเดินทั่วไป
                # เช็คทางขวา
                if (i < 7 and j < 7 and self.data[i+1][j+1] == "1") and not (i < 6 and j > 1 and (self.data[i+1][j-1] == "W" or self.data[i+1][j-1] == "HW") and self.data[i+2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#39E75F" ,state="normal") 
                    self.canvas.tag_bind(f"Chanel{i+1}{j+1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1, chanel_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team))
                # เช็คทางซ้าย
                if (i < 7 and j > 0 and self.data[i+1][j-1] == "1") and not (i < 6 and j < 6 and (self.data[i+1][j+1] == "W" or self.data[i+1][j+1] == "HW") and self.data[i+2][j+2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+1}{j-1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1, chanel_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team))
                # กรณีที่สามารถกินได้
                # เช็คทางขวา
                if (i < 6 and j < 6 and (self.data[i+1][j+1] == "W" or self.data[i+1][j+1] == "HW") and self.data[i+2][j+2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i+2}{j+2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+2}{j+2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2, chanel_j = j+2, delete_i = i+1, delete_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
                # เช็คทางซ้าย
                if (i < 6 and j > 1 and (self.data[i+1][j-1] == "W" or self.data[i+1][j-1] == "HW") and self.data[i+2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i+2}{j-2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+2}{j-2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2, chanel_j = j-2, delete_i = i+1, delete_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
            else:
                pass
        else:
            if (self.data[i][j]=="W"): # ตัวหมากธรรมดา
                # กรณีเดินทั่วไป
                # เช็คทางขวา
                if (i > 0 and j < 7 and self.data[i-1][j+1] == "1") and not (i > 1 and j > 1 and (self.data[i-1][j-1] == "B" or self.data[i-1][j-1] == "HB") and self.data[i-2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-1}{j+1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1, chanel_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team))
                # เช็คทางซ้าย
                if (i > 0 and j > 0 and self.data[i-1][j-1] == "1") and not (i > 1 and j < 6 and (self.data[i-1][j+1] == "B" or self.data[i-1][j+1] == "HB") and self.data[i-2][j+2] == "1" ):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-1}{j-1}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1, chanel_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team))
                # กรณีที่สามารกินได้
                # เช็คทางขวา
                if (i > 1 and j < 6 and (self.data[i-1][j+1] == "B" or self.data[i-1][j+1] == "HB") and self.data[i-2][j+2] == "1" ):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i-2}{j+2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-2}{j+2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2, chanel_j = j+2, delete_i = i-1, delete_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
                # เช็คทางซ้าย
                if (i > 1 and j > 1 and (self.data[i-1][j-1] == "B" or self.data[i-1][j-1] == "HB") and self.data[i-2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i-2}{j-2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-2}{j-2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2, chanel_j = j-2, delete_i = i-1, delete_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
            else:
                pass
            
            
    def move_pawn(self, pawn_i, pawn_j, chanel_i, chanel_j, team, delete_i=0,delete_j=0):
        if(delete_i == 0 and delete_j == 0): # กรณีเดินปกติ
            # สร้างวงกลมใหม่ในช่องที่กด
            self.createPawn(chanel_i, chanel_j, team)
            # ลบวงกลมอันเก่า
            self.canvas.delete(f"Pawn{pawn_i}{pawn_j}")
            # เปลี่ยนค่าใน array 
            self.data[pawn_i][pawn_j] = "1"
            self.data[chanel_i][chanel_j] = team[0].upper()
            # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
            self.reset_widget(self.trun)
            self.check_canAttack(self.trun)
        else: # กรณีที่กิน
            # สร้างวงกลมใหม่ในช่องที่กด
            self.createPawn(chanel_i, chanel_j, team, "normal")
            # ลบวงกลมอันเก่า
            self.canvas.delete(f"Pawn{pawn_i}{pawn_j}")
            self.canvas.delete(f"Pawn{delete_i}{delete_j}")
            # เปลี่ยนค่าใน array 
            self.data[pawn_i][pawn_j] = "1"
            self.data[delete_i][delete_j] = "1"
            self.data[chanel_i][chanel_j] = team[0].upper()
            # เช็คว่าสามารถกินต่อได้ไหม
            if(team == 'black'):
                if  ((chanel_i < 6 and chanel_j < 6 and (self.data[chanel_i+1][chanel_j+1] == "W" or self.data[chanel_i+1][chanel_j+1] == "HW") and self.data[chanel_i+2][chanel_j+2] == "1")
                    or 
                    (chanel_i < 6 and chanel_j > 1 and (self.data[chanel_i+1][chanel_j-1] == "W" or self.data[chanel_i+1][chanel_j-1] == "HW") and self.data[chanel_i+2][chanel_j-2] == "1")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'black')
                else:
                    # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
                    self.reset_widget(self.trun)
                    self.check_canAttack(self.trun)
            else:
                if  ((chanel_i > 1 and chanel_j < 6 and (self.data[chanel_i-1][chanel_j+1] == "B" or self.data[chanel_i-1][chanel_j+1] == "HB") and self.data[chanel_i-2][chanel_j+2] == "1" )
                    or 
                    (chanel_i > 1 and chanel_j > 1 and (self.data[chanel_i-1][chanel_j-1] == "B" or self.data[chanel_i-1][chanel_j-1] == "HB") and self.data[chanel_i-2][chanel_j-2] == "1")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'white')
                else:
                    # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
                    self.reset_widget(self.trun)
                    self.check_canAttack(self.trun)
    
    
    def check_canAttack(self, turn):
        canAttack = False # ตัวแปรที่บอกว่ามีตัวที่สามารถกินได้ไหม
        # ลูปนี้จะทำให้กดได้เฉพาะตัวที่สามารถกินได้และจะทำให้ตัวที่กินไม่ได้ทั้งหมดกดไม่ได้
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                if(turn == 'black'):
                    if (self.data[i][j] == "B"):
                        if ((i < 6 and j < 6 and (self.data[i+1][j+1] == "W" or self.data[i+1][j+1] == "HW") and self.data[i+2][j+2] == "1") or (i < 6 and j > 1 and (self.data[i+1][j-1] == "W" or self.data[i+1][j-1] == "HW") and self.data[i+2][j-2] == "1")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
                else:
                    if (self.data[i][j] == "W"):
                        if ((i > 1 and j < 6 and (self.data[i-1][j+1] == "B" or self.data[i-1][j+1] == "HB") and self.data[i-2][j+2] == "1" ) or (i > 1 and j > 1 and (self.data[i-1][j-1] == "B" or self.data[i-1][j-1] == "HB") and self.data[i-2][j-2] == "1")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
        # เงื่อนไขนี้มีเพื่อในกรณีที่ไม่มีตัวไหนสามารถกินได้เลยจะทำให้หมากของฝ่ายนั้นสามารถกดเดินได้
        if not canAttack :
            for i in range(8):
                for j in range(8):       
                    if(turn == 'black'):
                        if (self.data[i][j] == "B"):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",state="normal")
                    else:
                        if (self.data[i][j] == "W"):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",state="normal")
          
                             
    def reset_widget(self, turn = ""):
        # รีเช็ตให้ Widget ทุกตัวกลับสู่สภาพปกติ
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0)
                self.canvas.itemconfigure(f"Chanel{i}{j}",fill="#DAC6A3" if self.data[i][j] == "0" else "#95561E" ,state="disable") 
                self.canvas.tag_bind(f"Chanel{i}{j}","<Button-1>")
        # หากมีการส่งพารามิเตอร์ turn มาด้วยจะทำการสลับเทิร์นหากไม่มีจะทำงานแค่ลูปด้านบน
        if (turn == "black"):
            for row in range(8):
                for column in range(8):
                    if ("B" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif ("W" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.trun = "white"
        elif (turn == "white"):
            for row in range(8):
                for column in range(8):
                    if ("W" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif ("B" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.trun = "black"

                              
root = Tk()
game = GameCheckers(root)
root.mainloop()
