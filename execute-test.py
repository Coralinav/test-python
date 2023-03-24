from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create instances of Chrome and Firefox drivers
chrome_driver = webdriver.Chrome()
firefox_driver = webdriver.Firefox()

# Launch tests with Chrome and Firefox drivers
chrome_driver.get("https://www.google.com/")
firefox_driver.get("https://www.google.com/")

## Launch tests with Chrome and Firefox drivers
for driver in [chrome_driver, firefox_driver]:
    driver.get("https://www.google.com/")
    assert "Google" in driver.title

 # Find the search box and input the search query
    #Chrome
    search_box = chrome_driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium python")
    search_box.send_keys(Keys.RETURN)
    
    #Firefox
    search_box = firefox_driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium python")
    search_box.send_keys(Keys.RETURN)

# Close Chrome and Firefox drivers
chrome_driver.quit()
firefox_driver.quit()
