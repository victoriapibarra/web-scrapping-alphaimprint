import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Lista ampliada de palabras clave en español, inglés y abreviaciones
palabras_clave = [
    # Español
    "Tel", "Teléfono", "Contacto", "Correo", "Email", "Móvil", "Celular", "WhatsApp", "Llámame", 
    "Llámanos", "Comunícate", "Info", "Información", "Atención", "Servicio", "Oficina", "Soporte",
    "Asistencia", "Línea", "Contacto directo", "Contáctanos", "Redes sociales",
    
    # Inglés
    "Phone", "Telephone", "Contact", "Email", "Mail", "Mobile", "Cell", "WhatsApp", "Call us", 
    "Call me", "Reach out", "Support", "Info", "Information", "Customer service", "Help", 
    "Assistance", "Hotline", "Direct line", "Social media",
    
    # Abreviaciones y símbolos
    "Tel.", "Tlf.", "Ph.", "Mob.", "Cell.", "@", "☎", "📧", "✉", "📞", "📱", "📟"
]

# Cargar datos desde el archivo Excel
ruta_excel = "/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO_Southwest Fuel & Convenience_Jun 01 2025.xlsx"  # Ruta y nombre correcto del archivo
df = pd.read_excel(ruta_excel)

# Configura Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Función para buscar contacto en Google
def buscar_contacto(empresa):
    # Accede a Google
    driver.get("https://www.google.com")
    time.sleep(2)
    
    # Busca la empresa en Google
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(empresa + " contact")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # Inicializa el contacto como "No encontrado"
    contacto = "No encontrado"
    
    # Recorre todos los posibles elementos que contengan las palabras clave
    try:
        elementos = driver.find_elements(By.XPATH, "//*[contains(text(), '')]")
        for elemento in elementos:
            texto = elemento.text.lower()
            if any(palabra.lower() in texto for palabra in palabras_clave):
                contacto = texto.strip()
                break
    except Exception as e:
        print(f"Error al buscar contacto para {empresa}: {e}")
    
    return contacto

# Lista para almacenar los resultados
resultados_contacto = []

# Recorrer las empresas en el archivo Excel y buscar su contacto
for empresa in df['Nombre']:  # Asegúrate de que la columna se llama 'Nombre' en tu Excel
    contacto = buscar_contacto(empresa)
    resultados_contacto.append(contacto)
    print(f"Contacto de {empresa}: {contacto}")

# Guardar los resultados en un nuevo archivo Excel
df['Contacto'] = resultados_contacto
df.to_excel("/Users/victoriaperez/Documents/Alpha Imprint/empresas_con_contacto.xlsx", index=False)

# Cierra el navegador
driver.quit()
