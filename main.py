from image_operations import apply_filters, resize_image, crop_image, convert_to_grayscale
from utils import load_image, save_image

def main():
    image_path = 'input.jpg'
    output_path = 'output.jpg'
    
    # Cargar imagen
    image = load_image(image_path)
    
    # Aplicar filtros
    filtered_image = apply_filters(image)
    
    # Redimensionar imagen
    resized_image = resize_image(filtered_image, (800, 600))
    
    # Recortar imagen
    cropped_image = crop_image(resized_image, (100, 100, 700, 500))
    
    # Convertir a escala de grises
    grayscale_image = convert_to_grayscale(cropped_image)
    
    # Guardar imagen resultante
    save_image(grayscale_image, output_path)
    print("Imagen procesada y guardada en", output_path)

if __name__ == "__main__":
    main()
