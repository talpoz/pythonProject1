from selenium import webdriver
from selenium.webdriver.common.by import By


class AOSToolbar:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def aos_icon(self):
        """This function returns the element of the AOS logo on the left top corner of the page"""
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")

    def user_icon(self):
        """This function returns the element of the user icon in the toolbar"""
        return self.driver.find_element(By.ID, "menuUser")

    def user_name(self):
        """This function returns the element of the users name next to the user icon"""
        return self.driver.find_element(By.XPATH, "//a[@id='menuUserLink']/span")

    def user_sign_out(self):
        """This function returns the element of the 'sign out' option in the user menu"""
        return self.driver.find_element(By.XPATH, "//div[@id='loginMiniTitle']/label[3]")

    def my_orders(self):
        """This function returns the element of the 'my orders' option in the user menu"""
        return self.driver.find_element(By.XPATH, "//div[@id='loginMiniTitle']/label[2]")

    def my_orders_order_num(self):
        """This function returns the text of the order number in 'my orders' page"""
        return self.driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[1]/label").text

    def cart_icon(self):
        """This function returns the element of the cart icon in the toolbar"""
        return self.driver.find_element(By.ID, "menuCart")
