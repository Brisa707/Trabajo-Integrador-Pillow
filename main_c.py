import tkinter as tk
from tkinter import simpledialog, messagebox
from util_c import cargar_imagen, mostrar_imagen, guardar_imagen
from opera_c import cambiar_tamano, convertir_a_grises, rotar_imagen, aplicar_filtro

class EditorDeImagenes:
    def __init__(self, root):
        self.root = root
        self.imagen = None
        self.ventana_imagen = None
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Editor de Imágenes")
        self.root.geometry("450x380")

        boton_style1 = {
            "padx": 15,
            "pady": 5,
            "bg": "#7b68ee",
            "fg": "white",
            "font": ("Arial", 15, "bold")
        }

        tk.Button(self.root, text="Cargar Imagen nueva", command=self.cargar_imagen, **boton_style1).pack(pady=5)
        tk.Button(self.root, text="Redimensionar Imagen", command=self.cambiar_tamano, **boton_style1).pack(pady=5)
        tk.Button(self.root, text="Convertir a Escala de Grises", command=self.convertir_a_grises, **boton_style1).pack(pady=5)
        tk.Button(self.root, text="Rotar Imagen", command=self.rotar_imagen, **boton_style1).pack(pady=5)
        tk.Button(self.root, text="Aplicar Filtro", command=self.aplicar_filtro, **boton_style1).pack(pady=5)
        tk.Button(self.root, text="Guardar Imagen", command=self.guardar_imagen, **boton_style1).pack(pady=5)

    def cargar_imagen(self):
        self.imagen = cargar_imagen()
        if self.imagen:
            self.mostrar_imagen()

    def cambiar_tamano(self):
        if self.imagen:
            porcentaje = simpledialog.askinteger("Perfecto!", "Ingrese un porcentaje:")
            if porcentaje:
                try:
                    self.imagen = cambiar_tamano(self.imagen, porcentaje)
                    self.mostrar_imagen()
                except ValueError as e:
                    messagebox.showwarning("Alerta!", str(e))
            else:
                messagebox.showwarning("Alerta!", "PORCENTAJE INVALIDO")
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def convertir_a_grises(self):
        if self.imagen:
            self.imagen = convertir_a_grises(self.imagen)
            self.mostrar_imagen()
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def rotar_imagen(self):
        if self.imagen:
            self.imagen = rotar_imagen(self.imagen)
            self.mostrar_imagen()
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def aplicar_filtro(self):
        if self.imagen:
            filtro = simpledialog.askinteger("Aplicar Filtro", "Seleccionar un filtro:\n1. Desenfocar\n2. Enfocar")
            try:
                self.imagen = aplicar_filtro(self.imagen, filtro)
                self.mostrar_imagen()
            except ValueError as e:
                messagebox.showwarning("Alerta!", str(e))
        else:
            messagebox.showwarning("Alerta!", "TE OLVIDASTE DE CARGAR LA IMAGEN")

    def mostrar_imagen(self):
        if self.ventana_imagen:
            self.ventana_imagen.destroy()
        self.ventana_imagen = mostrar_imagen(self.imagen, self.root)

    def guardar_imagen(self):
        guardar_imagen(self.imagen)

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorDeImagenes(root)
    root.mainloop()
