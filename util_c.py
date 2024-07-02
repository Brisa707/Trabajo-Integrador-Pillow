import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk

def cargar_imagen():
    ruta = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if ruta:
        try:
            return Image.open(ruta)
        except Exception:
            messagebox.showerror("Alerta!", "ERROR AL CARGAR LA IMAGEN!")
            return None
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")
        return None

def mostrar_imagen(imagen, root):
    if imagen:
        ventana_imagen = tk.Toplevel(root)
        ventana_imagen.title("Imagen")
        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(ventana_imagen, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.pack()
        return ventana_imagen
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

def guardar_imagen(imagen):
    if imagen:
        nuevo_nombre = simpledialog.askstring("Guardar imagen", "Ingrese un nombre:")
        if nuevo_nombre:
            imagen.save(f"{nuevo_nombre}.jpg")
            messagebox.showinfo("Muy bien", f"IMAGEN GUARDADA COMO {nuevo_nombre}.jpg")
        else:
            messagebox.showwarning("Alerta!", "NOMBRE NO VALIDO")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")
