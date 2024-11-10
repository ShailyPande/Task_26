
import pytest
from pages.base_page import BasePage
from pages.names_page import NamesPage
from Utils.config import BASE_URL



@pytest.mark.usefixtures("setup")
class TestNamePage:
    def test_Name_Page(self, setup):
        self.driver = setup
        namepage_data = NamesPage(self.driver, BASE_URL)
        namepage_data.expand_all_button_click()
        namepage_data.enter_name("Audrey")
        namepage_data.enter_start_birthdate("11-11")
        namepage_data.enter_end_birthdate("11-12")
        namepage_data.enter_birthday("11-11-2011")
        namepage_data.select_award_options(["oscar_nominated"])
        namepage_data.select_topic(option_value='Biography')
        namepage_data.enter_start_deathdate("11-20")
        namepage_data.enter_end_deathdate("11-20")
        namepage_data.select_gender(gender="Female")
        namepage_data.credit(credit="abc")
        namepage_data.select_adult_name(option="Exclude")
        namepage_data.click_see_result()
        print("Quitting driver")
        self.driver.quit()

