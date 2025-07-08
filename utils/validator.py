def validar_factura(consumo, tarifa, total):
    esperado = round(consumo * tarifa, 2)
    return abs(esperado - total) < 5.0
