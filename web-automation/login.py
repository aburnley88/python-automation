import create_driver as cd
from selenium.webdriver.common.keys import Keys as k

def main():
    URL = "https://automated.pythonanywhere.com/login/"
    driver = cd.initiate_driver(URL)
    driver.find_element(by="id", value="id_username").send_keys("automated")
    cd.t.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automated"*2 + k.RETURN)
    print(driver.current_url)

    click_link(driver, "/html/body/nav/div/a")

def click_link(driver, xpath):
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)

if __name__ == "__main__":
    print(main())
    