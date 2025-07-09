from factura_parser.base_parser import BaseParser
import re

class ParserAAA(BaseParser):
    def parse(self, text: str) -> dict:
        empresa = "AAA"
        tipo_servicio = "acueducto"

        consumo_match = re.search(r"CONSUMO DEL MES:\s*(\d+)", text)
        tarifa_match = re.search(r"TOTAL ACUEDUCTO.*?\$([\d,.]+)", text)
        total_match = re.search(r"TOTAL\s+\$([\d,.]+)", text)

        consumo = int(consumo_match.group(1)) if consumo_match else 0
        tarifa = float(tarifa_match.group(1).replace('.', '').replace(',', '.')) / consumo if consumo else 0
        total = float(total_match.group(1).replace('.', '').replace(',', '.')) if total_match else 0

        return {
            "empresa": empresa,
            "tipo_servicio": tipo_servicio,
            "consumo": consumo,
            "tarifa": round(tarifa, 2),
            "total": round(total, 2)
        }