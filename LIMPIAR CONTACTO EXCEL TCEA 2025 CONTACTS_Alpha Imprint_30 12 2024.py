import pandas as pd
import re

# Función para extraer correos electrónicos
def extraer_correos(texto):
    if isinstance(texto, str):
        return ', '.join(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto))
    return ''

# Función para extraer números de teléfono
def extraer_telefonos(texto):
    if isinstance(texto, str):
        return ', '.join(re.findall(r'\b\d{2,4}[-.\s]??\d{2,4}[-.\s]??\d{3,4}\b', texto))
    return ''

# Ruta del archivo
archivo = '/Users/victoriaperez/Documents/Alpha Imprint/empresas_con_contacto.xlsx'

# Cargar archivo Excel
df = pd.read_excel(archivo)

# Verificar los nombres de las columnas
print("Nombres de las columnas:", df.columns)

# Ajustar el nombre de la columna 'Contacto'
columna_contacto = 'Contacto'  # Ahora usa 'Contacto' con la C mayúscula

if columna_contacto in df.columns:
    # Extraer correos y teléfonos
    df['Correos'] = df[columna_contacto].apply(extraer_correos)
    df['Teléfonos'] = df[columna_contacto].apply(extraer_telefonos)

    # Guardar el resultado en un nuevo archivo
    archivo_salida = '/Users/victoriaperez/Documents/Alpha Imprint/empresas_contacto_resultado.xlsx'
    df.to_excel(archivo_salida, index=False)
    print(f"Extracción completada. Archivo guardado como: {archivo_salida}")
else:
    print(f"La columna '{columna_contacto}' no existe en el archivo. Verifica los nombres de las columnas.")
