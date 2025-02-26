import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Carga la página principal
url = "https://ahr25.mapyourshow.com/8_0/#/"
driver.get(url)

#Dame el nombre (título) de la página que estás abriendo
print(driver.title)

#Encuentra el searchbox por su ID, puede ser, ID o NAME porque CLASS es muy general
search = driver.find_element(by=By.ID, value="search-main") 

#Busca esa empresa en el searchbox
search.send_keys("Accurate Perforating")
search.send_keys(Keys.RETURN)

#click  a links
link = driver.find_element(by=By.LINK_TEXT, value="Exhibitor List")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "exhibitor"))
        )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "See All Results"))
        )
    element.click()
except:
    driver.quit()

    
# ==========================================================================================

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
opts.add_argument("--headless")  # Corrección aquí: 'add_argument' en lugar de 'add.argument'

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts  
)

driver.get('https://ahr25.mapyourshow.com/8_0/explore/exhibitor-alphalist.cfm?nav=1#/')

sleep(3)

# Modifica el XPath para seleccionar los títulos dentro de <h3> y extraer el texto del <a>
titulos = driver.find_elements(By.XPATH, '//h3[contains(@class, "card-Title")]/a')

for titulo in titulos:
    print(titulo.text)

# Cierra el navegador después de la ejecución
driver.quit()


#=====================================================================================================

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Carga la página principal
url = "https://ahr25.mapyourshow.com/8_0/#/"
driver.get(url)

# Click  a botones para llegar a lista de Expositors
link = driver.find_element(by=By.LINK_TEXT, value="Exhibitor List")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "exhibitor"))
        )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "See All Results"))
        )
    element.click()
except:
  

# Encuentra todos los expositores dentro de los cuadritos en la página de All Expositors
 expositors = driver.find_elements(by=By.XPATH, value='//li[contains(@class, "js-Card card br3 dib float pa3")]')

for expositor in expositors:
    print(expositor.find_element(by=By.XPATH, value='.//h3[contains(@class, "card-Title break-word f3 mb1 mt0")]').text)
    expositor.find_element(by=By.XPATH, value='.//a[contains(@title, "Visit this booth")]').text


# ===================================================================================================================

# Como hacer un XPATH
/p[contains(@class, "howcase-address tc"


