import sys
import tkinter as tk
from tkinter import Menu, messagebox

from Widgets.window import Window
from Widgets.button import Button
from Widgets.menu import MainMenu
from Widgets.canvas import Canvas
from ImageFile.imageFile import ImageFile

def create_widgets():
    main_menu = Menu(root)
    no_separator = False
    file_menu = MainMenu(main_menu,'Archivo')
    file_menu.create_option('Abrir', open_image)
    file_menu.create_option('Guardar', image_file.save)
    file_menu.create_option('Salir', exit, no_separator)
    file_menu.add_menu()
    
    edit_menu = MainMenu(main_menu, 'Filtros')
    edit_menu.create_option('Sepia', sepia_filter)
    edit_menu.create_option('Blanco y Negro', black_white_filter)
    edit_menu.create_option('Escala de Grises', gray_scale)
    edit_menu.create_option('Negativo', negative_filter)
    edit_menu.create_option('Modo Espejo', mirror_mode)
    edit_menu.create_option('Deshacer', reset_image, no_separator)
    edit_menu.add_menu()

    help_menu = MainMenu(main_menu, 'Ayuda')
    help_menu.create_option('Bienvenido', welcome)
    help_menu.create_option('Acerca de', about)
    help_menu.create_option('Ver código fuente', view_code, no_separator)
    help_menu.add_menu()

    root.config(menu=main_menu)

    open_button = Button(root , 'Abrir', 0, 2, command=open_image)
    save_button = Button(root, 'Guardar', 1, 2, command=image_file.save)
    reset_button = Button(root, 'Reiniciar', 2, 2, command=reset_image)
    sepia_button = Button(root, 'Sepia', 3, 2 , command=sepia_filter)
    black_white_button = Button(root, 'Blanco y Negro', 4, 2, command=black_white_filter)
    gray_button = Button(root, 'Escala de Gris', 5, 2, command=gray_scale)
    negative_button = Button(root, 'Negativo', 6, 2, command=negative_filter)
    mirror_mode_button = Button(root, 'Espejo', 7, 2, command=mirror_mode)

def open_image():
    image = image_file.open_image()
    if image:
        canvas.show_image(image)
        canvas_modified_image.show_image(image)

def show_warning():
    messagebox.showwarning('Advertencia', 'Primero debes abrir una imagen.')
        
    
def sepia_filter():
    image = image_file.apply_sepia_filter()
    if image:
        canvas_modified_image.show_image(image)
    else:
        show_warning()
            
def black_white_filter():
    image = image_file.apply_black_and_white()
    if image:
        canvas_modified_image.show_image(image)
    else:
        show_warning()
    
def gray_scale():
    image = image_file.apply_gray_scale()
    if image:
        canvas_modified_image.show_image(image)
    else:
        show_warning()

def negative_filter():
    image = image_file.apply_negative_filter()
    if image:
        canvas_modified_image.show_image(image)
    else:
        show_warning()

def mirror_mode():
    image = image_file.mirror_mode()
    if image:
        canvas_modified_image.show_image(image)
    else:
        show_warning()

def reset_image():
    image = image_file.get_original_image()
    if image:
        canvas.show_image(image)
        canvas_modified_image.show_image(image)
    else:
        show_warning()

def exit():
    root.quit()
    root.destroy
    sys.exit()   

def about():
    messagebox.showinfo('Acerca de', 'Editor de Imágenes v1.0')

def welcome():
    message = (
    'Bienvenido a Editor de Imágenes\n'
    'Podrás editar imagenes aplicando varios filtros\n'
    'y después podrás guardar los cambios hechos.' )
    messagebox.showinfo('Bienvenido', message)

def view_code():
    messagebox.showinfo('Ver código fuente', 'Puedes ver el código fuente en: @github.com')

if __name__ == '__main__':
    root = Window()
    
    image_file = ImageFile()
    label = tk.Label(root, text='Imagen Original')
    label.grid(row=0, column=0, padx=0)
    label2 = tk.Label(root, text='Imagen Modificada')
    label2.grid(row=0, column=1)
    canvas = Canvas(root, 0, 8, 'lightblue')
    canvas_modified_image = Canvas(root, 1, 8, 'white')
    create_widgets()
    
    root.mainloop()
