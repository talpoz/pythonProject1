from selenium import webdriver
from selenium.webdriver.common.by import By


class AOSCategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def product_id(self, Id):
        """This function returns the element of the product by the inserted id"""
        return self.driver.find_element(By.ID, Id)

    def category_title(self):
        """This function returns the text of the category title on the top of the page"""
        return self.driver.find_element(By.CSS_SELECTOR, ".categoryTitle").text


