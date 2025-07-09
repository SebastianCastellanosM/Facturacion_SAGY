from factura_parser.base_parser import BaseParser
import re

class ParserEnel(BaseParser):
    def parse(self, text: str) -> dict:
        empresa = "ENEL"
        tipo_servicio = "energía"

        consumo_match = re.search(r"(\d+)\s*kWh", text)
        tarifa_match = re.search(r"\$([\d.,]+)\s*kWh", text)
        total_match = re.search(r"TOTAL A PAGAR\s*\$([\d.,]+)", text)

        consumo = int(consumo_match.group(1)) if consumo_match else 0
        tarifa = float(tarifa_match.group(1).replace('.', '').replace(',', '.')) if tarifa_match else 0
        total = float(total_match.group(1).replace('.', '').replace(',', '.')) if total_match else 0

        return {
            "empresa": empresa,
            "tipo_servicio": tipo_servicio,
            "consumo": consumo,
            "tarifa": round(tarifa, 2),
            "total": round(total, 2)
        }
