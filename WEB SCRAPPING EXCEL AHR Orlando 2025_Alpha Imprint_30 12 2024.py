# ADDRESS
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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_AHR Orlando_10 02 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 2].tolist()

# Tu XPath para extraer el address
address_xpath = '//p[contains(@class, "showcase-address tc")]'

# Lista para guardar los resultados
addresses = []

# Función para obtener el address de la página
def get_address(url, xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el texto
        address_element = driver.find_element(By.XPATH, xpath)
        address = address_element.text
    except Exception as e:
        address = f"Error: {str(e)}"
    
    return address

# Iterar por cada URL y extraer el address
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    address = get_address(url, address_xpath)
    addresses.append(address)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Address'] = addresses

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO_LIST_AHR_Orlando_Updated.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")


# ==============================================================================================================
# WEBPAGE

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_AHR Orlando_10 02 2025.xlsx'
df = pd.read_excel(file_path)

# Limitar a las primeras 5 filas
urls = df.iloc[:5, 2].tolist()

# XPath para extraer el enlace de la página web
webpage_xpath = '//ul[contains(@class, "showcase-web-phone")]//a[contains(@title, "Visit our website")]'

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

# Imprimir los resultados en la consola
for i, webpage in enumerate(webpages):
    print(f"Webpage {i+1}: {webpage}")

# Cierra el navegador después de obtener los datos
driver.quit()

print("Extracción completa.")


# =====================================================================================
#TELÉFONO 

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_AHR Orlando_10 02 2025.xlsx'
df = pd.read_excel(file_path)

# Limitar a las primeras 5 filas
urls = df.iloc[:5, 2].tolist()

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

# Imprimir los resultados en la consola
for i, phone in enumerate(phones):
    print(f"Phone {i+1}: {phone}")

# Cierra el navegador después de obtener los datos
driver.quit()

print("Extracción completa.")


# =====================================================================================
#NOMBRE CONTACTO 

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_AHR Orlando_10 02 2025.xlsx'
df = pd.read_excel(file_path)

# Limitar a las primeras 5 filas
urls = df.iloc[:5, 2].tolist()

# XPath para extraer el nombre de contacto
contact_name_xpath = '//div[contains(@class, "tc mb0")]//h3[contains(@class, "dib f2 ma0 mb1")]'

# Lista para guardar los resultados
contact_names = []

# Función para obtener el nombre de contacto de la página
def get_contact_name(url, xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el texto
        contact_name_element = driver.find_element(By.XPATH, xpath)
        contact_name = contact_name_element.text.strip()
        
        # Si no encuentra el texto, devuelve "No Contact"
        if not contact_name:
            contact_name = "No Contact"
    
    except NoSuchElementException:
        contact_name = "No Contact"  # Si no encuentra el elemento
    
    except Exception as e:
        contact_name = "No Contact"  # Si ocurre algún otro error
    
    return contact_name

# Iterar por cada URL y extraer el nombre de contacto
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    contact_name = get_contact_name(url, contact_name_xpath)
    contact_names.append(contact_name)

# Imprimir los resultados en la consola
for i, contact_name in enumerate(contact_names):
    print(f"Contact_Name {i+1}: {contact_name}")

# Cierra el navegador después de obtener los datos
driver.quit()

print("Extracción completa.")


# =====================================================================================
#PUESTO NOMBRE CONTACTO 

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
file_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO LIST_AHR Orlando_10 02 2025.xlsx'
df = pd.read_excel(file_path)

# Asume que los enlaces están en la columna C (índice 2)
urls = df.iloc[:, 2].tolist()

# XPath para extraer el nombre de contacto
contact_title_xpath = '//P[contains(@class, "f3 lh-title muted tc")]'

# Lista para guardar los resultados
contact_titles = []

# Función para obtener el nombre de contacto de la página
def get_contact_title(url, xpath):
    try:
        # Navega a la página
        driver.get(url)
        
        # Espera hasta que el elemento esté presente (máximo 10 segundos)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Busca el elemento usando el XPath y extrae el texto
        contact_title_element = driver.find_element(By.XPATH, xpath)
        contact_title = contact_title_element.text.strip()
        
        # Si no encuentra el texto, devuelve "No Contact"
        if not contact_title:
            contact_title = "No Contact Info"
    
    except NoSuchElementException:
        contact_title = "No Contact Info"  # Si no encuentra el elemento
    
    except Exception as e:
        contact_title = "No Contact Info"  # Si ocurre algún otro error
    
    return contact_title

# Iterar por cada URL y extraer el nombre de contacto
for i, url in enumerate(urls):
    print(f"Procesando URL {i+1}/{len(urls)}: {url}")
    contact_title = get_contact_title(url, contact_title_xpath)
    contact_titles.append(contact_title)

# Agregar los resultados a una nueva columna D en el DataFrame
df['Contact_Title'] = contact_titles

# Guardar el DataFrame actualizado en un nuevo archivo Excel
output_path = '/Users/victoriaperez/Documents/Alpha Imprint/Lists/Expo Lists/EXPO_LIST_AHR_Orlando_Contact_Title.xlsx'
df.to_excel(output_path, index=False)

# Cierra el navegador después de obtener los datos
driver.quit()

print(f"Extracción completa. Los resultados han sido guardados en '{output_path}'.")