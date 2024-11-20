from pl import Agsat
from tkinter import *

if __name__ == "__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (1500, 800, 200, 100))
    screen.title("Dr.Niknam")
    screen.resizable(False, False)
    paheme = Agsat.App(screen)
    screen.mainloop()
