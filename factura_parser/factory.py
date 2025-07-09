# Detecta la plantilla basada en el texto OCR

def detectar_plantilla(text):
    text = text.upper()

    if "CELSIA" in text:
        from .parser_celsia import ParserCelsia
        return ParserCelsia()
    elif "EPM" in text:
        from .parser_epm import ParserEPM
        return ParserEPM()
    elif "TRIPLE A DE B/Q" in text or "AAA" in text:
        from .parser_aaa import ParserAAA
        return ParserAAA()
    elif "ENEL" in text:
        from .parser_enel import ParserEnel
        return ParserEnel()
    elif "BIA ENERGY" in text or "BIASOLAR" in text:
        from .parser_bia import ParserBia
        return ParserBia()
    elif "GASCARIBE" in text:
        from .parser_gascaribe import ParserGascaribe
        return ParserGascaribe()
    elif "AIR-E" in text or "AIRE" in text:
        from .parser_aire import ParserAIRE
        return ParserAIRE()
    else:
        raise ValueError("No se pudo identificar la empresa en el texto de la factura.")
