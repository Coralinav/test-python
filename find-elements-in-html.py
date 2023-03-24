from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

h2 = driver.find_element(By.CSS_SELECTOR "//h1[contains(text(),'Resources')]")
p = driver.find_element(By.CSS_SELECTOR, "//p[contains(text(),'JSONPlaceholder comes with a set of 6 common resources:')]")

driver.quit()

