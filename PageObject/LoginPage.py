from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    Text_username_name = (By.NAME, "username")
    Text_password_name = (By.NAME, "password")
    Click_login_Xpath = (By.XPATH, "//button[@type='submit']")
    Check_Status_Xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Menu_Xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "username")))
        self.driver.find_element(*Login.Text_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Login.Text_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Login.Click_login_Xpath).click()


    def login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
            self.driver.find_element(*Login.Check_Status_Xpath)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def click_menu(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
        self.driver.find_element(*Login.Click_Menu_Xpath).click()


    def click_logout(self):
        self.driver.find_element(*Login.Click_Logout_Xpath).click()
