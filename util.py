import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk

imagen = None
ventana_imagen = None

def cargar_imagen(root):
    global imagen
    ruta = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if ruta:
        try:
            imagen = Image.open(ruta)
            messagebox.showwarning("HABEMUS IMAGEN!", "SE CARGÓ EXITOSAMENTE")
            mostrar_imagen(root)
        except Exception:
            messagebox.showerror("Alerta!", "ERROR AL CARGAR LA IMAGEN!")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

def mostrar_imagen(root):
    global imagen, ventana_imagen
    if imagen:
        if ventana_imagen:
            ventana_imagen.destroy()
        ventana_imagen = tk.Toplevel(root)
        ventana_imagen.title("Imagen")
        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(ventana_imagen, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.pack()
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

def guardar_imagen():
    global imagen
    if imagen:
        nuevo_nombre = simpledialog.askstring("Guardar imagen", "Ingrese un nombre:")
        if nuevo_nombre:
            imagen.save(f"{nuevo_nombre}.jpg")
            messagebox.showwarning("Muy bien", f"IMAGEN GUARDADA COMO {nuevo_nombre}.jpg")
        else:
            messagebox.showwarning("Alerta!", "NOMBRE NO VALIDO")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")