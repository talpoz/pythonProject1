from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AOSProductPage:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def product_name(self):
        """This function returns the text of the product name"""
        product1 = self.driver.find_element(By.XPATH, "//*[@id='Description']/h1")
        product = str(product1.text)
        return product

    def product_price(self):
        """This function returns the price (number) of the product"""
        e_price = self.driver.find_element(By.XPATH, "//div[@id='Description']"
                                                     "/h2[@class='roboto-thin screen768 ng-binding']")
        e_price = e_price.text.replace("$", "").replace(",", "")
        price = float(e_price)
        return price

    def add_to_cart(self):
        """This function returns the element of the 'Add To Cart' button"""
        return self.driver.find_element(By.NAME, "save_to_cart")

    def product_color(self, title):
        """This function returns the element of the color by the inserted color title"""
        title = title.upper()
        return self.driver.find_element(By.CSS_SELECTOR, f"[title='{title}']")

    def quantity_amount(self, amount: int):
        """This function returns the insert act of the wanted quantity from the inserted wanted amount"""
        wanted_quantity = self.driver.find_element(By.NAME, "quantity")
        action_chains = ActionChains(self.driver)
        return action_chains.move_to_element(wanted_quantity).click().send_keys(str(amount)).perform()