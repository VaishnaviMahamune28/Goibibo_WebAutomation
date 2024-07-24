from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)
        self.image=(By.XPATH,'//div[@class="NewSortOptionsstyles__SortTab-sc-1k34lsv-5 jVPxPT flex1 flexCol alignItemsCenter blueCnt"]//*[2]')
        self.down_arrow = (By.XPATH, "//div[@class='f500 txtUpper dF alignItemsCenter']//*[name()='svg' and @class='ArrowDown__ArrowDownIcon-sc-1oyna77-0 kwjccM']")
        self.up_arrow=(By.XPATH,"//div[@class='f500 txtUpper dF alignItemsCenter']//*[name()='svg' and @class='ArrowUp__ArrowUpIcon-sc-4psm7l-0 eSNSDJ']")
        self.update_btn=(By.XPATH,"//button[text()='UPDATE SEARCH']")

    def price_order(self):
        update_button=self.wait.until(EC.presence_of_element_located(self.update_btn))
        update_button.click()
        time.sleep(10)
        try:
            assending_order=self.wait.until(EC.presence_of_element_located(self.down_arrow))
            image_indicator=self.wait.until(EC.presence_of_element_located(self.image))
            if assending_order.is_displayed():
                print("Prices are in ascending order.")
                assert(image_indicator==assending_order)
        except TimeoutException:
            print("Timeout while waiting for the downarrow element.")
            self.driver.save_screenshot("timeout_exception_screenshot.png")
            raise

        try:
            descending_order=self.wait.until(EC.presence_of_element_located(self.up_arrow))
            image_indicator=self.wait.until(EC.presence_of_element_located(self.image))
            if descending_order.is_displayed():
                print("Prices are in descending order.")
                assert(image_indicator==descending_order)
        except:
            print("Timeout while waiting for the uparrow element.")
            self.driver.save_screenshot("timeout_exception_screenshot.png")
            raise