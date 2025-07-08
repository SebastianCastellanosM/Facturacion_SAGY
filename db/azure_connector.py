# Conexión con Azure SQL
import pyodbc
from config import DB_CONFIG

def guardar_factura(data):
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};UID={DB_CONFIG['username']};PWD={DB_CONFIG['password']};Encrypt=yes;"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Facturas (empresa, tipo_servicio, consumo, tarifa, total)
        VALUES (?, ?, ?, ?, ?)''',
        (data['empresa'], data['tipo_servicio'], data['consumo'], data['tarifa'], data['total'])
    )
    conn.commit()
    cursor.close()
    conn.close()
