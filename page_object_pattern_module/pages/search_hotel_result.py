from page_object_pattern_module.locators.locators import SearchResultLocators
import logging

class SearchHotelResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotels_xpath = SearchResultLocators.hotels_xpath
        self.text_attribute = SearchResultLocators.text_attribute
        self.prices_xpath = SearchResultLocators.prices_xpath
        self.logger = logging.getLogger(__name__)

    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotels_xpath)
        self.logger.info("Available hotels are: ")
        names = [hotel.get_attribute(self.text_attribute) for hotel in hotels]
        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.prices_xpath)
        hotel_prices = [price.get_attribute(self.text_attribute) for price in prices]
        self.logger.info("Current hotel prices are: ")
        for  price in hotel_prices:
            self.logger.info(price)
        return hotel_prices