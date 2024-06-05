from tkinter import Menu

class MainMenu():
    
    def __init__(self, main_menu, label_menu):
        self.main_menu = main_menu
        self.label_menu = label_menu   
        self.submenu = Menu(self.main_menu, tearoff=0)     
    
    def create_option(self, label_option, command, separator = True):
        #Add new option to main menu
        self.submenu.add_command(label=label_option, command=command)
        if separator:
            self.submenu.add_separator()
        
    def add_menu(self):    
        #add submenu to main menu
        self.main_menu.add_cascade(menu=self.submenu, label=self.label_menu)

    




