import tkinter
import tkinter as tk
import tkinter.font as tkfont
import turtle

class MyTkinterApp:
    def __init__(self, windowtext="SneakySnake"):
        self.root = tk.Tk()
        self.root.minsize(width=900, height=900)
        self.root.maxsize(width=900, height=900)
        self.root.title(windowtext)
        self.count = 0
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.color('black')

def main():
    myGUI = MyTkinterApp("SneakySnake")
    myGUI.root.mainloop()


if __name__ == "__main__":
    main()