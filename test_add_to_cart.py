from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

if cart.text == "1":
    print("Add To Cart Passed")
else:
    print("Add To Cart Failed")

time.sleep(2)
driver.quit()