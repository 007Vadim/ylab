#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Пинг-понг')
game = True
field = []
cross_count = 0


def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game
    game = True
    global cross_count
    cross_count = 0
    
    
def click(row, col):
    if game and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_lose('X')
        if game and cross_count < 51:
            computer_move()
            check_lose('O')

def game_over(player):                                                         
    global game
    game = False
    if player == 'X':
        messagebox.showinfo('Победитель', 'Победил комьютер')
    else:
        messagebox.showinfo('Победитель', 'Вы выиграли')
        
        
def check_lose(player):                                                         
    horizontal(player)
    vertical(player)
    diagonal(player)
   
        
def horizontal(player):
    series = 0
    r=[]
    for row in range(10):
        for col in range(10):
            if field[row][col]['text'] == player:
                series += 1
                r.append(field[row][col])
                if series == 5:
                    for i in r:
                        i['background'] = 'pink'
                    game_over(player)
            else:
                series = 0
                r=[]
        series = 0
        r=[]
        
        
def vertical(player):
    series = 0
    r=[]
    for col in range(10):
        for row in range(10):
            if field[row][col]['text'] == player:
                series += 1
                r.append(field[row][col])
                if series == 5:
                    for i in r:
                        i['background'] = 'pink'
                    game_over(player)                
            else:
                series = 0                
                r=[]
        series = 0
        r=[]
        
        
def diagonal(player):
    r=[]
    for row in range(10):
        for col in range(10):
            try:
                if (field[row][col]['text'] == player and
                    field[row + 1][col + 1]['text'] == player and
                    field[row + 2][col + 2]['text'] == player and
                    field[row + 3][col + 3]['text'] == player and
                    field[row + 4][col + 4]['text'] == player):
                        field[row][col]['background'] = 'pink'
                        field[row + 1][col + 1]['background'] = 'pink' 
                        field[row + 2][col + 2]['background'] = 'pink' 
                        field[row + 3][col + 3]['background'] = 'pink' 
                        field[row + 4][col + 4]['background'] = 'pink'
                        game_over(player)
                elif (field[row][col]['text'] == player and 
                      field[row + 1][col - 1]['text'] == player and
                    field[row + 2][col - 2]['text'] == player and
                    field[row + 3][col - 3]['text'] == player and
                    field[row + 4][col - 4]['text'] == player):
                        field[row][col]['background'] = 'pink'
                        field[row + 1][col - 1]['background'] = 'pink' 
                        field[row + 2][col - 2]['background'] = 'pink' 
                        field[row + 3][col - 3]['background'] = 'pink' 
                        field[row + 4][col - 4]['background'] = 'pink'
                        game_over(player)
            except IndexError:
                continue                

                
def computer_move():

    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
            
            
for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
    
    
new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=11, column=0, columnspan=10, sticky='nsew')
root.mainloop()


# In[ ]:




