from factura_parser.base_parser import BaseParser
import re

class ParserBIA(BaseParser):
    def parse(self, text: str) -> dict:
        empresa = "BIA"
        tipo_servicio = "energía"

        consumo_match = re.search(r"Energía activa \(([\d.,]+)\s*kWh", text)
        tarifa_match = re.search(r"x Cu \$([\d.,]+)\)", text)
        total_match = re.search(r"Total a pagar.*?\$([\d.,]+)", text)

        consumo = float(consumo_match.group(1).replace('.', '').replace(',', '.')) if consumo_match else 0
        tarifa = float(tarifa_match.group(1).replace('.', '').replace(',', '.')) if tarifa_match else 0
        total = float(total_match.group(1).replace('.', '').replace(',', '.')) if total_match else 0

        return {
            "empresa": empresa,
            "tipo_servicio": tipo_servicio,
            "consumo": consumo,
            "tarifa": round(tarifa, 2),
            "total": round(total, 2)
        }