from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time as t

service = Service('C:\\Users\\aburn\\Downloads\\chromedriver_win32\\chromedriver.exe')

def initiate_driver():
    """create driver with options"""
    URL = "https://automated.pythonanywhere.com/"
    options = webdriver.ChromeOptions()
    options.add_argument("disable-inforbars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    return driver

# def main():
#     """create instance of driver and scrape text value from given website"""
#     driver = initiate_driver()
#     element = driver.find_element(by = "xpath", value = "/html/body/div[1]/div/h1[1]")
#     return element.text

def get_temperature_from_text(text):
    """ INPUT: str input formated like sdjndjlf jfl: ___ where the blank
        value is a changing number
        OUTPUT: the number as a float
    """
    output = float(text.split(": ")[1])
    return output

def main():
    """createe instance of driver and scrape a dynamic value"""
    driver = initiate_driver()
    # pause script to allow dynamic value to load
    t.sleep(2)
    element = driver.find_element(by = "xpath", value = "/html/body/div[1]/div/h1[2]")
    return get_temperature_from_text(element.text)

if __name__ == "__main__":
    print(main())