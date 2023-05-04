"""gives access to certain keyboard keys"""
from selenium.webdriver.common.keys import Keys as k
import create_driver as cd


def login(driver):
    """login"""  
    driver.find_element(by="id", value="id_username").send_keys("automated")
    cd.t.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automated"*2 + k.RETURN)
    print(driver.current_url)

    click_link(driver, "/html/body/nav/div/a")

def click_link(driver, xpath):
    """click home hyperlink"""
    driver.find_element(by="xpath", value=xpath).click()
    print(driver.current_url)


    