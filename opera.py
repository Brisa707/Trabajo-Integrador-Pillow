from PIL import ImageOps, ImageFilter

def cambiar_tamano(imagen, porcentaje):
    return imagen.resize((int(imagen.width * porcentaje / 100), int(imagen.height * porcentaje / 100)))

def convertir_a_grises(imagen):
    return ImageOps.grayscale(imagen)

def rotar_imagen(imagen, angulo=-90):
    return imagen.rotate(angulo, expand=True)

def aplicar_filtro(imagen, filtro):
    filtros = {
        1: ImageFilter.BLUR,
        2: ImageFilter.SHARPEN
    }
    if filtro in filtros:
        if imagen.mode != "RGB":
            imagen = imagen.convert("RGB")
        return imagen.filter(filtros[filtro])
    return imagen
