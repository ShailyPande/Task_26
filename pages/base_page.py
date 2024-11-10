from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver,url):
        self.driver = driver
        self.url=url

    def click_element(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()


    def launch_url(self,timeout=40):
        self.driver.get(self.url)
        self.driver.maximize_window()
        #WebDriverWait(self.driver, timeout).until(EC.url_to_be(self.url))


    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
