from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def username_checkout(self, user):
        """This function returns the act of inserting the username
        from the inserted value in the checkout login area"""
        return self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(user)

    def password_checkout(self, password):
        """This function returns the act of inserting the password
                from the inserted value in the checkout login area"""
        return self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def login_button_checkout(self):
        """This function returns the element of the login button in the checkout area"""
        return self.driver.find_element(By.ID, "login_btnundefined")

    def username_floating_window(self, user):
        """This function returns the act of inserting the username
        from the inserted value in the login floating window"""
        return self.driver.find_element(By.NAME, "username").send_keys(user)

    def password_floating_window(self, password):
        """This function returns the act of inserting the password
        from the inserted value in the login floating window"""
        return self.driver.find_element(By.NAME, "password").send_keys(password)

    def signin_floating_window(self):
        """This function returns the element of the 'SIGNIN' button in the login floating page"""
        return self.driver.find_element(By.ID, "sign_in_btnundefined")