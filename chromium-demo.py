from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome("./chromedriver")

default_url = "chrome://dino/"
try:
    driver.get(default_url)
except:
    # 因為 chrome:// 一定會炸掉，用 try 繞過
    pass

try:
    actions = ActionChains(driver)

    # 等待小恐龍載入
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )

    for i in range(10):
        actions.send_keys(Keys.SPACE)
        actions.perform()
        sleep(1)

    actions.send_keys(Keys.DOWN)
    actions.perform()
    sleep(10)

finally:
    driver.quit()