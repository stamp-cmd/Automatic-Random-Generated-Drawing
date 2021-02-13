import tkinter
from tkinter.constants import DISABLED, NORMAL
import turtle
import random
import time

root = tkinter.Tk()
root.iconbitmap("ARGD\ARGD-logo-_2_.ico")
root.title("Automatic Random Generated Drawing")
root.resizable(False, False)
root.configure(bg="#c9c9c9")

Header = "System 15"
Paragraph = "System 10"

Canvas = tkinter.Canvas(root, width=500, height=500, bg="white")
Canvas.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

t = turtle.RawTurtle(Canvas)

Rotation = random.randint(-350, 350)
Repeat = random.randint(15, 30)
Movement = random.randint(5, 40)

def Runs():
    t.pensize(5)
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=DISABLED)
    Run.grid(row=2, column=0, pady=5)
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=DISABLED)
    Reset.grid(row=2, column=1, pady=5)

    for i in range(Repeat):
        Algorithm = random.randint(1, 4)

        if (Algorithm == 1):
            t.forward(Movement)
        elif (Algorithm == 2):
            t.left(Rotation)
        elif (Algorithm == 3):
            t.right(Rotation)
        else:
            t.backward(Movement)
    
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=NORMAL)
    Reset.grid(row=2, column=1, pady=5)
    time.sleep(1)
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=NORMAL)
    Run.grid(row=2, column=0, pady=5)
         
def Resets():
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=DISABLED)
    Reset.grid(row=2, column=1, pady=5)
    t.reset()
    Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs , state=NORMAL)
    Run.grid(row=2, column=0, pady=5)
    Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets, state=NORMAL)
    Reset.grid(row=2, column=1, pady=5)

Title = tkinter.Label(root, text="Automatic Random Generated Drawing" ,font=Header)
Title.grid(row=0, column=0, columnspan=2, pady=5)
Run = tkinter.Button(root, text="Run", font=Paragraph, width=10, command=Runs)
Run.grid(row=2, column=0, pady=5)
Reset = tkinter.Button(root, text="Reset", font=Paragraph, width=10, command=Resets)
Reset.grid(row=2, column=1, pady=5)

root.mainloop()