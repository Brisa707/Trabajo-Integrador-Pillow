from PIL import ImageOps
def convertir_a_grises(imagen):
    nueva_imagen = ImageOps.grayscale(imagen)
    print("Imagen convertida a escala de grises.")
    return nueva_imagen