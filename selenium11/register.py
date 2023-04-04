from selenium import webdriver
from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def registration_button1(self):
        """This function returns the element of the 'registration' button from the order payment page"""
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def username(self, user):
        """This function returns the act of sending the
        inserted 'user' to the username field in the registration page"""
        return self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(user)

    def email(self, email):
        """This function returns the act of sending the
        inserted 'email' to the email field in the registration page"""
        return self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(email)

    def password_and_confirmation(self, password):
        """This function returns the act of sending the inserted 'password'
        to the password and confirmed password field in the registration page"""
        return self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(password), \
            self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(password)

    def agree_to_terms(self):
        """This function returns the element of the 'agree to term's' check box in the registration page"""
        return self.driver.find_element(By.NAME, "i_agree")

    def next_button(self):
        """This function returns the element of the
        'NEXT' button from the registration process"""
        return self.driver.find_element(By.ID, "next_btn")

    def registration_button2(self):
        """This function returns the element of the 'REGISTER' button from the registration page"""
        return self.driver.find_element(By.ID, "register_btnundefined")