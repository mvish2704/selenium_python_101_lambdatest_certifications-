import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LambdaAutomationSeleniumPython(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(cls):
        """Set up the WebDriver before each test."""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_scenario1(self):
        """Test Scenario 1: Simple Form Demo"""
        # Step 1: Open the Selenium Playground
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        
        # Step 2: Click on "Simple Form Demo"
        demo_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Simple Form Demo")))
        time.sleep(1.5)
        demo_link.click()

        # Step 3: Validate the URL
        expected_url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)

        # Step 4: Enter a welcome message
        welcome = "Welcome to LambdaTest ASSIGNMENT"

        # Step 5: Enter the message in the text box
        enter_text = self.driver.find_element(By.XPATH, "//*[@id='user-message']")
        enter_text.send_keys(welcome)
        time.sleep(2)

        # Step 6: Click "Get Checked Value"
        checked = self.driver.find_element(By.XPATH, "//*[@id='showInput']")
        checked.click()
        time.sleep(2)

        # Step 7: Validate the message
        my_msg = self.driver.find_element(By.XPATH, "//*[@id='message']")
        my_msg_text = my_msg.text
        self.assertEqual(my_msg_text, welcome)

    def test_scenario2(self):
        """Test Scenario 2: Drag & Drop Sliders"""
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        self.driver.get("https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo")
        # Set the value of the slider directly to 100
        self.driver.find_element(By.CSS_SELECTOR, ".sp__range-success > .sp__range").send_keys("100")
        time.sleep(1)
        # Click on the slider
        self.driver.find_element(By.CSS_SELECTOR, ".sp__range-success > .sp__range").click()
        time.sleep(1)
        # Get the ID of the slider
        id_set = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div/div/div/div[2]/div[1]/div/output').id
        print("ID:" + id_set)

    def test_scenario3(self):
        """Test Scenario 3: Input Form Submit"""
        self.driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
        submit = self.driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button")
        submit.click()
        name = self.driver.find_element(By.ID, "name")
        required_message = name.get_attribute("required")
        self.assertTrue(required_message)
        error_message = "Please fill out this field."
        self.assertTrue(error_message)
        time.sleep(5)
        country = self.driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[3]/div[1]/select")
        country.click()
        country_option = self.driver.find_element(By.CSS_SELECTOR,
                                                  "#seleniumform > div:nth-child(3) > "
                                                  "div.form-group.w-6\\/12.smtablet\\:w-full.pr-20.smtablet\\:pr-0 > "
                                                  "select > option:nth-child(238)")
        country_option.click()
        name.send_keys("Test Lambda")
        time.sleep(1)
        email = self.driver.find_element(By.CSS_SELECTOR, "#inputEmail4")
        email.send_keys("TestData@gmail.com")
        time.sleep(1)
        password = self.driver.find_element(By.ID, "inputPassword4")
        password.send_keys("Test_Lamda#@123")
        time.sleep(1)
        company = self.driver.find_element(By.XPATH, "//*[@id='company']")
        company.send_keys("Test_Lamda pvt ltd.")
        time.sleep(1)
        website = self.driver.find_element(By.CSS_SELECTOR, "#websitename")
        website.send_keys("www.Test_Lamda.com")
        time.sleep(1)
        city = self.driver.find_element(By.ID, "inputCity")
        city.send_keys("Earth")
        time.sleep(1)
        address1 = self.driver.find_element(By.XPATH, "//*[@id='inputAddress1']")
        address1.send_keys("Earth_Air")
        time.sleep(1)
        address2 = self.driver.find_element(By.CSS_SELECTOR, "#inputAddress2")
        address2.send_keys("Earth Water")
        time.sleep(1)
        state = self.driver.find_element(By.ID, "inputState")
        state.send_keys("Test_Lamda State")
        time.sleep(1)
        zipcode = self.driver.find_element(By.XPATH, "//*[@id='inputZip']")
        zipcode.send_keys("111111")
        time.sleep(1)
        submit.click()
        submit_msg = "Thanks for contacting us, we will get back to you shortly."
        actual_submit = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/section[2]/div/div/div/div/p").text
        self.assertEqual(actual_submit, submit_msg)
        time.sleep(5)
        self.driver.close()

    @classmethod
    def tearDown(cls):
        """Close the WebDriver after each test."""
        if cls.driver is not None:
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
