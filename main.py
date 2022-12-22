import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

load_dotenv('variables.env')
WEBSITE = os.getenv('URL')
PATH = os.getenv('DRIVER_PATH')
if __name__ == '__main__':
    # Orden de prioridades en búsqueda de elementos
    # 1. Id
    # 2. Class name, tag name, css selector
    # 3. XPath

    # C:\Github\web-scraping-for-informatica\venv\Scripts\chromedriver.exe
    service = service.Service(executable_path=PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(WEBSITE)  # Agregar "waits" para saber si la página terminó de cargar

    element = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
    element.click()

    element2 = Select(driver.find_element(By.ID, 'country'))
    element2.select_by_visible_text('Argentina')

    elements3 = driver.find_elements(By.TAG_NAME, 'tr')
    for match in elements3:
        print(match.text)
