# WEBPAGES
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de opciones de Chrome
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
opts.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin interfaz)
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")

# Inicializa el WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# Cargar el archivo de Excel y leer los enlaces de la columna C
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_HIMSS_03 03 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 2].tolist()

# XPath para extraer el número de teléfono
phone_xpath = '//ul[contains(@class, "showcase-web-phone")]//li[contains(.//span, "Phone:")]'

# Lista para guardar los resultados
phones = []

# Función para obtener el número de teléfono de la página
def get_phone(url, xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el texto
        phone_element = driver.find_element(By.XPATH, xpath)
        phone = phone_element.text.strip()
    except Exception as e:
        phone = f"Error: {str(e)}"
    
    return phone

# Iterar por cada URL y extraer el número de teléfono
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    phone = get_phone(url, phone_xpath)
    phones.append(phone)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Phone'] = phones

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_HIMSS_03 03 2025_Phones.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")

