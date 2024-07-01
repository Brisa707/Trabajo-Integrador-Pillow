import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps

imagen = None
ventana_imagen = None

# Función que carga una imagen y la muestra.
def cargar_imagen():
    global imagen
    ruta = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if ruta:
        try:
            imagen = Image.open(ruta)
            messagebox.showwarning("HABEMUS IMAGEN!", "SE CARGÓ EXITOSAMENTE")
            mostrar_imagen()
        except Exception:
            messagebox.showerror("Alerta!", "ERROR AL CARGAR LA IMAGEN!")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

# Función que aumenta o reduce una imagen.
def cambiar_tamano():
    global imagen
    if imagen:
        porcentaje = simpledialog.askinteger("Perfecto!", "Ingrese un porcentaje:")
        if porcentaje:
            imagen = imagen.resize((int(imagen.width * porcentaje / 100), int(imagen.height * porcentaje / 100)))
            messagebox.showwarning("QUE GRANDEEE!", "TAMAÑO DE LA IMAGEN MODIFICADO CORRECTAMENTE!")
            mostrar_imagen()
        else:
            messagebox.showwarning("Alerta!", "PORCENTAJE INVALIDO")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

# Cambia la imagen a blanco y negro.
def convertir_a_grises():
    global imagen
    if imagen:
        imagen = ImageOps.grayscale(imagen)
        messagebox.showwarning("QUE VINTAGE!", "IMAGEN EN BLANCO Y NEGRO")
        mostrar_imagen()
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

# Función que rota una imagen 90° en sentido horario
def rotar_imagen():
    global imagen
    if imagen:
        angulo = -90
        imagen = imagen.rotate(angulo, expand=True)
        messagebox.showwarning("QUE GIRO!", "IMAGEN ROTADA EXITOSAMENTE")
        mostrar_imagen()
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

# Función que aplica un filtro (desenfocar o enfocar) a elección del usuario.
def aplicar_filtro():
    global imagen
    if imagen:
        filtro = simpledialog.askinteger("Aplicar Filtro", "Seleccionar un filtro:\n1. Desenfocar\n2. Enfocar")
        filtros = {
            1: ImageFilter.BLUR,
            2: ImageFilter.SHARPEN
        }
        if filtro in filtros:
            # Convertir la imagen a modo "RGB" si no está en ese modo
            if imagen.mode != "RGB":
                imagen = imagen.convert("RGB")
            imagen = imagen.filter(filtros[filtro])
            messagebox.showwarning("Muy bien!", "FILTRO APLICADO EXITOSAMENTE")
            mostrar_imagen()
        else:
            messagebox.showwarning("Alerta!", "VALOR NO VALIDO")
    else:
        messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

# Función que muestra la imagen con las modificaciones hasta el momento
def mostrar_imagen():
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

# Función que guarda la imagen con todas las modificaciones hechas hasta el momento.
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

root = tk.Tk()
root.title("Editor de Imágenes")
root.geometry("450x380")  # Establece el tamaño inicial de la ventana

# Aplicar un estilo a los botones
boton_style1 = {
    "padx": 15,
    "pady": 5,
    "bg": "#7b68ee",
    "fg": "white",
    "font": ("Arial", 15, "bold")
}

boton_cargar = tk.Button(root, text="Cargar Imagen nueva", command=cargar_imagen, **boton_style1)
boton_cargar.pack(pady=5)

boton_redimensionar = tk.Button(root, text="Redimensionar Imagen", command=cambiar_tamano, **boton_style1)
boton_redimensionar.pack(pady=5)

boton_escala_grises = tk.Button(root, text="Convertir a Escala de Grises", command=convertir_a_grises, **boton_style1)
boton_escala_grises.pack(pady=5)

boton_rotar = tk.Button(root, text="Rotar Imagen", command=rotar_imagen, **boton_style1)
boton_rotar.pack(pady=5)

boton_filtro = tk.Button(root, text="Aplicar Filtro", command=aplicar_filtro, **boton_style1)
boton_filtro.pack(pady=5)

boton_guardado = tk.Button(root, text="Guardar Imagen", command=guardar_imagen, **boton_style1)
boton_guardado.pack(pady=5)

root.mainloop()
