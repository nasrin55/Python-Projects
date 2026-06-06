from tkinter import*
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors Game')
root.config(bg='pink')
Label(root, text='Rock, Paper, Scissors ', font='arial 20 bold', bg='pink').pack()
user_take = StringVar()
Label(root, text='Choose any one: rock, paper, scissors', font='arial 15',
      bg='pink').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take,
      bg='whitesmoke').place(x=90, y=130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        result.set('tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        result.set('you loose, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        result.set('you win, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        result.set('you loose, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        result.set('you win, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        result.set('you loose, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        result.set('you win, computer select paper')
    else:
        result.set('Invalid: choose any one --- rock, paper, scissors')

def reset():
    result.set("")
    user_take.set("")

def exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=result,
        bg='whitesmoke').place(x=25, y= 250, height=25, width=345)

Button(root, font='arial 13 bold', text='PLAY', padx=5,
       bg='springgreen', command=play).place(x=150, y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,
       padx =5,bg ='springgreen' ,command = reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,
       padx =5,bg ='springgreen' ,command = exit).place(x=230,y=310)

root.mainloop()

















