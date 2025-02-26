#INFO PHONE/ADDRESS

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Hyperlinks Lists/HYPERLINKS_SPECIALTY COFFE_Houston, TX_04 25 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 2].tolist()

# Lista para guardar los resultados
phones = []

# Función para obtener todos los elementos con clase `profileResponse`
def get_all_profile_responses(url):
    try:
        driver.get(url)

        # Clic en el enlace de contacto
        link = driver.find_element(By.LINK_TEXT, "Contact")
        link.click()

        # Esperar a que los elementos con clase `profileResponse` estén presentes
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "profileResponse"))
        )

        # Obtener todos los elementos con clase `profileResponse`
        profile_responses = driver.find_elements(By.CLASS_NAME, "profileResponse")

        # Extraer el texto de cada elemento y devolverlo como lista
        return [element.text.strip() for element in profile_responses]

    except NoSuchElementException:
        print(f"No se encontró el enlace 'Contact' o los elementos con clase 'profileResponse' en {url}")
        return ["No Data"]

    except Exception as e:
        print(f"Error en la URL {url}: {e}")
        return ["Error"]

# Iterar por cada URL y extraer los datos
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    responses = get_all_profile_responses(url)
    phones.append(responses)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Phone'] = phones

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO_SPECIALTY COFFE_Houston, TX_04 25 2025.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")

#=============================================================================
# webpage

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Hyperlinks Lists/HYPERLINKS_SPECIALTY COFFE_Houston, TX_04 25 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 2].tolist()

# XPath para extraer el enlace de la página web
webpage_xpath = "//a[contains(@title, 'http')]"

# Lista para guardar los resultados
webpages = []

# Función para obtener la página web de la página
def get_webpage(url, xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el atributo href
        address_element = driver.find_element(By.XPATH, xpath)
        webpage = address_element.get_attribute('href')
    except Exception as e:
        webpage = f"Error: {str(e)}"
    
    return webpage

# Iterar por cada URL y extraer el webpage
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    webpage = get_webpage(url, webpage_xpath)
    webpages.append(webpage)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Webpage'] = webpages

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/WEBPAGES_SPECIALTY COFFE_Houston, TX_04 25 2025.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")
