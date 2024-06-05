from tkinter import filedialog, messagebox
from PIL import Image

class ImageFile():
    def __init__(self):
       self.image_path = None
       self.original_image = None
       self.modified_image = None
    
    def open_image(self):
        self.image_path = filedialog.askopenfilename(title="Seleccionar Imagen", filetypes=[("Archivos de imagen", "*.jpg *.png *.ico *.bmp")])
        if self.image_path:
            try:
                self.original_image = Image.open(self.image_path)
                self.modified_image = self.original_image.copy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al cargar la imagen: {e}")

        return self.original_image
        
    def save(self):
        if self.modified_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("BMP Files", "*.bmp")])
            if file_path:
                try:
                    self.modified_image.save(file_path)
                    messagebox.showinfo("Guardar Imagen", "Imagen guardada exitosamene!")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al guardar la imagen: {e}")
        else:
            messagebox.showwarning("Advertencia", "No hay ninguna imagen para guardar")
    
    def reset_image(self):
        if self.original_image is None:
            return
        self.modified_image = self.original_image.copy()
       

    def get_original_image(self):
        self.reset_image()
        return self.original_image
    
    def get_modified_image(self):
        return self.modified_image
        
    def __convert_to_rgb(self):
        self.reset_image()
        if self.modified_image.mode not in ('RGB', 'RGBA'):
            self.modified_image = self.modified_image.convert('RGB')

    def apply_sepia_filter(self):
        if self.modified_image is None:
            return 
        self.__convert_to_rgb()

        width, height = self.modified_image.size
        pixels = self.modified_image.load()

        for pixel_y in range(height):
            for pixel_x in range(width):
                if self.modified_image.mode == 'RGBA':
                    r, g, b, a = pixels[pixel_x, pixel_y]
                else:
                    r, g, b = pixels[pixel_x, pixel_y]
                    a = None

                red = int(0.393 * r + 0.796 * g + 0.189 * b)
                green = int(0.349 * r + 0.686 * g + 0.168 * b)
                blue = int(0.272 * r + 0.534 * g + 0.131 * b)
                
                if red > 255: 
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255

                if a is not None:
                    pixels[pixel_x, pixel_y] = (red, green, blue, a)
                else:
                    pixels[pixel_x, pixel_y] = (red, green, blue)

        return self.modified_image
        
    
    def apply_black_and_white(self):
        if self.modified_image is None:
            return
        
        self.__convert_to_rgb()
        color_base = 120
        gray = None
        width, height = self.modified_image.size
        pixels = self.modified_image.load()

        for pixel_y in range(height):
            for pixel_x in range(width):
                if self.modified_image.mode == 'RGBA':
                    r, g, b, a = pixels[pixel_x, pixel_y]
                    
                else:
                    r, g, b = pixels[pixel_x, pixel_y]
                    a = None
                    

                gray = (r + g + b) / 3
                if gray < color_base:
                    if a is not None:
                        pixels[pixel_x, pixel_y] = (0, 0, 0, a)
                    else:
                        pixels[pixel_x, pixel_y] = (0, 0, 0)
                else:
                    if a is not None:
                        pixels[pixel_x, pixel_y] = (255, 255, 255, a)
                    else:
                        pixels[pixel_x, pixel_y] = (255, 255, 255)
                
        return self.modified_image


    def apply_gray_scale(self):
        if self.modified_image is None:
            return
        
        self.__convert_to_rgb()
        width, height = self.modified_image.size
        pixels = self.modified_image.load()

        for pixel_y in range(height):
            for pixel_x in range(width):
                if self.modified_image.mode == 'RGBA':
                    r, g, b, a = pixels[pixel_x, pixel_y]
                else:
                    r, g, b = pixels[pixel_x, pixel_y]
                    a = None

                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                if a is not None:
                    pixels[pixel_x, pixel_y] = (gray, gray, gray, a)
                else:
                    pixels[pixel_x, pixel_y] = (gray, gray, gray)

        return self.modified_image
   
    def apply_negative_filter(self):
        if self.modified_image is None:
            return
        self.__convert_to_rgb()
        width, height = self.modified_image.size

        pixels = self.modified_image.load()
        for pixel_y in range(height):
            for pixel_x in range(width):
                if self.modified_image.mode == 'RGBA':
                    r, g, b, a = pixels[pixel_x, pixel_y]
                else:
                    r, g, b = pixels[pixel_x, pixel_y]
                    a = None

                if a is not None:
                    pixels[pixel_x, pixel_y] = (255 - r, 255 - g, 255 - b, a)
                else:
                    pixels[pixel_x, pixel_y] = (255 - r, 255 - g, 255 - b)

        return self.modified_image


    def mirror_mode(self):
        if self.modified_image is None:
            return
        self.__convert_to_rgb()
        width, height = self.modified_image.size
        mode = self.modified_image.mode
        pixels = self.modified_image.load()
        new_image_pixels = []
        data = None
        mirror_image = Image.new(mode, (width, height))
        
        for pixel_y in range(height):
            row = []
            for pixel_x in range(width):
                if mode == 'RGBA':
                    r, g, b, a = pixels[pixel_x, pixel_y]
                    data = (r, g, b, a)
                else:
                    r, g, b = pixels[pixel_x, pixel_y]
                    data = (r, g, b)

                row.append(data)
            row.reverse()
            new_image_pixels += row
        mirror_image.putdata(new_image_pixels)
        self.modified_image = mirror_image
        
        return self.modified_image