from pl import Agsat
from tkinter import *

def setup_window():
    screen = Tk()

    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()


    window_width = int(screen_width * 1.0)
    window_height = int(screen_height * 1.0)


    screen.geometry(f"{window_width}x{window_height}")
    screen.title("Dr.Niknam")


    paheme = Agsat.App(screen)


    screen.mainloop()

if __name__ == "__main__":
    setup_window()

