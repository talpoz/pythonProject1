from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOSCart:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object and the wait object"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def cart_page_title(self):
        """This function returns the element of the title in the cart page"""
        return self.driver.find_element(By.XPATH, "//article/h3")

    def empy_message(self):
        """This function returns the text 'your cart is empty' from the cart page when the cart is empty"""
        return self.driver.find_element(By.XPATH, "//div/div/label[1][@class='roboto-bold ng-scope']").text

    def cart_page_title_path(self):
        """This function returns the text of the 'shopping cart'
        while in the shopping cart (from the navigation panel)"""
        return self.driver.find_element(By.CSS_SELECTOR, ".select").text

    def cart_page_total_price(self):
        """This function returns the number of the cart total price from the cart page"""
        e_price = self.driver.find_element(By.XPATH, "//td[@colspan='2']/span[2]")
        e_price = e_price.text.replace("$", "").replace(",", "")
        price = float(e_price)
        return price

    def cart_page_edit_button(self, num):
        """This function returns the element of the wanted 'EDIT' button in the cart
        page by the inserted number of the product you want to edit"""
        e_list = self.driver.find_elements(By.LINK_TEXT, "EDIT")
        return e_list[(num - 1)]

    def cart_page_quantities(self):
        """This function returns the number of the quantity of each product from the cart page"""
        e_q = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]/label[2]")
        quantities = []
        for element in e_q:
            element = int(element.text)
            quantities.append(element)
        return sum(quantities)

    def cart_icon_window_number(self):
        """This function returns the number of all the products in the cart from the cart floating window"""
        window = self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-regular ng-binding']")
        self.wait.until(EC.visibility_of(window))
        amount = window.text
        amount = amount.replace((amount[0]), "")
        amount = amount.replace((amount[-6:]), "")
        amount = int(amount)
        return amount

    def cart_window_quantities(self):
        """This function returns a list of numbers of the products quantities from the cart floating window"""
        e_qty = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        qty = []
        for element in e_qty:
            qty1 = element.text.replace(element.text[:4], "")
            qty1 = int(qty1)
            qty.append(qty1)
        return qty

    def cart_window_names(self):
        """This function returns the list of the products names from the cart floating window"""
        names = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/h3")
        p_names = []
        for element in names:
            p_names.append(element.text)
        return p_names

    def cart_window_colors(self):
        """This function returns the list of the products colors from the cart floating window"""
        e_colors = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[2]/span")
        colors = []
        for element in e_colors:
            colors.append(element.text)
        return colors

    def cart_window_prices(self):
        """This function returns the list of the products prices from the cart floating window"""
        e_prices = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/p")
        prices = []
        for element in e_prices:
            element = element.text.replace("$", "").replace(",", "")
            f_element = float(element)
            prices.append(f_element)
        return prices

    def cart_window_remove(self):
        """This function returns the element of the first 'x' button from the floating cart window"""
        return self.driver.find_element(By.XPATH, "//li/tool-tip-cart/div/table/tbody/tr[1]/td[3]/div/div[1]")

    def cart_window_checkout_button(self):
        """This function returns the element of the 'checkout' button from the floating cart window"""
        return self.driver.find_element(By.ID, "checkOutPopUp")

    def cart_window(self):
        """This function returns the element of the floating cart window"""
        return self.driver.find_element(By.ID, "toolTipCart")