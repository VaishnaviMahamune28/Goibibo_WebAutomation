from utils.driver_manager import take_screenshot, driver  # Import driver fixture

def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        driver = item.funcargs['driver']
        take_screenshot(driver, item.name)
