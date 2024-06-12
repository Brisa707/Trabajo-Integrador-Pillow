from PIL import Image, ImageOps, ImageFilter
#Yo usé la imagen C:\Repo-git\unab.jpg


def cargar_imagen(): #Función que carga la imagen a partir de la dirección provista por el usuario.
    ruta = input("Ingresa la ruta de la imagen: ")
    try:
        imagen = Image.open(ruta)
        print("Imagen cargada exitosamente.")
        return imagen
    except Exception as e:
        print(f"ERROR AL CARGAR LA IMAGEN: {e}")
        return None

def cambiar_tamano(imagen): #Función que cambia el tamaño de la imagen y la abre.  
    Porcentaje = int(input("Ingrese un porcentaje: ")) #Porcentaje del tamaño
    nueva_imagen = imagen.resize((int(imagen.width * Porcentaje / 100), int(imagen.height * Porcentaje / 100)))
    print("Tamaño de imagen cambiado.") 
    return nueva_imagen

def convertir_a_grises(imagen): #Función que convierte la imagen a escalade grises y la abre.
    nueva_imagen = ImageOps.grayscale(imagen)
    print("Imagen convertida a escala de grises.")
    return nueva_imagen

def rotar_imagen(imagen): #Función que rota la imagen 90° en sentido anti horario y la abre.
    angulo = -90
    nueva_imagen = imagen.rotate(angulo, expand=True)
    print("Imagen rotada.")
    return nueva_imagen

def aplicar_filtro(imagen): #Función que aplica un filtro a elección del usuario (enfocar y desenfocar) y la abre.
    print("Selecciona un filtro: ")
    print("1. Desenfocar")
    print("2. Enfocar")
    
    filtro = input("Ingrese una opción: ")
    
    filtros = {
        "1": ImageFilter.BLUR,
        "2": ImageFilter.SHARPEN
    }
    
    if filtro in filtros:
        nueva_imagen = imagen.filter(filtros[filtro])
        print("Filtro aplicado.")
        return nueva_imagen
    else:
        print("OPCIÓN DE FILTRO NO VALIDA.")
        return imagen

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Cambiar tamaño de la imagen")
    print("2. Convertir imagen a escala de grises")
    print("3. Rotar imagen")
    print("4. Aplicar filtro")
    print("5. Guardar cambios")
    print("6. Salir")

def main():
    imagen = cargar_imagen()
    if imagen is None:
        print("ERROR AL CARGAR LA IMAGEN.")
        return
    
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        if opcion == "1": #Cambia el tamaño de la imagen segun el porcentaje provisto por el usuario.
            imagen = cambiar_tamano(imagen)
            imagen.show()
        elif opcion == "2": #Cambia la imagen a blanco y negro
            imagen = convertir_a_grises(imagen)
            imagen.show()
        elif opcion == "3": #Rota la imagen 90°
            imagen = rotar_imagen(imagen)
            imagen.show()
        elif opcion == "4": #Aplica un filtro a elección del usuario
            imagen = aplicar_filtro(imagen)
            imagen.show()
        elif opcion == "5": #Permite elegir el nombre del archivo y lo guarda en formato "jpg".
            nuevo_nombre = str(input(f"Ingrese un nombre")) 
            print("Guardando cambios.")
            imagen.save(f"{nuevo_nombre}.jpg")
        elif opcion == "6": #Sale del programa sin guardar
            print("Saliendo del programa.")
            break
        else:
            print("OPCIÓN NO VALIDA. INTENTE DE NUEVO.")

        
if __name__ == "__main__":
    main()
