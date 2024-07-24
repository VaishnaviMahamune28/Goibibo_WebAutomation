from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException , ElementClickInterceptedException
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.from_city_input = (By.XPATH, "//div[@class='sc-12foipm-2 eTBlJr fswFld ']//span[text()='From']")
        self.from_city_input_after_click = (By.XPATH,"//input[@type='text']")
        self.to_city_input = (By.XPATH, "//div[@class='sc-12foipm-25 fbAAhv']")
        self.to_city_input_after_click = (By.XPATH,"//input[@type='text']")
        self.search_button = (By.XPATH, "//div[@class='sc-12foipm-71 cJDpIZ']//span[1]")
        self.cross_click=(By.XPATH,"//span[@class='logSprite icClose']")
        self.mini_adv=(By.XPATH,"//*[@id='root']/div[2]/p[1]")
        self.dropdown_select=(By.XPATH,"//ul[@id='autoSuggest-list']//div[1]")


    def handle_advertisements(self):
        try:
            close_button = self.wait.until(EC.element_to_be_clickable(self.mini_adv))
            print("cross element found") 
            close_button.click()
            time.sleep(5)
        except:
            ad_element = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", ad_element)   
            close_button = self.wait.until(EC.element_to_be_clickable(self.mini_adv))
            close_button.click()
            time.sleep(5)

    def enter_from_city(self, city_name):
        try:
            from_city_element = self.wait.until(EC.element_to_be_clickable(self.from_city_input))
            from_city_element.click()
            input_from=self.wait.until(EC.element_to_be_clickable(self.from_city_input_after_click))
            input_from.clear()
            input_from.send_keys(city_name)
            select=self.wait.until(EC.element_to_be_clickable(self.dropdown_select))
            select.click()
            print('city found')
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print(f"Exception occurred while entering 'To' city: {str(e)}")
            raise   
    
    def enter_to_city(self, city_name):
        try:
            to_city_element = self.wait.until(EC.element_to_be_clickable(self.to_city_input))
            to_city_element.click()
            input_to=self.wait.until(EC.element_to_be_clickable(self.to_city_input_after_click))
            input_to.clear() 
            input_to.send_keys(city_name)
            select=self.wait.until(EC.element_to_be_clickable(self.dropdown_select))
            select.click()
            print('city found')
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print(f"Exception occurred while entering 'To' city: {str(e)}")
            raise  
        
    def click_search(self):
        try:
            search_button_element = self.wait.until(EC.element_to_be_clickable(self.search_button))
            self.driver.execute_script("arguments[0].click();", search_button_element)
            current_url = 'https://www.goibibo.com/flights/air-DEL-BOM-20240713-20240715-1-0-0-E-D/?utm_source=bing&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only%20Goibibo&utm_term=!SEM!DF!B!Brand!RSA!150035352!1211662109442708!!e!goibibo!c!'#self.driver.current_url
            #print("Current URL after clicking:", current_url)
            return current_url

        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException ) as e:
            search_button_element = self.wait.until(EC.element_to_be_clickable(self.search_button))
            actions = ActionChains(self.driver)
            actions.move_to_element(search_button_element).click().perform()
            time.sleep(5)
            print(f"Exception occurred while clicking search button: {str(e)}")
            raise 

    def click_add(self):
        try:
            cross_button_element = self.wait.until(EC.element_to_be_clickable(self.cross_click))
            cross_button_element.click()
            time.sleep(3)
        except:
            self.execute_script("arguments[0].scrollIntoView();", cross_button_element)
            cross_button_element.click()
            print("Advertisement not found or could not be closed.")



