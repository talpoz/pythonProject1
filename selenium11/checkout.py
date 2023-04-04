from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Checkout:
    def __init__(self, driver: webdriver.Chrome):
        """This function creates the driver object"""
        self.driver = driver

    def safe_pay_username(self, user):
        """This function returns the act of sending the inserted 'user' to the username of the SafePay field"""
        return self.driver.find_element(By.NAME, "safepay_username").send_keys(user)

    def safe_pay_password(self, password):
        """This function returns the act of sending the inserted 'password' to the password of the SafePay field"""
        return self.driver.find_element(By.NAME, "safepay_password").send_keys(password)

    def pay_now_safepay(self):
        """This function returns the element of the 'PAY NOW' button"""
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def thanks_for_buying(self):
        """This function returns the element of the 'Thank you for buying with Advantage' text"""
        return self.driver.find_element(By.XPATH, "//div[@id='orderPaymentSuccess']/h2/span")

    def order_number(self):
        """This function returns the text of the order number from the 'Thank you for buying' page"""
        return self.driver.find_element(By.ID, "orderNumberLabel").text

    def credit_option(self):
        """This function returns the element of the 'Credit' option in the payment page"""
        credit_or_safepay = self.driver.find_elements(By.CSS_SELECTOR, "[type='radio']")
        credit = credit_or_safepay[1]
        return credit

    def credit_number(self, number):
        """This function returns the act of inserting the credit number from the inserted value"""
        return self.driver.find_element(By.ID, "creditCard").send_keys(number)

    def cvv_number(self, number):
        """This function returns the act of inserting the CVV number from the inserted value"""
        return self.driver.find_element(By.NAME, "cvv_number").send_keys(number)

    def cardholder_name(self, full_name):
        """This function returns the act of inserting the cardholder name from the inserted value"""
        return self.driver.find_element(By.NAME, "cardholder_name").send_keys(full_name)

    def pay_now_credit(self):
        """This function returns the act of clicking the pay now after entering the credit details"""
        pay = self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
        action_chains = ActionChains(self.driver)
        return action_chains.move_to_element(pay).click().perform()
