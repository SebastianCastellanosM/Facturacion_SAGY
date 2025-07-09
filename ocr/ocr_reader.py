def extraer_texto(path):
    import fitz
    from pdf2image import convert_from_path
    from pytesseract import image_to_string
    from PIL import Image
    import os

    ext = os.path.splitext(path)[1].lower()

    # Si es imagen
    if ext in ['.png', '.jpg', '.jpeg']:
        img = Image.open(path)
        return image_to_string(img, lang='eng')  # o 'spa' si disponible

    # Si es PDF
    elif ext == '.pdf':
        doc = fitz.open(path)
        texto = ""
        for page in doc:
            page_text = page.get_text().strip()
            if page_text:
                texto += page_text + "\n"
            else:
                # Página sin texto, extraer imagen y aplicar OCR
                images = convert_from_path(path, dpi=300)
                for img in images:
                    texto += image_to_string(img, lang='eng') + "\n"
                break
        return texto
