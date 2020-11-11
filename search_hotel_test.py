import datetime
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
driver.find_element_by_name("checkin").send_keys("15/10/2020")
driver.find_element_by_name("checkout").send_keys("19/10/2020")
driver.find_element_by_id("travellersInput").clear()
driver.find_element_by_id("travellersInput").send_keys("1 Adult 3 Child")
driver.find_element_by_xpath("//button[text()=' Search']").click()
#//h4[contains(@class,'list_title')]//b
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
prices_values = [price.get_attribute("textContent") for price in prices]

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

assert prices_values[0] == '$22'
assert prices_values[1] == '$50'
assert prices_values[2] == '$80'
assert prices_values[3] == '$150'

time.sleep(2)
driver.quit()