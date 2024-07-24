from pages.base_page import *
from selenium.webdriver.common.by import By
from pages.goibibo_home_page import SearchResultsPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_home_page(driver):
    driver.get("https://www.goibibo.com")
    time.sleep(5)
    home_page = HomePage(driver)
    home_page.click_add()
    driver.refresh()
    home_page.handle_advertisements()
    home_page.enter_from_city("Mumbai")
    home_page.enter_to_city("New Delhi")
    url=home_page.click_search()
    driver.execute_script(f"window.open('{url}', 'new_window', 'height=600,width=800');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(10)
    driver.get_log('browser')
    search_results_page = SearchResultsPage(driver)
    search_results_page.price_order()