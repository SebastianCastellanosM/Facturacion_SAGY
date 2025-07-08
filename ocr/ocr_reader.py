from pdf2image import convert_from_path
from pytesseract import image_to_string

def extraer_texto(path):
    pages = convert_from_path(path)
    return ' '.join([image_to_string(p, lang='spa') for p in pages])
