from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AOSToolbar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def aos_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")

    def user_icon(self):
        return self.driver.find_element(By.ID, "menuUser")

    def cart_icon(self):
        return self.driver.find_element(By.ID, "menuCart")