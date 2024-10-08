from tkinter import *

class GameCheckers:
    def __init__(self, root):
        self.root = root
        self.root.title("Checkers (Thai version)")
        self.square_size = 100 # แนะนำขนานช่องที่ 75ถึง100 เพื่อความสวยงาม
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
                # สร้างตาราง
                if (self.data[i][j] == "0"):
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size
                                                 ,j*self.square_size+self.square_size,i*self.square_size+self.square_size
                                                 ,fill="#DAC6A3",tags=f"Chanel{i}{j}",state="disabled")
                else:
                    self.canvas.create_rectangle(j*self.square_size,i*self.square_size
                                                 ,j*self.square_size+self.square_size,i*self.square_size+self.square_size
                                                 ,fill="#95561E",tags=f"Chanel{i}{j}",state="disabled")
                
                # สร้างตัวหมากและใส่ฟังก์ชันให้ตัวหมากแต่ละตัวเมื่อกดจะไฮไลต์ช่องที่สามารถเดินได้
                if (self.data[i][j] == "B"):
                    self.canvas.create_oval(j*self.square_size+10,i*self.square_size+10
                                            ,j*self.square_size+self.square_size-10,i*self.square_size+self.square_size-10
                                            ,width=0,fill="black",tags=f"Pawn{i}{j}",state="disabled")
                    self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>"
                                         ,lambda event, i=i,j=j,team='black':self.hilighte_chanel(i, j, team))
                elif (self.data[i][j] == "W"):
                    self.canvas.create_oval(j*self.square_size+10,i*self.square_size+10
                                            ,j*self.square_size+self.square_size-10,i*self.square_size+self.square_size-10
                                            ,width=0,fill="white",tags=f"Pawn{i}{j}",state="disabled")
                    self.canvas.tag_bind(f"Pawn{i}{j}","<Button-1>"
                                         ,lambda event, i=i,j=j,team='white':self.hilighte_chanel(i, j, team))
                
                # ปรับให้ตัวหมากกดได้หากเป็นตา(turn)ของทีมนั้น
                if (self.trun == "white"):
                    if self.data[i][j] == "W":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")
                else:
                    if self.data[i][j] == "B":
                        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="",width=0,state="normal")       

    def hilighte_chanel(self, i, j, team):
        # ทำให้ทุกปุ่มกลับสู่สภาพเดิม
        for row in range(8):
            for column in range(8):
                self.canvas.itemconfigure(f"Pawn{row}{column}",outline="",width=0)
                self.canvas.itemconfigure(f"Chanel{row}{column}",fill="#DAC6A3" if self.data[row][column] == "0" else "#95561E",
                                          state="disable") 
                
        # เพิ่มกรอบสีเขียวให้ตัวหมากที่กด
        self.canvas.itemconfigure(f"Pawn{i}{j}",outline="green",width=3)
        
        # สร้างเงื่อนไขเช็คในกรณีที่ j เป็น 0หรือ7 หากไม่เช็คจะทำให้ IndexError หรือ ผลลัพท์ไม่เป็นตามที่คาดหวัง
        if (j in [0,7]):
            if (team == "black"):
                # จำต้องแยกเช็คทีละกรณี กรณีที่ j=0 และกรณีที่ j=7 เนื่องจากเงื่อนไขไม่เหมือนกัน
                if (j==0 and self.data[i+1][j+1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#39E75F" ,state="normal")
                elif (j==7 and self.data[i+1][j-1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#39E75F" ,state="normal")
            else:
                # จำต้องแยกเช็คทีละกรณี กรณีที่ j=0 และกรณีที่ j=7 เนื่องจากเงื่อนไขไม่เหมือนกัน
                if (j==0 and self.data[i-1][j+1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#39E75F" ,state="normal")
                elif (j==7 and self.data[i-1][j-1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#39E75F" ,state="normal")
        else:
            if (team == "black"):
                # ที่ต้องมี if 2ครั้งเพราะ ต้องเช็คทั้ง2ทางว่าทางไหนโล่งหรือมีค่าใน self.data เป็น 1 จะเปลี่ยนสีให้เป็นสีเขียว
                if (self.data[i+1][j+1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j+1}",fill="#39E75F" ,state="normal") 
                if (self.data[i+1][j-1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i+1}{j-1}",fill="#39E75F" ,state="normal")
            elif (team == "white"):
                # ที่ต้องมี if 2ครั้งเพราะ ต้องเช็คทั้ง2ทางว่าทางไหนโล่งหรือมีค่าใน self.data เป็น 1 จะเปลี่ยนสีให้เป็นสีเขียว
                if (self.data[i-1][j+1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j+1}",fill="#39E75F" ,state="normal")
                if (self.data[i-1][j-1] == "1"):
                    self.canvas.itemconfigure(f"Chanel{i-1}{j-1}",fill="#39E75F" ,state="normal")
                                 
root = Tk()
game = GameCheckers(root)
root.mainloop()
