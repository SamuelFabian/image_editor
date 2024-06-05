import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x800+50+50')
        self.title('Editor de Imágenes')
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        for i in range(9):
            self.grid_rowconfigure(i, weight=1)
            if i == 8:
                self.grid_rowconfigure(i, weight=4)

