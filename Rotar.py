def rotar_imagen(imagen):
    angulo = -90
    nueva_imagen = imagen.rotate(angulo, expand=True)
    print("Imagen rotada.")
    return nueva_imagen