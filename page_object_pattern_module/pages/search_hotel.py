from page_object_pattern_module.locators.locators import SearchHotelsLocators
import logging


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = SearchHotelsLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelsLocators.search_hotel_input_xpath
        self.location_match_xpath = SearchHotelsLocators.location_match_xpath
        self.check_in_input_name = SearchHotelsLocators.check_in_input_name
        self.check_out_input_name = SearchHotelsLocators.check_out_input_name
        self.travellers_input_id = SearchHotelsLocators.travellers_input_id
        self.search_button_xpath = SearchHotelsLocators.search_button_xpath
        self.logger = logging.getLogger(__name__)

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()


    def set_check_in(self, check_in_date):
        self.logger.info("Setting checkin date {}".format(check_in_date))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in_date)

    def set_check_out(self, check_in_out):
        self.logger.info("Setting checkout date {}".format(check_in_out))
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_in_out)

    def set_travellers (self, number_of_travellers):
        self.logger.info("Setting number of travellers {}".format(number_of_travellers))
        self.driver.find_element_by_id(self.travellers_input_id).clear()
        self.driver.find_element_by_id(self.travellers_input_id).send_keys(number_of_travellers)

    def search_hotel(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

