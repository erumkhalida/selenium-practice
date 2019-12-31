from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from pages.loginpage import LoginPage
from pages.registerpage import Registrer
from pages.Dashboard import Dashboard

class McK_login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        self.login = LoginPage(self.driver)
        self.register = Registrer(self.driver)
        self.dashboard = Dashboard(self.driver)
          #login to this site
    def test_loginPage(self):
        self.driver.get("https://courses.edx.org")
        self.assertTrue(self.login.is_browser_on_the_Mpage())
        self.driver.find_element_by_link_text('Sign In').click()  

        #This is login Page
        self.assertTrue(self.login.is_browser_on_the_loginpage())        
        self.login.enter_username('erum.khalida@arbisoft.com')              
        self.login.enter_password('thispassword_11')
        self.login.submit_button()
        self.assertTrue(self.dashboard.is_browser_on_the_page())
        self.login.logout()


        self.assertTrue(self.register.is_browser_on_the_Mpage())
        
        #this is Register Page    
        self.driver.find_element_by_link_text('Register').click()
        self.assertTrue(self.register.is_browser_on_the_registerpage())
        self.register.regemail('erumkhalida@yopmail.com')
        self.register.regname('erumk')
        self.register.regusername('erumk123')
        self.register.regpassword('123abc__')
        self.register.regcountry('Pakistan')
        self.register.submitButton()
        self.assertTrue(self.dashboard.is_browser_on_the_page())
        self.register.logout()
        self.assertTrue(self.register.is_browser_on_the_Mpage())
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
