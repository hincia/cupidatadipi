from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.example.com 10).until(EC.element_to_be_clickable((By.XPATH, delete_btn)))
delete_button = driver.find_element(By.XPATH, delete_btn)
delete_button.click()
