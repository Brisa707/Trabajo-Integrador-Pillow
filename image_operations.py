from PIL import Image, ImageFilter

def apply_filters(image):
    return image.filter(ImageFilter.BLUR).filter(ImageFilter.CONTOUR)

def resize_image(image, size):
    return image.resize(size)

def crop_image(image, box):
    return image.crop(box)

def convert_to_grayscale(image):
    return image.convert("L")
