import tkinter
from tkinter.constants import DISABLED, NORMAL
import turtle
import random
import time

Header = "System 15" #Edit Header font Here
Paragraph = "System 10" #Edit Paragraph font Here
Title_Text = "Automatic Random Generated Drawing" #Edit Title Here
Background_Color = "#c9c9c9" #Edit Background color Here (Hex Code)
Icon_Address = "ARGD-logo-_2_.ico" #Edit Icon_Address
Size = 5 #Edit Pen Size
Color = "#000000" #Edit Color


root = tkinter.Tk()
root.iconbitmap(Icon_Address)
root.title(Title_Text)
root.resizable(False, False)
root.configure(bg=Background_Color)

Canvas = tkinter.Canvas(root, width=500, height=500, bg="white")
Canvas.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

turt = turtle.RawTurtle(Canvas)

Max_Rotation = 350 #Edit Maximum Rotation Degree Here
Min_Rotation = -350 #Edit Minimum Rotatio Degree Here
Max_Repeat = 30 #Edit Maximum Times Here
Min_Repeat = 15 #Edit Minimum Times Here
Max_Movement = 20 #Edit Maximum Movement Step Here
Min_Movement = 5 #Edit Minimum Movement Step Here

Rotation = random.randint(Min_Rotation, Max_Rotation)
Repeat = random.randint(Min_Repeat, Max_Repeat)
Movement = random.randint(Min_Movement, Max_Movement)

def Runs():
    turt.pensize(5)
    turt.color(
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=DISABLED)
    Run.grid(row=2, column=0, pady=5)
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=DISABLED)
    Reset.grid(row=2, column=1, pady=5)

    for i in range(Repeat):
        Algorithm = random.randint(1, 4)

        if (Algorithm == 1):
            turt.forward(Movement)
        elif (Algorithm == 2):
            turt.left(Rotation)
        elif (Algorithm == 3):
            turt.right(Rotation)
        else:
            turt.backward(Movement)
    
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=NORMAL)
    Reset.grid(row=2, column=1, pady=5)
    time.sleep(1)
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=NORMAL)
    Run.grid(row=2, column=0, pady=5)
         
def Resets():
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=DISABLED)
    Reset.grid(row=2, column=1, pady=5)
    turt.reset()
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=NORMAL)
    Run.grid(row=2, column=0, pady=5)
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=NORMAL)
    Reset.grid(row=2, column=1, pady=5)

Title = tkinter.Label(root, text=Title_Text ,font=Header)
Title.grid(row=0, column=0, columnspan=2, pady=5)
Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs)
Run.grid(row=2, column=0, pady=5)
Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets)
Reset.grid(row=2, column=1, pady=5)

root.mainloop()
