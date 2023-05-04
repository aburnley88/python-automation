import create_driver as cd
import login as ln
import values as v

def main():
    driver = cd.initiate_driver(v.URL)
    ln.login(driver)
    val = cd.scrape_dynamic(driver)
    return val

if __name__ == "__main__":
    print(main())