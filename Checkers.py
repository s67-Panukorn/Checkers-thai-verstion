from tkinter import *

class GameCheckers:
    def __init__(self, root) :
        self.root = root
        self.root.title("Checkers (Thai version)")
        self.square_size = 100 # Recommend ไม่ควรเป็นประภท float 
        self.canvas = Canvas(self.root,width=self.square_size*8,height=self.square_size*8,background="#E4DDD4")
        self.info = Canvas(self.root, width=self.square_size*4, height=self.square_size*8,background="#E4DDD4")
        self.info.grid(row=0, column=1)
        self.canvas.grid(row=0, column=0)
        self.data = [["0","B","0","B","0","B","0","B"],
                     ["B","0","B","0","B","0","B","0"],
                     ["0","1","0","1","0","1","0","1"],
                     ["1","0","1","0","1","0","1","0"],
                     ["0","1","0","1","0","1","0","1"],
                     ["1","0","1","0","1","0","1","0"],
                     ["0","W","0","W","0","W","0","W"],
                     ["W","0","W","0","W","0","W","0"]]
        self.turn = "white"
        self.createTable()
        self.information()
    
    def endGame(self):
        winner = "black" if self.turn == "white" else "white"
        self.info.delete(self.txtTurn)
        self.info.delete(self.recTurn)
        self.canvas.create_rectangle(0, 0, self.square_size*8, self.square_size*8, fill=winner, outline='')
        self.canvas.create_text(self.square_size*4,self.square_size*3,text="The Winner is ...", font=('Times', int(self.square_size*40/100), 'italic'), fill=self.turn)
        self.canvas.create_text(self.square_size*4,self.square_size*4,text=winner.capitalize()+" team !!!", font=('Times', int(self.square_size*75/100), 'bold italic'), fill=self.turn)
        
    def information(self):
        self.info.create_text(self.square_size*2,int(self.square_size*45/100),text="Welcome to", font=('Times', int(self.square_size*20/100), 'italic'), fill='#0a0a0a')
        self.info.create_text(self.square_size*2,int(self.square_size*90/100),text="Checkers", font=('Times', int(self.square_size*55/100), 'bold'), fill='#000')
        self.txtTurn = self.info.create_text(self.square_size*2, self.square_size*2,text="Turn  :  "+self.turn.capitalize(), font=('Helvetica', int(self.square_size*15/100), 'bold'), fill='#0a0a0a')
        self.recTurn = self.info.create_rectangle(int(self.square_size*2-self.square_size*80/100), int(self.square_size*2.2), int(self.square_size*2+self.square_size*80/100), int(self.square_size*2.2)+int(self.square_size*35/100), fill=self.turn, outline="silver")
        
    def createKing(self, i, j, team, state="disable"): # method ใช้สร้างตัวฮอส(King)โดยไม่ต้องเขียนยาว
        self.canvas.create_oval(j*self.square_size+(self.square_size*10/100),i*self.square_size+(self.square_size*10/100),j*self.square_size+self.square_size-(self.square_size*10/100),i*self.square_size+self.square_size-(self.square_size*10/100),width=0,fill=team,tags=f"Pawn{i}{j}",state=state)
        self.canvas.create_oval(j*self.square_size+(self.square_size*40/100),i*self.square_size+(self.square_size*40/100),j*self.square_size+self.square_size-(self.square_size*40/100),i*self.square_size+self.square_size-(self.square_size*40/100),outline="",fill= "silver",tags=f"Pawn{i}{j}",state=state)
        self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>",lambda event, i=i,j=j,team=team:self.hilighte_chanel(i, j, team))
        
    def createPawn(self, i, j, team, state="disable"): # method ใช้สร้างตัวหมากโดยไม่ต้องเขียนยาว
        self.canvas.create_oval(j*self.square_size+(self.square_size*10/100),i*self.square_size+(self.square_size*10/100),j*self.square_size+self.square_size-(self.square_size*10/100),i*self.square_size+self.square_size-(self.square_size*10/100),width=0,fill=team,tags=f"Pawn{i}{j}",state=state)
        self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>",lambda event, i=i,j=j,team=team:self.hilighte_chanel(i, j, team))

    def createTable(self): # method ใช้สร้างตารางและตัวหมาก
        for i in range(8):
            for j in range(8):
                # สร้างตาราง
                if (self.data[i][j] == "0"):
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#DAC6A3",tags=f"Chanel{i}{j}",state="disabled",outline='')
                else:
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size,j*self.square_size+self.square_size,i*self.square_size+self.square_size,fill="#95561E",tags=f"Chanel{i}{j}",state="disabled",outline='')
                
                # สร้างตัวหมาก
                if (self.data[i][j] == "B"):
                    self.createPawn(i, j, "black")
                elif (self.data[i][j] == "W"):
                    self.createPawn(i, j, "white")
                elif (self.data[i][j] == "HB"):
                    self.createKing(i, j, 'black')
                elif (self.data[i][j] == "HW"):
                    self.createKing(i, j, 'white')
                    
                # ทำให้สถานะ(state)ของตัวหมากสามารถกดได้ปกติ หากเป็นเทิร์นของฝ่ายนั้น
                if (self.turn == "black"):
                    if "B" in self.data[i][j]:
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")
                else:
                    if "W" in self.data[i][j]:
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
                if (i < 6 and j < 6 and "W" in self.data[i+1][j+1] and self.data[i+2][j+2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i+2}{j+2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+2}{j+2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2, chanel_j = j+2, delete_i = i+1, delete_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
                # เช็คทางซ้าย
                if (i < 6 and j > 1 and "W" in self.data[i+1][j-1] and self.data[i+2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i+2}{j-2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+2}{j-2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2, chanel_j = j-2, delete_i = i+1, delete_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
            else:
                self.hilighte_King(i, j, "black")
                    
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
                if (i > 1 and j < 6 and "B" in self.data[i-1][j+1] and self.data[i-2][j+2] == "1" ):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i-2}{j+2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-2}{j+2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2, chanel_j = j+2, delete_i = i-1, delete_j = j+1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
                # เช็คทางซ้าย
                if (i > 1 and j > 1 and "B" in self.data[i-1][j-1] and self.data[i-2][j-2] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#EB4343")
                    self.canvas.itemconfigure(f"Chanel{i-2}{j-2}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-2}{j-2}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2, chanel_j = j-2, delete_i = i-1, delete_j = j-1:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j))
            else:
                self.hilighte_King(i, j, "white")
            
            
    def move_pawn(self, pawn_i, pawn_j, chanel_i, chanel_j, team, delete_i=0,delete_j=0,king=False):
        # pawn_ i,j คือตำแหน่งของตัวหมากที่กดเดิน
        # chanel_ i,j คือตำแหน่งของช่องที่ตัวหมากนั้นเดินไป
        # delete_ i,j คือตำแหน่งของตัวหมากที่โดนกิน
        if(delete_i == 0 and delete_j == 0): # กรณีเดินปกติ
            # สร้างวงกลมใหม่ในช่องที่กด ถ้าในกรณีที่ฮอสเดินจะส่งพารามิเตอร์ king เข้ามาเป็น True
            if ( team == "black" ):
                if (chanel_i == 7 or king):
                    self.createKing(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "HB"
                else:
                    self.createPawn(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "B"
            else:
                if (chanel_i == 0 or king):
                    self.createKing(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "HW"
                else:
                    self.createPawn(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "W"
            # ลบวงกลมอันเก่า
            self.canvas.delete(f"Pawn{pawn_i}{pawn_j}")
            # เปลี่ยนค่าใน array 
            self.data[pawn_i][pawn_j] = "1"
            # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
            self.reset_widget(self.turn)
            self.check_canAttack(self.turn)
            self.is_Loss()
        else: # กรณีที่กิน
            # สร้างวงกลมใหม่ในช่องที่กด  ถ้าในกรณีที่ฮอสเดินจะส่งพารามิเตอร์ king เข้ามาเป็น True
            if ( team == "black" ):
                if (chanel_i == 7 or king):
                    self.createKing(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "HB"
                else:
                    self.createPawn(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "B"
            else:
                if (chanel_i == 0 or king):
                    self.createKing(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "HW"
                else:
                    self.createPawn(chanel_i, chanel_j, team)
                    self.data[chanel_i][chanel_j] = "W"
            # ลบวงกลมอันเก่า
            self.canvas.delete(f"Pawn{pawn_i}{pawn_j}")
            self.canvas.delete(f"Pawn{delete_i}{delete_j}")
            # เปลี่ยนค่าใน array 
            self.data[pawn_i][pawn_j] = "1"
            self.data[delete_i][delete_j] = "1"
            # เช็คว่าสามารถกินต่อได้ไหม
            if(team == 'black'):
                # เช็คของฮอส บน-ล่าง ซ้าย-ขวา
                if king and (self.check_canAttackKing(chanel_i, chanel_j, 'B', 'R', "black") or self.check_canAttackKing(chanel_i, chanel_j, 'B', 'L', "black") or self.check_canAttackKing(chanel_i, chanel_j, 'T', 'R', "black") or self.check_canAttackKing(chanel_i, chanel_j, 'T', 'L', "black")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'black')
                # เช็คของหมากธรรมดา
                elif  (not king and (chanel_i < 6 and chanel_j < 6 and (self.data[chanel_i+1][chanel_j+1] == "W" or self.data[chanel_i+1][chanel_j+1] == "HW") and self.data[chanel_i+2][chanel_j+2] == "1")
                    or 
                    (chanel_i < 6 and chanel_j > 1 and (self.data[chanel_i+1][chanel_j-1] == "W" or self.data[chanel_i+1][chanel_j-1] == "HW") and self.data[chanel_i+2][chanel_j-2] == "1")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'black')
                else:
                    # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
                    self.reset_widget(self.turn)
                    self.check_canAttack(self.turn)
                    self.is_Loss()
            else:
                # เช็คของฮอส บน-ล่าง ซ้าย-ขวา
                if king and (self.check_canAttackKing(chanel_i, chanel_j, 'B', 'R', "white") or self.check_canAttackKing(chanel_i, chanel_j, 'B', 'L', "white") or self.check_canAttackKing(chanel_i, chanel_j, 'T', 'R', "white") or self.check_canAttackKing(chanel_i, chanel_j, 'T', 'L', "white")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'white')
                # เช็คของหมากธรรมดา  
                elif (not king and (chanel_i > 1 and chanel_j < 6 and (self.data[chanel_i-1][chanel_j+1] == "B" or self.data[chanel_i-1][chanel_j+1] == "HB") and self.data[chanel_i-2][chanel_j+2] == "1" )
                    or 
                    (chanel_i > 1 and chanel_j > 1 and (self.data[chanel_i-1][chanel_j-1] == "B" or self.data[chanel_i-1][chanel_j-1] == "HB") and self.data[chanel_i-2][chanel_j-2] == "1")):
                    for i in range(8):
                        for j in range(8):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                    self.canvas.itemconfigure(f"Pawn{chanel_i}{chanel_j}",outline="green",width=3,state="normal")
                    self.hilighte_chanel(chanel_i, chanel_j, 'white')
                else:
                    # สลับเทิร์นและเช็คว่าอีกฝั่งสามารถกินได้ไหม
                    self.reset_widget(self.turn)
                    self.check_canAttack(self.turn)
                    self.is_Loss()
    
    
    def hilighte_King(self, i, j, team):
        check_team = 'W' if team == 'black' else 'B'   
        # เดินปกติ
        if not self.check_canAttackKing(i, j, 'B', 'R', team) and not self.check_canAttackKing(i, j, 'B', 'L', team) and not self.check_canAttackKing(i, j, 'T', 'R', team) and not self.check_canAttackKing(i, j, 'T', 'L', team):
            # ล่างขวา
            for index in range(8):
                if (i+index < 7 and j+index < 7 and self.data[i+1+index][j+1+index] != "1"):
                    break
                elif (i+index < 7 and j+index < 7 and self.data[i+1+index][j+1+index] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1+index}{j+1+index}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+1+index}{j+1+index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1+index, chanel_j = j+1+index:self.move_pawn(i, j, chanel_i, chanel_j, team, king=True))
            # ล่างซ้าย
            for index in range(8):
                if (i+index < 7 and j-index > 0 and self.data[i+1+index][j-1-index] != "1"):
                    break
                elif (i+index < 7 and j-index > 0 and self.data[i+1+index][j-1-index] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1+index}{j-1-index}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i+1+index}{j-1-index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+1+index, chanel_j = j-1-index:self.move_pawn(i, j, chanel_i, chanel_j, team, king=True))
            # บนขวา
            for index in range(8):
                if (i-index > 0 and j+index < 7 and self.data[i-1-index][j+1+index] != "1"):
                    break
                elif (i-index > 0 and j+index < 7 and self.data[i-1-index][j+1+index] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1-index}{j+1+index}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-1-index}{j+1+index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1-index, chanel_j = j+1+index:self.move_pawn(i, j, chanel_i, chanel_j, team, king=True))
            # บนซ้าย
            for index in range(8):
                if (i-index > 0 and j-index > 0 and self.data[i-1-index][j-1-index] != "1"):
                    break
                elif (i-index > 0 and j-index > 0 and self.data[i-1-index][j-1-index] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1-index}{j-1-index}",fill="#39E75F" ,state="normal")
                    self.canvas.tag_bind(f"Chanel{i-1-index}{j-1-index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-1-index, chanel_j = j-1-index:self.move_pawn(i, j, chanel_i, chanel_j, team, king=True))
        # กินได้
        else:    
            # เช็คล่างขวากินได้ไหม
            if self.check_canAttackKing(i, j, 'B', 'R', team):
                for index in range(8):
                    if (i+index < 6 and j+index < 6 and check_team in self.data[i+1+index][j+1+index] and self.data[i+2+index][j+2+index] == "1"):
                        self.canvas.itemconfigure(f"Chanel{i+1+index}{j+1+index}",fill="#EB4343")
                        self.canvas.itemconfigure(f"Chanel{i+2+index}{j+2+index}",fill="#39E75F" ,state="normal")
                        self.canvas.tag_bind(f"Chanel{i+2+index}{j+2+index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2+index, chanel_j = j+2+index, delete_i = i+1+index, delete_j = j+1+index:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j, king=True))
                        break
            # เช็คล่างซ้ายกินได้ไหม
            if self.check_canAttackKing(i, j, 'B', 'L', team):
                for index in range(8):
                    if (i+index < 6 and j-index > 1 and check_team in self.data[i+1+index][j-1-index] and self.data[i+2+index][j-2-index] == "1"):
                        self.canvas.itemconfigure(f"Chanel{i+1+index}{j-1-index}",fill="#EB4343")
                        self.canvas.itemconfigure(f"Chanel{i+2+index}{j-2-index}",fill="#39E75F" ,state="normal")
                        self.canvas.tag_bind(f"Chanel{i+2+index}{j-2-index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i+2+index, chanel_j = j-2-index, delete_i = i+1+index, delete_j = j-1-index:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j, king=True))
                        break
            # เช็คบนขวากินได้ไหม
            if self.check_canAttackKing(i, j, 'T', 'R', team):
                for index in range(8):
                    if (i+index > 1 and j+index < 6 and check_team in self.data[i-1-index][j+1+index] and self.data[i-2-index][j+2+index] == "1"):
                        self.canvas.itemconfigure(f"Chanel{i-1-index}{j+1+index}",fill="#EB4343")
                        self.canvas.itemconfigure(f"Chanel{i-2-index}{j+2+index}",fill="#39E75F" ,state="normal")
                        self.canvas.tag_bind(f"Chanel{i-2-index}{j+2+index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2-index, chanel_j = j+2+index, delete_i = i-1-index, delete_j = j+1+index:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j, king=True))
                        break
            # เช็คบนซ้ายกินได้ไหม
            if self.check_canAttackKing(i, j, 'T', 'L', team):
                for index in range(8):
                    if (i-index > 1 and j-index > 1 and check_team in self.data[i-1-index][j-1-index] and self.data[i-2-index][j-2-index] == "1"):
                        self.canvas.itemconfigure(f"Chanel{i-1-index}{j-1-index}",fill="#EB4343")
                        self.canvas.itemconfigure(f"Chanel{i-2-index}{j-2-index}",fill="#39E75F" ,state="normal")
                        self.canvas.tag_bind(f"Chanel{i-2-index}{j-2-index}","<Button-1>",lambda event, i=i, j=j, chanel_i = i-2-index, chanel_j = j-2-index, delete_i = i-1-index, delete_j = j-1-index:self.move_pawn(i, j, chanel_i, chanel_j, team, delete_i, delete_j, king=True))
                        break     
           
    # ฟังก์ชันเช็คว่าฮอสนั้นสามารถกินได้ไหม
    def check_canAttackKing(self, i, j, check_i, check_j, team):
        check_team = 'W' if team == 'black' else 'B'
        # เช็คล่างขวา Bottom & Right
        if (check_i == 'B' and check_j == 'R'):
            for n in range(8):
                if (i+1+n < 8 and j+1+n < 8 and self.data[i+1+n][j+1+n] == '1'):
                    continue
                elif (i+1+n < 8 and j+1+n < 8 and team[0].upper() in self.data[i+1+n][j+1+n]):
                    return False
                elif (i+1+n < 8 and j+1+n < 8 and check_team in self.data[i+1+n][j+1+n]):
                    if (i+2+n < 8 and j+2+n < 8 and self.data[i+2+n][j+2+n] == "1"):
                        return True
                    else:
                        return False
        # เช็คล่างซ้าย Bottom & Left
        elif (check_i == 'B' and check_j == 'L'):
            for n in range(8):
                if (i+1+n < 8 and j-1-n >= 0 and self.data[i+1+n][j-1-n] == '1'):
                    continue
                elif (i+1+n < 8 and j-1-n >= 0 and team[0].upper() in self.data[i+1+n][j-1-n]):
                    return False
                elif (i+1+n < 8 and j-1-n >= 0 and check_team in self.data[i+1+n][j-1-n]):
                    if (i+2+n < 8 and j-2-n >= 0 and self.data[i+2+n][j-2-n] == "1"):
                        return True
                    else:
                        return False
        # เช็คล่างขวา Top & Right
        elif (check_i == 'T' and check_j == 'R'):
            for n in range(8):
                if (i-1-n >= 0 and j+1+n < 8 and self.data[i-1-n][j+1+n] == '1'):
                    continue
                elif (i-1-n >= 0 and j+1+n < 8 and team[0].upper() in self.data[i-1-n][j+1+n]):
                    return False
                elif (i-1-n >= 0 and j+1+n < 8 and check_team in self.data[i-1-n][j+1+n]):
                    if (i-2-n >= 0 and j+2+n < 8 and self.data[i-2-n][j+2+n] == "1"):
                        return True
                    else:
                        return False
        # เช็คล่างขวา Top & Left
        elif (check_i == 'T' and check_j == 'L'):
            for n in range(8):
                if (i-1-n >= 0 and j-1-n >= 0 and self.data[i-1-n][j-1-n] == '1'):
                    continue
                elif (i-1-n >= 0 and j-1-n >= 0 and team[0].upper() in self.data[i-1-n][j-1-n]):
                    return False
                elif (i-1-n >= 0 and j-1-n >= 0 and check_team in self.data[i-1-n][j-1-n]):
                    if (i-2-n >= 0 and j-2-n >= 0 and self.data[i-2-n][j-2-n] == "1"):
                        return True
                    else:
                        return False
        return False
    
    def check_canAttack(self, turn):
        canAttack = False # ตัวแปรที่บอกว่ามีตัวที่สามารถกินได้ไหม
        # ลูปนี้จะทำให้กดได้เฉพาะตัวที่สามารถกินได้และจะทำให้ตัวที่กินไม่ได้ทั้งหมดกดไม่ได้
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="disable")
                if(turn == 'black'):
                    if (self.data[i][j] == "B"):
                        if ((i < 6 and j < 6 and "W" in self.data[i+1][j+1] and self.data[i+2][j+2] == "1") or (i < 6 and j > 1 and "W" in self.data[i+1][j-1] and self.data[i+2][j-2] == "1")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
                    if (self.data[i][j] == "HB"):
                        if (self.check_canAttackKing(i, j, 'B', 'R', "black") or self.check_canAttackKing(i, j, 'B', 'L', "black") or self.check_canAttackKing(i, j, 'T', 'R', "black") or self.check_canAttackKing(i, j, 'T', 'L', "black")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
                    
                else:
                    if (self.data[i][j] == "W"):
                        if ((i > 1 and j < 6 and "B" in self.data[i-1][j+1] and self.data[i-2][j+2] == "1" ) or (i > 1 and j > 1 and "B" in self.data[i-1][j-1] and self.data[i-2][j-2] == "1")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
                    if (self.data[i][j] == "HW"):
                        if (self.check_canAttackKing(i, j, 'B', 'R', "white") or self.check_canAttackKing(i, j, 'B', 'L', "white") or self.check_canAttackKing(i, j, 'T', 'R', "white") or self.check_canAttackKing(i, j, 'T', 'L', "white")):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",outline="red",width=3,state="normal")
                            canAttack = True
        
        # เงื่อนไขนี้มีเพื่อในกรณีที่ไม่มีตัวไหนสามารถกินได้เลยจะทำให้หมากของฝ่ายนั้นสามารถกดเดินได้
        if not canAttack :
            for i in range(8):
                for j in range(8):       
                    if(turn == 'black'):
                        if ("B" in self.data[i][j]):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",state="normal")
                    else:
                        if ("W" in self.data[i][j]):
                            self.canvas.itemconfigure(f"Pawn{i}{j}",state="normal")
          
                             
    def reset_widget(self, turn = ""):
        # รีเช็ตให้ Widget ทุกตัวกลับสู่สภาพปกติ
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0)
                self.canvas.itemconfigure(f"Chanel{i}{j}",fill="#DAC6A3" if self.data[i][j] == "0" else "#95561E" ,state="disable") 
                self.canvas.tag_bind(f"Chanel{i}{j}","<Button-1>")
 
        if (turn == "black"):
            for row in range(8):
                for column in range(8):
                    if ("B" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif ("W" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.turn = "white"
            self.info.itemconfigure(self.txtTurn, text="Turn  :  "+self.turn.capitalize(), fill='#0a0a0a')
            self.info.itemconfigure(self.recTurn, fill=self.turn)
            
        elif (turn == "white"):
            for row in range(8):
                for column in range(8):
                    if ("W" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="disable")
                    elif ("B" in self.data[row][column]):
                        self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0,state="normal")
            self.turn = "black"
            self.info.itemconfigure(self.txtTurn, text="Turn  :  "+self.turn.capitalize(), fill='#0a0a0a')
            self.info.itemconfigure(self.recTurn, fill=self.turn)
            
    def is_Loss(self):
        loss = True
        if (self.turn == 'black'):
            for i in range(8):
                for j in range(8):
                    if(self.data[i][j] == 'B'):
                        if ((i < 7 and j < 7 and self.data[i+1][j+1] == "1") or 
                            (i < 7 and j > 0 and self.data[i+1][j-1] == "1") or 
                            (i < 6 and j < 6 and "W" in self.data[i+1][j+1] and self.data[i+2][j+2] == "1") or 
                            (i < 6 and j > 1 and "W" in self.data[i+1][j-1] and self.data[i+2][j-2] == "1")):
                            loss = False
                    elif (self.data[i][j] == 'HB'):
                        if ((i < 7 and j < 7 and self.data[i+1][j+1] == "1") or
                            (i < 7 and j > 0 and self.data[i+1][j-1] == "1") or
                            (i > 0 and j < 7 and self.data[i-1][j+1] == "1") or
                            (i > 0 and j > 0 and self.data[i-1][j-1] == "1") or
                            (self.check_canAttackKing(i, j, 'B', 'R', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'B', 'L', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'T', 'R', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'T', 'L', self.turn)) ):
                            loss = False
        else:
            for i in range(8):
                for j in range(8):
                    if(self.data[i][j] == 'W'):
                        if ((i > 0 and j < 7 and self.data[i-1][j+1] == "1") or 
                            (i > 0 and j > 0 and self.data[i-1][j-1] == "1") or 
                            (i > 1 and j < 6 and "B" in self.data[i-1][j+1] and self.data[i-2][j+2] == "1") or 
                            (i > 1 and j > 1 and "B" in self.data[i-1][j-1] and self.data[i-2][j-2] == "1")):
                            loss = False
                    elif (self.data[i][j] == 'HW'):
                        if ((i < 7 and j < 7 and self.data[i+1][j+1] == "1") or
                            (i < 7 and j > 0 and self.data[i+1][j-1] == "1") or
                            (i > 0 and j < 7 and self.data[i-1][j+1] == "1") or
                            (i > 0 and j > 0 and self.data[i-1][j-1] == "1") or
                            (self.check_canAttackKing(i, j, 'B', 'R', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'B', 'L', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'T', 'R', self.turn)) or 
                            (self.check_canAttackKing(i, j, 'T', 'L', self.turn)) ):
                            loss = False                   
        if loss:
            self.endGame()

                              
root = Tk()
game = GameCheckers(root)
root.mainloop()
