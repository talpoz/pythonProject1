from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from AOS_Toolbar import AOSToolbar
from AOSProductsPage import AOSProductPage
from AOSHomePage import AOSHomePage
from AOSCategoryPage import AOSCategoryPage
from AOS_cart import AOSCart
from register import Register
from Checkout import Checkout
from login import Login


class TestAOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Selenium1\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

        self.Home = AOSHomePage(self.driver)
        self.Category = AOSCategoryPage(self.driver)
        self.Product = AOSProductPage(self.driver)
        self.Toolbar = AOSToolbar(self.driver)
        self.Cart = AOSCart(self.driver)
        self.Register = Register(self.driver)
        self.Checkout = Checkout(self.driver)

    def test_cart_window_amount(self):
        """This test checks that the numbers of selected products is displayed in the cart window"""
        self.Home.speakers().click()
        self.Category.product_id("20").click()
        q2 = 2
        self.Product.quantity_amount(q2)
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.laptops().click()
        self.Category.product_id("9").click()
        q1 = 4
        self.Product.quantity_amount(q1)
        self.Product.add_to_cart().click()
        self.assertEqual(self.Cart.cart_icon_window_number(), q1 + q2)
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_cart_window_info(self):
        """This test checks that the color,quantity,name and price displayed in the cart window"""
        self.Home.speakers().click()
        self.Category.product_id("24").click()
        c3 = "RED"
        self.Product.product_color(c3)
        qt3 = 1
        self.Product.quantity_amount(qt3)
        price3 = self.Product.product_price()
        p3 = self.Product.product_name()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.mice().click()
        self.Category.product_id("30").click()
        c2 = "RED"
        self.Product.product_color(c2)
        qt2 = 2
        self.Product.quantity_amount(qt2)
        price2 = self.Product.product_price()
        p2 = self.Product.product_name()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.tablets().click()
        self.Category.product_id("18").click()
        c1 = "BLACK"
        self.Product.product_color(c1)
        qt1 = 3
        self.Product.quantity_amount(qt1)
        price1 = self.Product.product_price()
        p1 = self.Product.product_name()
        self.Product.add_to_cart().click()
        p_names = [p1, p2, p3]
        self.assertEqual(p_names, self.Cart.cart_window_names())
        p_colors = [c1, c2, c3]
        self.assertEqual(p_colors, self.Cart.cart_window_colors())
        p_quantity = [qt1, qt2, qt3]
        self.assertEqual(p_quantity, self.Cart.cart_window_quantities())
        prices = [price1 * qt1, price2 * qt2, price3 * qt3]
        self.assertEqual(prices, self.Cart.cart_window_prices())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_cart_window_remove_product(self):
        """this test checks that the product disappear from the
        cart window after removing the product by pressing 'X'"""
        self.Home.headphones().click()
        self.Category.product_id("12").click()
        p2 = self.Product.product_name()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.tablets().click()
        self.Category.product_id("16").click()
        p1 = self.Product.product_name()
        self.Product.add_to_cart().click()
        self.Cart.cart_window_remove().click()
        self.assertEqual(self.Cart.cart_icon_window_number(), 1)
        self.assertNotIn(p1, self.Cart.cart_window_names())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_cart_page_open(self):
        """This test checks that by pressing the cart icon you will transfer to the cart page"""
        self.Home.speakers().click()
        self.Category.product_id("25").click()
        self.Product.add_to_cart().click()
        self.Toolbar.cart_icon().click()
        self.wait.until(EC.visibility_of(self.Cart.cart_page_title()))
        self.assertEqual("SHOPPING CART", self.Cart.cart_page_title_path())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_cart_page_total_price(self):
        """This test checks that the sum of all the products is equal to the total price displayed in the cart page"""
        self.Home.laptops().click()
        self.Category.product_id("11").click()
        qt3 = 2
        self.Product.quantity_amount(qt3)
        name3 = self.Product.product_name()
        price3 = self.Product.product_price()
        self.Product.add_to_cart().click()
        print(f"Product Name: {name3}\n"
              f"Unit Price: {price3}   "
              f"Quantity: {qt3}   "
              f"Total Price: {price3 * qt3}")
        print("-------------------------------------------------------")
        self.Toolbar.aos_icon().click()
        self.Home.mice().click()
        self.Category.product_id("26").click()
        qt2 = 4
        self.Product.quantity_amount(qt2)
        name2 = self.Product.product_name()
        price2 = self.Product.product_price()
        self.Product.add_to_cart().click()
        print(f"Product Name: {name2}\n"
              f"Unit Price: {price2}   "
              f"Quantity: {qt2}   "
              f"Total Price: {price2 * qt2}")
        print("-------------------------------------------------------")
        self.Toolbar.aos_icon().click()
        self.Home.tablets().click()
        self.Category.product_id("17").click()
        qt1 = 1
        self.Product.quantity_amount(qt1)
        name1 = self.Product.product_name()
        price1 = self.Product.product_price()
        self.Product.add_to_cart().click()
        print(f"Product Name: {name1}\n"
              f"Unit Price: {price1}   "
              f"Quantity: {qt1}   "
              f"Total Price: {price1 * qt1}")
        self.Toolbar.cart_icon().click()
        self.assertEqual(round((price3 * qt3) + (price2 * qt2) + (price1 * qt1), 2), self.Cart.cart_page_total_price())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_edit_quantity(self):
        """This test checks that after you're editing the order quantity the quantity gets updated"""
        self.Home.speakers().click()
        self.Category.product_id("23").click()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.mice().click()
        self.Category.product_id("33").click()
        self.Product.add_to_cart().click()
        self.Toolbar.cart_icon().click()
        self.Cart.cart_page_edit_button(1).click()
        qt2 = 3
        self.Product.quantity_amount(qt2)
        self.Product.add_to_cart().click()
        self.Cart.cart_page_edit_button(2).click()
        qt1 = 3
        self.Product.quantity_amount(qt1)
        self.Product.add_to_cart().click()
        self.assertEqual(qt1 + qt2, self.Cart.cart_page_quantities())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_back_to_category_and_home_page(self):
        """This test checks that after you're adding a product you can go back to
        the category page and then back to the home page"""
        self.Home.tablets().click()
        self.Category.product_id("16").click()
        self.Product.add_to_cart().click()
        self.driver.back()
        self.assertEqual("TABLETS", self.Category.category_title())
        self.driver.back()
        self.assertEqual("https://www.advantageonlineshopping.com/#/", self.driver.current_url)
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_checkout_register_with_SafePay(self):
        """This test checks that after you register and pay with SafePay the payment
        succeed, the cart is empty and the order exist in the user orders"""
        self.Home.speakers().click()
        self.Category.product_id("20").click()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.laptops().click()
        self.Category.product_id("9").click()
        self.Product.add_to_cart().click()
        self.Cart.cart_window_checkout_button().click()
        self.Register.registration_button1().click()
        self.Register.username("Noam28")
        self.Register.email("Tal28@gmail.com")
        self.Register.password_and_confirmation("TalNoam28")
        self.wait.until(EC.invisibility_of_element(self.Cart.cart_window()))
        self.Register.agree_to_terms().click()
        self.Register.registration_button2().click()
        self.Register.next_button().click()
        self.Checkout.safe_pay_username("Tester12")
        self.Checkout.safe_pay_password("tesTer12")
        self.Checkout.pay_now_safepay().click()
        self.wait.until(EC.visibility_of(self.Checkout.thanks_for_buying()))
        order_num = self.Checkout.order_number()
        self.assertIn("Thank you for buying with Advantage", self.Checkout.thanks_for_buying().text)
        self.Toolbar.cart_icon().click()
        self.assertIn("empty", self.Cart.empy_message())
        self.wait.until(EC.invisibility_of_element(self.Cart.cart_window()))
        self.Toolbar.user_icon().click()
        self.Toolbar.my_orders().click()
        self.assertEqual(order_num, self.Toolbar.my_orders_order_num())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_checkout_login_with_CreditCard(self):
        """This test checks that after you log in to an existing account and pay with a credit card
        the cart is empty and the order exist in the user orders"""
        login = Login(self.driver)
        self.Home.speakers().click()
        self.Category.product_id("23").click()
        self.Product.add_to_cart().click()
        self.Toolbar.aos_icon().click()
        self.Home.mice().click()
        self.Category.product_id("32").click()
        self.Product.add_to_cart().click()
        self.Cart.cart_window_checkout_button().click()
        login.username_checkout("Noam4")
        login.password_checkout("Noam432")
        login.login_button_checkout().click()
        self.Register.next_button().click()
        self.Checkout.credit_option().click()
        self.Checkout.credit_number(123456784596)
        self.Checkout.cvv_number(852)
        self.Checkout.cardholder_name("Noam Aharon")
        self.Checkout.pay_now_credit()
        order_num = self.Checkout.order_number()
        self.Toolbar.cart_icon().click()
        self.assertIn("empty", self.Cart.empy_message())
        self.wait.until(EC.invisibility_of_element_located(self.Cart.cart_window()))
        self.Toolbar.user_icon().click()
        self.Toolbar.my_orders().click()
        self.assertEqual(order_num, self.Toolbar.my_orders_order_num())
        self.Toolbar.aos_icon().click()
        self.driver.quit()

    def test_login_logout(self):
        """This test check that the login and logout process works"""
        login = Login(self.driver)
        self.Toolbar.user_icon().click()
        login.username_floating_window("TesTer1")
        login.password_floating_window("Tester234")
        login.signin_floating_window().click()
        self.wait.until(EC.visibility_of(self.Home.speakers()))
        self.assertEqual("TesTer1", self.Toolbar.user_name().text)
        self.Toolbar.user_icon().click()
        self.Toolbar.user_sign_out().click()
        self.assertEqual("", self.Toolbar.user_name().text)
        self.driver.quit()