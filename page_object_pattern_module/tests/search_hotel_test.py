from selenium import webdriver

from page_object_pattern_module.pages.search_hotel import SearchHotelPage
from page_object_pattern_module.pages.search_hotel_result import SearchHotelResultPage

import pytest
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchHotel:

    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_search_hotel(self, test_setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_check_in("15/10/2020")
        search_hotel_page.set_check_out("19/10/2020")
        search_hotel_page.set_travellers("1 Adult 3 Child")
        search_hotel_page.search_hotel()
        search_result_page = SearchHotelResultPage(self.driver)
        hotel_names = search_result_page.get_hotel_names()
        prices_values = search_result_page.get_hotel_prices()


        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert prices_values[0] == '$22'
        assert prices_values[1] == '$50'
        assert prices_values[2] == '$80'
        assert prices_values[3] == '$150'