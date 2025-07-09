from factura_parser.base_parser import BaseParser
import re

class ParserGascaribe(BaseParser):
    def parse(self, text: str) -> dict:
        empresa = "GASCARIBE"
        tipo_servicio = "gas"

        consumo_match = re.search(r"EQUIVALEN A.*?(\d+[.,]?\d*)Kwh", text)
        total_match = re.search(r"\$\s?([\d.,]+)", text)

        consumo = float(consumo_match.group(1).replace('.', '').replace(',', '.')) if consumo_match else 0
        tarifa = 289.78  # aproximación por m3 a kWh
        total = float(total_match.group(1).replace('.', '').replace(',', '.')) if total_match else 0

        return {
            "empresa": empresa,
            "tipo_servicio": tipo_servicio,
            "consumo": consumo,
            "tarifa": round(tarifa, 2),
            "total": round(total, 2)
        }