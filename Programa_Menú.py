import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageFilter, ImageOps

def abrir_imagen():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.bmp")])
    if img_path:
        img = Image.open(img_path)
        img.show()

def guardar_imagen(imagen):
    ruta_guardado = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos los archivos", "*.*")])
    if ruta_guardado:
        imagen.save(ruta_guardado)

def aplicar_filtro():
    if img:
        img_filtrada = img.filter(ImageFilter.BLUR)
        img_filtrada.show()
        guardar_imagen(img_filtrada)

def redimensionar_imagen():
    if img:
        nuevo_ancho = simpledialog.askinteger("Entrada", "Ingresa el nuevo ancho:")
        nuevo_alto = simpledialog.askinteger("Entrada", "Ingresa el nuevo alto:")
        img_redimensionada = img.resize((nuevo_ancho, nuevo_alto))
        img_redimensionada.show()
        guardar_imagen(img_redimensionada)

def recortar_imagen():
    if img:
        izquierda = simpledialog.askinteger("Entrada", "Ingresa la coordenada izquierda:")
        arriba = simpledialog.askinteger("Entrada", "Ingresa la coordenada superior:")
        derecha = simpledialog.askinteger("Entrada", "Ingresa la coordenada derecha:")
        abajo = simpledialog.askinteger("Entrada", "Ingresa la coordenada inferior:")
        img_recortada = img.crop((izquierda, arriba, derecha, abajo))
        img_recortada.show()
        guardar_imagen(img_recortada)

def convertir_a_escala_grises():
    if img:
        img_gris = ImageOps.grayscale(img)
        img_gris.show()
        guardar_imagen(img_gris)

# Crear la ventana principal
root = tk.Tk()
root.title("Editor de Imágenes")

# Crear botones para las funciones
boton_abrir = tk.Button(root, text="Abrir Imagen", command=abrir_imagen)
boton_abrir.pack()

boton_filtro = tk.Button(root, text="Aplicar Filtro", command=aplicar_filtro)
boton_filtro.pack()

boton_redimensionar = tk.Button(root, text="Redimensionar Imagen", command=redimensionar_imagen)
boton_redimensionar.pack()

boton_recortar = tk.Button(root, text="Recortar Imagen", command=recortar_imagen)
boton_recortar.pack()

boton_escala_grises = tk.Button(root, text="Convertir a Escala de Grises", command=convertir_a_escala_grises)
boton_escala_grises.pack()

# Ejecutar el bucle principal de la ventana
root.mainloop()
