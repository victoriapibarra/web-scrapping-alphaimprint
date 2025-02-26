import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configura Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Carga la página principal
url = "https://register.tcea.org/2025/exhibitor_exhibitor_list25.cfm"
driver.get(url)

# Encuentra los elementos que contienen los nombres de los expositores y sus links
elements = driver.find_elements(By.XPATH, "//a[contains(@onclick, 'ExhibitorPopup')]")
nombres = [el.text for el in elements if el.text.strip()]  # Evita nombres vacíos

# Extrae el valor del onclick, que contiene la URL relativa
relative_links = [el.get_attribute("onclick").split("'")[1] for el in elements]
base_url = "https://register.tcea.org/2025/"  # La URL base para concatenar

# Concatenamos la URL base con la URL relativa obtenida
links = [base_url + link for link in relative_links]

# Encuentra los elementos que contienen los números de los booths
booths_elements = driver.find_elements(By.XPATH, "//td[@class='tb-text-center']")
booths = [booth.text.strip() for booth in booths_elements]

# Asegúrate de que los nombres, booths y links estén alineados
data = [{"Nombre": name, "Booth": booth, "Link": link} for name, booth, link in zip(nombres, booths, links)]

# Función para obtener la dirección y el sitio web desde el sublink
def obtener_info_exhibitor(link):
    driver.get(link)  # Accede al sublink del expositor
    time.sleep(2)  # Espera para asegurar que la página cargue correctamente
    try:
        # Obtener la dirección usando el nuevo XPath
        address_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table[2]/tbody/tr[1]/td[1]")
        address = address_element.text.strip() if address_element else "Dirección no encontrada"
        
        # Obtener el enlace del sitio web
        website_element = driver.find_element(By.XPATH, "//a[contains(@href, 'http')]")
        website = website_element.get_attribute("href") if website_element else "Sitio web no encontrado"
    except Exception as e:
        address = "Dirección no encontrada"
        website = "Sitio web no encontrado"
        print(f"Error al obtener información para {link}: {e}")
    
    return address, website

# Crear una lista para almacenar los datos completos
excel_data = []

# Recorrer los datos y obtener la información adicional
for entry in data:
    nombre = entry["Nombre"]
    booth = entry["Booth"]
    link = entry["Link"]
    
    # Obtener la dirección y el sitio web de cada expositor
    address, website = obtener_info_exhibitor(link)
    
    # Añadir la información a la lista
    excel_data.append({
        "Nombre": nombre,
        "Booth": booth,
        "Dirección": address,
        "Website": website
    })

# Convertir la lista en un DataFrame
df = pd.DataFrame(excel_data)

# Guardar el DataFrame en un archivo Excel
df.to_excel("expositores_info.xlsx", index=False)

print("Información guardada en el archivo 'expositores_info.xlsx'")

# Cierra el navegador
driver.quit()