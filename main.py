import os
import shutil
from ocr.ocr_reader import extraer_texto
from factura_parser.factory import detectar_plantilla
from db.azure_connector import guardar_factura
from utils.validator import validar_factura

def main():
    carpeta = "facturas"
    procesados_dir = "procesados"
    os.makedirs(procesados_dir, exist_ok=True)

    for archivo in os.listdir(carpeta):
        if not archivo.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
            continue

        path = os.path.join(carpeta, archivo)
        print(f"📄 Procesando {archivo}...")
        try:
            texto = extraer_texto(path)
            parser = detectar_plantilla(texto)
            datos = parser.parse(texto)

            if validar_factura(datos["consumo"], datos["tarifa"], datos["total"]):
                guardar_factura(datos)
                print(f"Factura válida y guardada: {datos}")
                shutil.move(path, os.path.join(procesados_dir, archivo))
            else:
                print(f"Validación fallida: {datos}")

        except Exception as e:
            with open("errores.log", "a", encoding="utf-8") as log:
                log.write(f"{archivo} → {str(e)}\n")
            print(f"Error procesando {archivo}: {e}")

if __name__ == "__main__":
    main()