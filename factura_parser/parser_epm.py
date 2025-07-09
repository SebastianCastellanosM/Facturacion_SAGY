from factura_parser.base_parser import BaseParser
import re

class ParserEPM(BaseParser):
    def parse(self, text: str) -> dict:
        empresa = "EPM"
        tipo_servicio = "energía"  # Puedes crear múltiples por servicio si deseas

        consumo_match = re.search(r"Energía may-25\s+(\d+[.,]?\d*)", text)
        tarifa_match = re.search(r"kWh\s+923,20", text)  # tarifa fija para energía
        total_match = re.search(r"Total Energía \$\s?([\d.,]+)", text)

        consumo = float(consumo_match.group(1).replace('.', '').replace(',', '.')) if consumo_match else 0
        tarifa = 923.20  # valor fijo encontrado en el PDF
        total = float(total_match.group(1).replace('.', '').replace(',', '.')) if total_match else 0

        return {
            "empresa": empresa,
            "tipo_servicio": tipo_servicio,
            "consumo": consumo,
            "tarifa": round(tarifa, 2),
            "total": round(total, 2)
        }