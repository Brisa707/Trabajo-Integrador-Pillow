from PIL import Image, ImageOps, ImageFilter
#Yo usé la imagen C:\Repo-git\unab.jpg


def cargar_imagen():
    while True:
        ruta = str(input("Ingresa la ruta de la imagen: "))
        try:
            imagen = Image.open(ruta)
            print("""\033[1mIMAGEN CARGADA EXITOSAMENTE.\033[0m
                  """)
            return imagen
        except Exception:
                        print("""\033[1mERROR AL CARGAR LA IMAGEN. INTENTE DE NUEVO.\033[0m
                  """)
                        opcion = input("¿Desea intentar de nuevo? S/N: ").upper()
                        if opcion == "N":
                            print("""\033[1mSALIENDO DEL PROGRAMA. CHAU!\033[0m
                                  """)
                            break
                        elif opcion == "S":
                            continue
                        else:
                            print("""\033[1mOPCIÓN NO VALIDA!!!\033[0m
                  """)
            
                

def cambiar_tamano(imagen):
    Porcentaje = int(input("INGRESE UN PORCENTAJE: "))
    nueva_imagen = imagen.resize((int(imagen.width * Porcentaje / 100), int(imagen.height * Porcentaje / 100)))
    print("""\033[1mTAMAÑO DE LA IMAGEN CAMBIADO!!!\033[0m
          """)
    return nueva_imagen

def convertir_a_grises(imagen):
    nueva_imagen = ImageOps.grayscale(imagen)
    print("""\033[1mIMAGEN CONVERTIDA A ESCALA DE GRISES!!!\033[0m
          """)
    return nueva_imagen

def rotar_imagen(imagen):
    angulo = -90
    nueva_imagen = imagen.rotate(angulo, expand=True)
    print("""\033[1mIMAGEN ROTADA. \033[0m
          """)
    return nueva_imagen

def aplicar_filtro(imagen):
    print("""SELECCIONAR UN FILTRO: 
    1. Desenfocar
    2. Enfocar""")
    
    filtro = input("Ingrese una opción: ")
    
    filtros = {
        "1": ImageFilter.BLUR,
        "2": ImageFilter.SHARPEN
    }
    
    if filtro in filtros:
        nueva_imagen = imagen.filter(filtros[filtro])
        print("""\033[1mFILTRO APLICADO.\033[0m
              """)
        return nueva_imagen
    else:
        print("""\033[1mOPCIÓN DE FILTRO NO VALIDA.\033[0m
              """)
        return imagen

def mostrar_menu():
    print("MENÚ DE OPCIONES: ")
    print("1. Cambiar tamaño de la imagen")
    print("2. Convertir imagen a escala de grises")
    print("3. Rotar imagen")
    print("4. Aplicar filtro")
    print("5. Mostrar cambios")
    print("6. Guardar cambios")
    print("""7. Salir
          """)

def main():
    imagen = cargar_imagen()
    if imagen is None:
        print("")
        return
    
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        if opcion == "1":
            imagen = cambiar_tamano(imagen)
        elif opcion == "2":
            imagen = convertir_a_grises(imagen)
        elif opcion == "3":
            imagen = rotar_imagen(imagen)
        elif opcion == "4":
            imagen = aplicar_filtro(imagen)
        elif opcion == "5":
            imagen.show()
        elif opcion == "6":
            nuevo_nombre = str(input("Ingrese un nombre: "))
            extencion = str(input("Ingrese una extencion (JPG, PNG, GIF): "))
            print("""\033[1mCAMBIOS GUARDADOS!!!.\033[0m
                  """)
            imagen.save(f"{nuevo_nombre}.{extencion}")
        elif opcion == "7":
            print("""\033[1mSALIENDO DEL PROGRAMA. CHAU!
                  \033[0m
                  """)
            break
        else:
            print("""\033[1mOPCIÓN NO VALIDA. INTENTE DE NUEVO. \033[0m
                  """)

        
if __name__ == "__main__":
    main()
