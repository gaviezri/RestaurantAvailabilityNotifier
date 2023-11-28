import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime

driver = webdriver.Chrome()
driver.get('https://bookings.zenchef.com/results?rid=358407')
guestSelect = Select(driver.find_element(By.XPATH, "(//select)[1]"))
dateInput = driver.find_element(By.XPATH, "(//input)[1]")

guestSelect.select_by_index(1)
dateInput.click()
if(datetime.now().month == 11):
    driver.find_element(By.XPATH, "(//div[@class='DayPicker-NavButton'])[1]").click()
# figure out how to get the clickable element
driver.find_element(By.CSS_SELECTOR,"div[aria-label='Monday, 18 December 2023']").click()

# move to december if needed
# select 18, 19, 20
# if "Service" is available
# send email to me and gili
driver.refresh()
# dateInput.send_keys("Tue 19 Dec")
# dateInput.send_keys("Wed 20 Dec")
elem = driver.find_element(By.XPATH, "//div[contains(text(), 'service')]")
input()
def check_available_dates(restaurant_url):
    # Send an HTTP request to the restaurant's website
    response = requests.get(restaurant_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use BeautifulSoup to navigate and extract information about available dates
        # This part depends on the specific structure of the website
        # Example: find all elements with a certain class
        available_dates = soup.find_all('span', class_='available-date')

        # Process and print the available dates
        for date in available_dates:
            print(date.text)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage
restaurant_url = 'https://bookings.zenchef.com/results?rid=358407'
check_available_dates(restaurant_url)
