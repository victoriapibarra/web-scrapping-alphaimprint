#BOOTH

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_Natural Products Expo West_03 04 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 1].tolist()

# XPath para extraer el nombre de contacto
booth_xpath = '//span[contains(@class, "sc-c3d23e77-0 gAgliq") and text()]'
address_xpath = '//a [contains(@target, "sc-efce57e-4 fEPJTD") and text()]'
webpage_xpath = ''

# Lista para guardar los resultados
booths = []
addresses = []
webpages = []

# Función para obtener el nombre de contacto de la página
def get_info(url, booth_xpath, address_xpath, webpage_xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, booth_xpath, address_xpath, webpage_xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el texto
        booth_element = driver.find_element(By.XPATH, booth_xpath)
        booth = booth_element.text.strip()
        
        address_element = driver.find_element(By.XPATH, address_xpath)
        address = address_element.text.strip()
        
        webpage_element = driver.find_element(By.XPATH, webpage_xpath)
        webpage = webpage_element.text.strip()
        
        # Si no encuentra el texto, devuelve "No Contact"
        if not booth:
            booth = "No Booth"
        
        if not address:
            address = "No Address"
        
        if not webpage:
            webpage = "No Webpage"
        
    
    except NoSuchElementException:
        booth = address = webpage = "No Data"  # Si no encuentra el elemento
    
    except Exception as e:
        booth = address = webpage = "Error"  # Si ocurre algún otro error
    
    return booth, address, webpage

# Iterar por cada URL y extraer el nombre del booth
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    booth, address, webpage = get_info(url, booth_xpath, address_xpath, webpage_xpath)
    booths.append(booth)
    addresses.append(address)
    webpages.append(webpage)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Booth'] = booths
df['Address'] = addresses
df['Webpage'] = webpages

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_Natural Products Expo West_03 04 2025_All Info.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")