import time
from PageObject.LoginPage import Login
from TestCases.confest import setup
from TestCases.confest import browser
from Utilities.ConfigReadValue import ReadValue
from Utilities.Logger import Loggen



class Test_Url_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    Url = ReadValue.getUrl()
    log = Loggen.loggen()

    def test_url(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        time.sleep(3)
        self.log.info("Opening Url")
        self.log.info("Printing Page Title")
        print(self.driver.title)

        self.log.info("Checking Page Title")
        if self.driver.title == "OrangeHRM":
            self.log.info("test_url is passed")
            self.driver.save_screenshot("C:\\Users\\Suyash\\Desktop\\CREDENCE CLASS\\Pycharm Program\\OrangeHRM by Me\\ScreenShots\\test_url_pass.png")
            assert True
        else:
            self.log.info("test_url is Failed")
            self.driver.save_screenshot("C:\\Users\\Suyash\\Desktop\\CREDENCE CLASS\\Pycharm Program\\OrangeHRM by Me\\ScreenShots\\test_url_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_url is Completed")


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Opening Browser")
        self.log.info("Going to Url")
        self.lp = Login(self.driver)
        self.log.info("Enter Username")
        self.lp.enter_username(self.username)
        self.log.info("Enter Password")
        self.lp.enter_password(self.password)
        self.log.info("Click Login Button")
        self.lp.click_login()
        if self.lp.login_status() == True:
            self.log.info("test_login is passed")
            self.driver.save_screenshot("C:\\Users\\Suyash\\Desktop\\CREDENCE CLASS\\Pycharm Program\\OrangeHRM by Me\\ScreenShots\\test_login_pass.png")
            self.log.info("Click on Menu")
            self.lp.click_menu()
            self.log.info("Click on logout")
            self.lp.click_logout()
            assert True
        else:
            self.log.info("test_login is failed")
            self.driver.save_screenshot("C:\\Users\\Suyash\\Desktop\\CREDENCE CLASS\\Pycharm Program\\OrangeHRM by Me\\ScreenShots\\test_login_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_login is Completed")
