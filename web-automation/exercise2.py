import create_driver as cd
import values as v
from datetime import datetime as dt

def write_txt(text):
    file_name = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(text)

def main():
    driver = cd.initiate_driver(v.URL2)
    while True:
        cd.t.sleep(2)
        element = driver.find_element(by = "xpath", value = "/html/body/div[1]/div/h1[2]")
        text = str(cd.get_temperature_from_text(element.text))
        write_txt(text)

if __name__ == "__main__":
    main()
