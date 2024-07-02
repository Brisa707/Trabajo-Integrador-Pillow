import tkinter as tk
from tkinter import simpledialog, messagebox
from util import cargar_imagen, mostrar_imagen, guardar_imagen
from opera import cambiar_tamano, convertir_a_grises, rotar_imagen, aplicar_filtro
from PIL import Image

imagen = None

def main():
    def cambiar_tamano_wrapper():
        global imagen
        if imagen:
            porcentaje = simpledialog.askinteger("Perfecto!", "Ingrese un porcentaje:")
            if porcentaje:
                imagen = cambiar_tamano(imagen, porcentaje)
                messagebox.showwarning("QUE GRANDEEE!", "TAMAÑO DE LA IMAGEN MODIFICADO CORRECTAMENTE!")
                mostrar_imagen(root)
            else:
                messagebox.showwarning("Alerta!", "PORCENTAJE INVALIDO")
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def convertir_a_grises_wrapper():
        global imagen
        if imagen:
            imagen = convertir_a_grises(imagen)
            messagebox.showwarning("QUE VINTAGE!", "IMAGEN EN BLANCO Y NEGRO")
            mostrar_imagen(root)
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def rotar_imagen_wrapper():
        global imagen
        if imagen:
            imagen = rotar_imagen(imagen)
            messagebox.showwarning("QUE GIRO!", "IMAGEN ROTADA EXITOSAMENTE")
            mostrar_imagen(root)
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def aplicar_filtro_wrapper():
        global imagen
        if imagen:
            filtro = simpledialog.askinteger("Aplicar Filtro", "Seleccionar un filtro:\n1. Desenfocar\n2. Enfocar")
            if filtro:
                imagen = aplicar_filtro(imagen, filtro)
                messagebox.showwarning("Muy bien!", "FILTRO APLICADO EXITOSAMENTE")
                mostrar_imagen(root)
            else:
                messagebox.showwarning("Alerta!", "VALOR NO VALIDO")
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    global root
    root = tk.Tk()
    root.title("Editor de Imágenes")
    root.geometry("450x380")  # Establece el tamaño inicial de la ventana

    boton_style1 = {
        "padx": 15,
        "pady": 5,
        "bg": "#7b68ee",
        "fg": "white",
        "font": ("Arial", 15, "bold")
    }

    tk.Button(root, text="Cargar Imagen nueva", command=lambda: cargar_imagen(root), **boton_style1).pack(pady=5)
    tk.Button(root, text="Redimensionar Imagen", command=cambiar_tamano_wrapper, **boton_style1).pack(pady=5)
    tk.Button(root, text="Convertir a Escala de Grises", command=convertir_a_grises_wrapper, **boton_style1).pack(pady=5)
    tk.Button(root, text="Rotar Imagen", command=rotar_imagen_wrapper, **boton_style1).pack(pady=5)
    tk.Button(root, text="Aplicar Filtro", command=aplicar_filtro_wrapper, **boton_style1).pack(pady=5)
    tk.Button(root, text="Guardar Imagen", command=guardar_imagen, **boton_style1).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()