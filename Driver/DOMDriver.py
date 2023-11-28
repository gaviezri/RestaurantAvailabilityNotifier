from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime

dates = ['Monday, 18 December 2023', 'Tuesday, 19 December 2023', 'Wednesday, 20 December 2023']
class DOMDriver:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def check_availability(self):
        driver = self.driver
        driver.refresh()
        self.select_guests()
        for date in dates:
            self.select_date(date)
            try:
                driver.find_element(By.XPATH, "//div[contains(text(), 'service')]")
                return True, date
            except...:
                continue
        return False, date


    def select_date(self, date):
        driver = self.driver
        # open date picker
        date_picker = driver.find_element(By.XPATH, "(//input)[1]")
        date_picker.click()
        if datetime.now().month == 11:
            # move to december
            driver.find_element(By.XPATH, "(//div[@class='DayPicker-NavButton'])[1]").click()
        driver.find_element(By.CSS_SELECTOR, f"div[aria-label={date}]").click()

    def select_guests(self):
        guest_select = Select(self.driver.find_element(By.XPATH, "(//select)[1]"))
        guest_select.select_by_index(1)
