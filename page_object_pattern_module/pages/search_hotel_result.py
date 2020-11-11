from page_object_pattern_module.locators.locators import SearchResultLocators

class SearchHotelResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotels_xpath = SearchResultLocators.hotels_xpath
        self.text_attribute = SearchResultLocators.text_attribute
        self.prices_xpath = SearchResultLocators.prices_xpath

    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotels_xpath)
        return [hotel.get_attribute(self.text_attribute) for hotel in hotels]


    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.prices_xpath)
        return [price.get_attribute(self.text_attribute) for price in prices]
