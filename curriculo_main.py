import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Edge()
driver.get("https://www.clouddog.com.br/trabalhe-conosco/")
time.sleep(3)
search_box=Select(driver.find_element(By.XPATH,'//*[@id="cargo"]'))
search_box.select_by_visible_text('Estágio Comercial Tech')
search_box=driver.find_element(By.XPATH,'//*[@id="nome"]')
search_box.send_keys("João Emmanuel Ferreira Cabral")
search_box=driver.find_element(By.XPATH,'//*[@id="email"]')
search_box.send_keys('joaoefcabral@gmail.com')
search_box=driver.find_element(By.XPATH,'//*[@id="projeto"]')
search_box.send_keys('https://github.com/JEFC55/Curriculo/blob/main/curriculo_main.py')

time.sleep(5)
