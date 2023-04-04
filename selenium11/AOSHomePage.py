from selenium import webdriver
from selenium.webdriver.common.by import By


class AOSHomePage:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def speakers(self):
        """This function returns the element of the speakers category"""
        return self.driver.find_element(By.ID, "speakersImg")

    def tablets(self):
        """This function returns the element of the tablets category"""
        return self.driver.find_element(By.ID, "tabletsImg")

    def laptops(self):
        """This function returns the element of the laptops category"""
        return self.driver.find_element(By.ID, "laptopsImg")

    def mice(self):
        """This function returns the element of the mice category"""
        return self.driver.find_element(By.ID, "miceImg")

    def headphones(self):
        """This function returns the element of the headphones category"""
        return self.driver.find_element(By.ID, "headphonesImg")