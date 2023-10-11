#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import SimpleGUICS2Pygame.simpleguics2pygame as sg
import random
easy_medium_hard = False
hint = 0
chance = 5
win = False
game_over = False
import math
class Sudoku:
    def __init__(self, N):
        self.N = N
        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)
        self.mat = [[0 for _ in range(N)] for _ in range(N)]
     
    def fillValues(self):
        # Fills the diagonal of SRN x SRN matrices
        self.fillDiagonal()
 
        # Fills remaining blocks
        self.fillRemaining(0, self.SRN)
     
    def fillDiagonal(self):
        for i in range(0, self.N, self.SRN):
            self.fillBox(i, i)
     
    def unUsedInBox(self, rowStart, colStart, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart + i][colStart + j] == num:
                    return False
        return True
     
    def fillBox(self, row, col):
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.randomGenerator(self.N)
                    if self.unUsedInBox(row, col, num):
                        break
                self.mat[row + i][col + j] = num
     
    def randomGenerator(self, num):
        return math.floor(random.random() * num + 1)
     
    def checkIfSafe(self, i, j, num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
     
    def unUsedInRow(self, i, num):
        for j in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    def unUsedInCol(self, j, num):
        for i in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    
    def fillRemaining(self, i, j):
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True
     
        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0
     
        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self.fillRemaining(i, j + 1)
     
        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.checkIfSafe(i, j, num):
                self.mat[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
                self.mat[i][j] = 0
         
        # No valid value was found, so backtrack
        return False

def Hint():
    global r,c,hint,win
    i = 0 
    while i != 1:
        r1 = random.randint(0,8)
        c1 = random.randint(0,8)
        if main[c1][r1] == 0:
            i = 1
            c = c1
            r = r1
            main[c][r] = solve[c][r] 
            hint = 1
    if won():
        win = True
        timer.stop()
def new_game():
    global main,l1,solve,wrong,inp,r,c,M,win,sec,min,pl_pa,time1,chance,game_over,easy_medium_hard,hint,puzzle,t1
    N = 9
    easy_medium_hard = False
    sudoku = Sudoku(N)
    sudoku.fillValues()
    solve=sudoku.mat
    c = diffculty
    main =  [[0 for _ in range(9)]for _ in range(9)]
    puzzle = [[0 for _ in range(9)]for _ in range(9)]
    for i in range(len(main)):
        for j in range(len(main)):
            main[i][j] = solve[i][j]
    l1 = [1,2,3,4,5,6,7,8,9]
    hint = 0
    wrong = [[0 for _ in range(9)]for _ in range(9)]
    inp = ""
    while (c != 0):
        i = random.randint(0,8)
        j = random.randint(0,8)
        if (main[i][j]!= 0):
            c -= 1
            main[i][j] = 0
    for i in range(len(main)):
        for j in range(len(main)):
            puzzle[i][j] = main[i][j]
    r = 0
    c = 0
    M = 9
    win = False
    sec = 0
    min = 0
    pl_pa = "play"
    time1 = ""
    chance = 5
    game_over = False
    timer.start()
    t1 = 0

def restart():
    global main,l1,solve,wrong,inp,r,c,M,z,win,sec,min,pl_pa,time1,chance,game_over,grid2,hint,puzzle,t1
    N = 9
    sudoku = Sudoku(N)
    sudoku.fillValues()
    solve=sudoku.mat
    main = [[0 for _ in range(9)]for _ in range(9)]
    for i in range(len(main)):
        for j in range(len(main)):
            main[i][j] = solve[i][j]
    puzzle = [[0 for _ in range(9)]for _ in range(9)]
    l1 = [1,2,3,4,5,6,7,8,9]
    hint = 0
    c = diffculty
    wrong = [[0 for _ in range(9)]for _ in range(9)]
    inp = ""
    while (c != 0):
        i = random.randint(0,8)
        j = random.randint(0,8)
        if (main[i][j]!= 0):
            c -= 1
            main[i][j] = 0
    for i in range(len(main)):
        for j in range(len(main)):
            puzzle[i][j] = main[i][j]
    r = 0
    c = 0
    M = 9
    win = False
    sec = 0
    min = 0
    pl_pa = "play"
    time1 = ""
    chance = 5
    game_over = False
    timer.start()
    t1 = 0
    
def pause():
    global pl_pa
    timer.stop()
    pl_pa = "pause"

def play():
    global pl_pa
    if win==False:
        timer.start()
    pl_pa="play"


def time():
    global sec,min,time1
    if sec>=59:
        sec = 0
        min += 1
    else:
        sec+=1
    second = sec
    minu = min
    if sec<10:
        second = f"0{sec}"
    if min<10:
        minu =f"0{min}"
    

def erase():
    global main
    if puzzle[c][r] == 0:
        main[c][r] = 0

def won():
    for i in main:
        if 0 in i:
            return False
    return True
    

def key(key):
    global r,c,solve,inp,win,chance,game_over,wrong
    if puzzle[c][r] == 0:
        if key in [sg.KEY_MAP['1'],sg.KEY_MAP['2'],sg.KEY_MAP['3'],sg.KEY_MAP['4'],sg.KEY_MAP['5'],sg.KEY_MAP['6'],sg.KEY_MAP['7'],sg.KEY_MAP['8'],sg.KEY_MAP['9']]:
            inp = chr(key)
            main[c][r] = int(inp)
            if solve[c][r] != int(inp):
                wrong[c][r] = 1
                chance -=1
            else:
                wrong[c][r] = 0
            if won():
                win = True
                timer.stop()
            if chance == 0:
                game_over = True
                timer.stop()
        if key == sg.KEY_MAP['0']:
            main[c][r]=0
    if key == sg.KEY_MAP["left"]:
        if c>0:
            c-=1
    if key == sg.KEY_MAP["right"]:
        if c<8:
            c+=1
    if key == sg.KEY_MAP["up"]:
        if r>0:
            r-=1
    if key == sg.KEY_MAP["down"]:
        if r<8:
            r+=1
def click(pos):
    global r,c,diffculty,easy_medium_hard,main,wrong,chance,win,game_over
    current_pos = pos
    if easy_medium_hard == False:
        if current_pos[0]>125 and current_pos[0]<355:
            if current_pos[1]>200 and current_pos[1]<250:
                diffculty = random.randint(30,40)
            if current_pos[1]>275 and current_pos[1]<325:
                diffculty = random.randint(40,50,)
            if current_pos[1]>350 and current_pos[1]<400:
                diffculty = random.randint(50,60)
            easy_medium_hard = True
            restart()
    elif game_over == True or win == True:
        if current_pos[0]>125 and current_pos[0]<325 and current_pos[1]>275 and current_pos[1]<325:
            new_game()
            
    else:
        if current_pos[1] > 530:
            if 10<current_pos[0] and current_pos[0]<90 and 540<current_pos[1] and current_pos[1]<560:
                erase()
            elif 100<current_pos[0] and current_pos[0]<180 and 540<current_pos[1] and current_pos[1]<560:
                pause()
                
            elif 190<current_pos[0] and current_pos[0]<270 and 540<current_pos[1] and current_pos[1]<560:
                restart()
                
            elif 280<current_pos[0] and current_pos[0]<360 and 540<current_pos[1]and current_pos[1]<560:
                new_game()
                
            elif 370<current_pos[0] and current_pos[0]<440 and 540<current_pos[1] and current_pos[1]<560:
                if hint == 0:
                    Hint() 
        elif current_pos[1] > 450 and current_pos[1]<500:
            if puzzle[c][r] == 0:
                for i in range(9):
                    if i*50<current_pos[0] and i*50+50>current_pos[0] and 450<current_pos[1] and current_pos[1]<500:
                        main[c][r] = i+1
                        if solve[c][r] != i+1:
                            wrong[c][r] = 1
                            chance -=1
                        else:
                            wrong[c][r] = 0
                        if won():
                            win = True
                            timer.stop()
                        if chance == 0:
                            game_over = True
                            timer.stop()
                        
                        
        elif pl_pa == "pause":
            if 125<current_pos[0] and current_pos[0]<325 and 275<current_pos[1] and current_pos[1]<325:
                play()
        else:
            if 0<current_pos[0] and current_pos[0]<450 and 0<current_pos[1] and current_pos[1]<450:
                r = current_pos[1]//50
                c = current_pos[0]//50

def draw(canvas):
    global t1
    if easy_medium_hard == False:
        frame.set_canvas_background("white")
        canvas.draw_text("Sudoku",[80,100],100,"blue")
        canvas.draw_polygon([[125,200],[325,200],[325,250],[125,250]],1,"black","#d3d3d3")
        canvas.draw_polygon([[125,275],[325,275],[325,325],[125,325]],1,"black","#d3d3d3")
        canvas.draw_polygon([[125,350],[325,350],[325,400],[125,400]],1,"black","#d3d3d3")
        canvas.draw_text(f"Easy",[195,240],35,"black")
        canvas.draw_text(f"Medium",[165,315],35,"black")
        canvas.draw_text(f"Hard",[195,390],35,"black")    
    elif win:
        canvas.draw_text(f"You Win In {time1}",[50,250],35,"blue")
        frame.set_canvas_background("white")
        canvas.draw_polygon([[125,275],[325,275],[325,325],[125,325]],1,"black","#d3d3d3")
        canvas.draw_text("New Game",[150,315],35,"black")
    elif game_over:
        canvas.draw_text(f"Game Over",[140,250],35,"blue")
        frame.set_canvas_background("white")
        canvas.draw_polygon([[125,275],[325,275],[325,325],[125,325]],1,"black","#d3d3d3")
        canvas.draw_text("New Game",[150,315],35,"black")
    elif pl_pa == "pause":
        canvas.draw_polygon([[125,275],[325,275],[325,325],[125,325]],1,"black","#d3d3d3")
        canvas.draw_text("Play",[195,315],35,"black")
        canvas.draw_text(f"Sudoku",[175,250],35,"blue")
        frame.set_canvas_background("white")
    else:
        frame.set_canvas_background("white")
        if main[c][r] != 0:
            for i in range(9):
                for j in range(9):
                    if main[c][r] == main[i][j]:
                        canvas.draw_polygon([[i*50,j*50],[50+i*50,j*50],[50+i*50,50+j*50],[i*50,50+j*50]],1,"#add8e6","#add8e6")
        for i in range(9):
            canvas.draw_polygon([[c*50,i*50],[50+c*50,i*50],[50+c*50,50+i*50],[c*50,50+i*50]],1,"#D3D3D3","#D3D3D3")
        for i in range(9):
            canvas.draw_polygon([[i*50,r*50],[50+i*50,r*50],[50+i*50,50+r*50],[i*50,50+r*50]],1,"#D3D3D3","#D3D3D3")
        startCol = r - r % 3
        startRow = c - c % 3
        for i in range(3):
            for j in range(3):
                canvas.draw_polygon([[(i+startRow)*50,(j+startCol)*50],[50+(i+startRow)*50,(j+startCol)*50],[50+(i+startRow)*50,50+(j+startCol)*50],[(i+startRow)*50,50+(j+startCol)*50]],1,"#D3D3D3","#D3D3D3")
        canvas.draw_polygon([[c*50,r*50],[50+c*50,r*50],[50+c*50,50+r*50],[c*50,50+r*50]],1,"black","#90EE90")
        for i in range(9):
            for j in range(9):
                if main[i][j] in l1:
                    canvas.draw_text(str(main[i][j]),[i*50+20,j*50+33],25,"black")
                    if wrong[i][j] == 1:
                        canvas.draw_text(str(main[i][j]),[i*50+20,j*50+33],25,"red")
        for i in range(9):
            if (i+1)%3==0:
                canvas.draw_line([50+50*i,0],[50+50*i,450],4,"black")
            else:
                canvas.draw_line([50+50*i,0],[50+50*i,450],2,"black")
        for i in range(9):
            if (i+1)%3==0:
                canvas.draw_line([0,50+50*i],[450,50+50*i],4,"black")
            else:
                canvas.draw_line([0,50+50*i],[450,50+50*i],2,"black")
        for i in range(9):
            canvas.draw_text(str(i+1),[i*50+10,495],50,"blue")
        
        canvas.draw_line([0,500],[450,500],2,"black")
        
        canvas.draw_text(time1,[50,525],20,"black")
        canvas.draw_text(f"Chance :{chance}/5",[300,525],20,"black")
        canvas.draw_line([0,530],[450,530],2,"black")
        canvas.draw_polygon([[10,540],[90,540],[90,560],[10,560]],1,"black","#d3d3d3")
        canvas.draw_polygon([[100,540],[180,540],[180,560],[100,560]],1,"black","#d3d3d3")
        canvas.draw_polygon([[190,540],[270,540],[270,560],[190,560]],1,"black","#d3d3d3")
        canvas.draw_polygon([[280,540],[360,540],[360,560],[280,560]],1,"black","#d3d3d3")
        canvas.draw_text(f"Erase",[30,555],17,"black")
        canvas.draw_text(f"Pause",[120,555],17,"black")
        canvas.draw_text(f"Restart",[205,555],17,"black")
        canvas.draw_text(f"New Game",[280,555],17,"black")
        if hint == 0: 
            canvas.draw_polygon([[370,540],[440,540],[440,560],[370,560]],1,"black","#d3d3d3")
            canvas.draw_text(f"Hint",[390,555],17,"black")
            

frame = sg.create_frame("Sudoku",450,570,0)
timer = sg.create_timer(1000,time)
frame.set_draw_handler(draw)
frame.set_canvas_background("white")
frame.set_mouseclick_handler(click)
frame.set_keyup_handler(key)
frame.start()


# In[ ]:




