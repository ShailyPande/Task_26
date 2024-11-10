from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class NamesPage(BasePage):

    def __init__(self,driver, url):
        super().__init__(driver, url)
        self.url = url
        self.driver = driver

        self.expand_all_locator = (By.XPATH, '//span[text()="Expand all"]')
        self.name_field_locator = (By.XPATH, '//input[@name="name-text-input"]')
        self.birth_start_date_locator = (By.XPATH, '//input[name="birthYearMonth-start"]')
        self.birth_end_date_locator = (By.XPATH, '//input[name="birthYearMonth-end"]')
        self.birthday_field_locator = (By.XPATH, '//input[@name="birthday-input"]')

        self.best_actress_nominated_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_actress_nominees"]')
        self.best_actor_nominated_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_actor_nominees"]')
        self.best_actress_winning_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_actress_winners"]')
        self.best_actor_winning_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_actor_winners"]')
        self.best_supporting_actress_nominated_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_supporting_actress_nominees"]')
        self.best_supporting_actor_nominated_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_supporting_actor_nominees"]')
        self.best_supporting_actress_winning_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_supporting_actress_winners"]')
        self.best_supporting_actor_winning_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_supporting_actor_winners"]')
        self.best_director_nominated_awards = (
        By.XPATH, '//button[@data-testid ="test-chip-id-oscar_best_director_nominees"]')
        self.best_director_winning_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-best_director_winner"]')
        self.oscar_nominated_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-oscar_nominee"]')
        self.emmy_award_nominated_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-emmy_nominee"]')
        self.golden_globe_nominated_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-golden_globe_nominated"]')
        self.oscar_winning_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-oscar_winner"]')
        self.emmy_award_winning_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-emmy_winner"]')
        self.golden_globe_winning_awards = (By.XPATH, '//button[@data-testid ="test-chip-id-golden_globe_winning"]')

        self.award_nominations_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-AWARD_NOMINATIONS"]')
        self.biography_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-BIOGRAPHY"]')
        self.birth_date_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-BIRTH_DATE"]')
        self.place_of_birth_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-BIRTH_PLACE"]')
        self.death_date_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-DEATH_DATE"]')
        self.place_of_death_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-DEATH_PLACE"]')
        self.height_info_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-HEIGHT_INFO"]')
        self.quotes_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-QUOTES"]')
        self.trivia_topics = (By.XPATH, '//button[@data-testid ="test-chip-id-TRIVIA"]')

        self.death_start_date_locator = (By.XPATH, '//input[@name="deathYearMonth-start"]')
        self.death_end_date_locator = (By.XPATH, '//input[@name="death-year-month-end-input"]')

        self.male_gender = (By.XPATH, '//span[text()="Male"]')
        self.female_gender = (By.XPATH, '//span[text()="Female"]')
        self.non_binary_gender = (By.XPATH, '//span[text()="Non-binary"]')
        self.other_gender = (By.XPATH, '//span[text()="Other"]')

        self.credit_locator = (By.XPATH, '//input[@data-testid="autosuggest-input-test-id-filmography"]')
        self.exclude_radio_button_locator = (By.XPATH, '//input[@id="exclude-adult-names"]')
        self.include_radio_button_locator = (By.XPATH, '//input[@id="exclude-adult-names"]')

        self.see_result_locator = (By.XPATH, '//span[text()="See results"]')

    def expand_all_button_click(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.expand_all_locator)).click()

    def enter_name(self, name):
        enter_name_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.name_field_locator))
        enter_name_field.send_keys(name)

    def enter_start_birthdate(self, start_birthdate):
        enter_start_birthdate = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.birth_start_date_locator))
        enter_start_birthdate.send_keys(start_birthdate)

    def enter_end_birthdate(self, end_birthdate):
        enter_end_birthdate = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.birth_end_date_locator))
        enter_end_birthdate.send_keys(end_birthdate)

    def enter_birthday(self, birthday):
        enter_birthday_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.name_field_locator))
        enter_birthday_field.send_keys(birthday)

    def select_award_options(self, award_types):
        award_locator_map = {
            "best_actress_nominated": self.best_actress_nominated_awards,
            "best_actor_nominated": self.best_actor_nominated_awards,
            "best_actress_winning": self.best_actress_winning_awards,
            "best_actor_winning": self.best_actor_winning_awards,
            "best_supporting_actress_nominated": self.best_supporting_actress_nominated_awards,
            "best_supporting_actor_nominated": self.best_supporting_actor_nominated_awards,
            "best_supporting_actress_winning": self.best_supporting_actress_winning_awards,
            "best_supporting_actor_winning": self.best_supporting_actor_winning_awards,
            "best_director_nominated": self.best_director_nominated_awards,
            "best_director_winning": self.best_director_winning_awards,
            "oscar_nominated": self.oscar_nominated_awards,
            "emmy_award_nominated": self.emmy_award_nominated_awards,
            "golden_globe_nominated": self.golden_globe_nominated_awards,
            "oscar_winning_awards": self.oscar_winning_awards,
            "emmy_award_winning": self.emmy_award_winning_awards,
            "golden_globe_winning": self.golden_globe_winning_awards,
        }

        for award_type in award_types:
            locator = award_locator_map.get(award_type)

            if locator is None:
                raise ValueError(f"Invalid award type provided: {award_type}")

            button = self.driver.find_element(*locator)
            button.click()


    def select_topic(self, option_value=None):
        self.search_within_topic = (By.XPATH, '//select[@id="within-topic-dropdown-id"]')
        dropdown = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_within_topic))
        select = Select(dropdown)
        select.select_by_value(option_value)

    def enter_start_deathdate(self, start_deathdate):
        start_death_date = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.death_start_date_locator))
        start_death_date.send_keys(start_deathdate)

    def enter_end_deathdate(self, end_birthdate):
        end_birth_date = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.death_end_date_locator))
        end_birth_date.send_keys(end_birthdate)

    def select_gender(self, gender=None):
        gender_locator_map = {
            "Male": self.male_gender,
            "Female": self.female_gender,
            "Non-binary": self.non_binary_gender,
            "other": self.other_gender
        }

        gender_locator = gender_locator_map.get(gender)

        if gender_locator is None:
            raise ValueError("Invalid gender provided. Choose from 'male', 'female', 'non-binary', or 'other'.")

        radio_button = self.driver.find_element(*gender_locator)
        radio_button.click()

    def credit(self, credit):
        enter_credit = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.credit_locator))
        enter_credit.send_keys(credit)

    def select_adult_name(self,option):
        option_locator_map = {
            "Exclude": self.exclude_radio_button_locator,
            "Include": self.include_radio_button_locator
        }

        adult_locator = option_locator_map.get(option)

        if adult_locator is None:
            raise ValueError("Invalid option provided. Choose 'exclude' or 'include'.")

            # Find and click the radio button element
        radio_button = self.driver.find_element(*adult_locator)
        radio_button.click()

    def click_see_result(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.see_result_locator)).click()











