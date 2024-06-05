import tkinter as tk
from PIL import ImageTk

class Canvas():
    def __init__(self, window, column, rowspan, background):
        self.canvas_width = 200
        self.canvas_height = 200
        self.canvas = tk.Canvas(window, width=self.canvas_width, height=self.canvas_height, bg=background)
        self.canvas.grid(row=1, column=column, rowspan=rowspan, sticky=tk.NSEW)
      
    def show_image(self, image):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        size = (canvas_width, canvas_height)
        image.thumbnail(size)
        image_tk = ImageTk.PhotoImage(image) 
        self.canvas.delete("all")
        self.canvas.create_image(canvas_width / 2, canvas_height / 2, anchor=tk.CENTER, image=image_tk)
        self.canvas.image = image_tk
        