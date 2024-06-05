from tkinter import ttk

class Button():
    def __init__(self, window, text, row, column, command):
        self.button = ttk.Button(window, text=text, command=command)
        self.button.grid(row=row, column=column, padx=10, pady=10)

    def disable_button(self):
        self.button.config(state='disabled')

    def enable_button(self):
        self.button.config('normal')

        