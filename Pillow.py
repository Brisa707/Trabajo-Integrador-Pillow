from PIL import Image, ImageFilter
from Menu import mostrar_menu
from Agrandado import cambiar_tamano
from Gris import convertir_a_grises
from Rotar import rotar_imagen
#Yo usé la imagen C:\Repo-git\unab.jpg

def cargar_imagen():
    ruta = input("Ingresa la ruta de la imagen: ")
    try:
        imagen = Image.open(ruta)
        print("Imagen cargada exitosamente.")
        return imagen
    except Exception as e:
        print(f"ERROR AL CARGAR LA IMAGEN: {e}")
        return None

cambiar_tamano

convertir_a_grises


rotar_imagen

def aplicar_filtro(imagen):
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

mostrar_menu

def main():
    imagen = cargar_imagen()
    if imagen is None:
        print("ERROR AL CARGAR LA IMAGEN.")
        return
    
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        if opcion == "1":
            imagen = cambiar_tamano(imagen)
            imagen.show()
        elif opcion == "2":
            imagen = convertir_a_grises(imagen)
            imagen.show()
        elif opcion == "3":
            imagen = rotar_imagen(imagen)
            imagen.show()
        elif opcion == "4":
            imagen = aplicar_filtro(imagen)
            imagen.show()
        elif opcion == "5":
            nuevo_nombre = str(input(f"Ingrese un nombre: "))
            print("Guardando cambios.")
            imagen.save(f"{nuevo_nombre}.jpg")
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("OPCIÓN NO VALIDA. INTENTE DE NUEVO.")

        
if __name__ == "__main__":
    main()
