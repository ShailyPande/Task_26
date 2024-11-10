from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def setup(request):
    """
      Setup Selenium WebDriver for class-level tests.
      Initializes the driver, maximizes the browser window, and quits after tests.
      """

    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    # print("Quitting driver")
    # driver.quit()

