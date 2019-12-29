import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver.exe")

    def test_facebook_login(self):
        driver = self.driver
        driver.get("http://www.facebook.com")
        self.assertIn("Facebook", driver.title)
        email_elem = self.driver.find_element_by_css_selector('#email')
        email_elem.send_keys('dummy@gmail.com')
        pwd_elem = self.driver.find_element_by_css_selector('#pass')
        pwd_elem.send_keys('dummy')
        subnit_elem = self.driver.find_element_by_css_selector('#loginbutton')
        subnit_elem.click()
        time.sleep(5)
        # Assert that 'Dashboard' is present in target pages browser title
        self.assertIn('Dashboard', self.driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
