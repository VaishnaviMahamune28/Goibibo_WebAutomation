import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
# Configure page load strategy
    driver.set_page_load_timeout(30) 
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    driver.save_screenshot(f'screenshots/{name}.png')
