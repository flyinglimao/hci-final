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
    
    input = 0 # 0 無 1 小跳 2 大跳 3 蹲
    while 1:
        sleep(1/1000) # 避免 CPU Busy Waiting
        if input == 0:
            print("Release")
            actions.key_up(Keys.SPACE)
            actions.key_up(Keys.DOWN)
            actions.perform()
        elif input == 1:
            print("S Jump")
            actions.key_down(Keys.SPACE)
            actions.perform()
            sleep(50/1000)
            actions.key_up(Keys.SPACE)
            actions.perform()
        elif input == 2:
            print("L Jump")
            actions.key_down(Keys.SPACE)
            actions.perform()
            sleep(200/1000)
            actions.key_up(Keys.SPACE)
            actions.perform()
        elif input == 3:
            print("Down")
            actions.key_down(Keys.DOWN)
            actions.perform()

finally:
    driver.quit()