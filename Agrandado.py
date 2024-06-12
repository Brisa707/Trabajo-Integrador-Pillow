
def cambiar_tamano(imagen):
    Porcentaje = int(input("Ingrese un porcentaje: "))
    nueva_imagen = imagen.resize((int(imagen.width * Porcentaje / 100), int(imagen.height * Porcentaje / 100)))
    print("Tamaño de imagen cambiado.")
    return nueva_imagen