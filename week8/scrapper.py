import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


base_url = "https://www.komplett.dk/category/21064/mobil/mobiltelefoner"
profile = webdriver.FirefoxProfile()
profile.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
)

# headless would be needed here if we did not have a GUI version of firefox
options = Options()
options.headless = True
# driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
browser = webdriver.Firefox(options=options)

browser.get(base_url)
browser.implicitly_wait(3)

cellphones = []


def get_cellphones():
    """ clicks on cookie buttons and reads all product elements"""

    """Pagaes loads dynamicly, so ve should scrall to the bottom and read current url insted of using the one belov (?)"""

    url = (
        "https://www.komplett.dk/category/21064/mobil/?nlevel=10444%C2%A721064&hits=192"
    )
    try:
        cookie_button = browser.find_element_by_css_selector("button.btn-large.primary")
        # print('Cookie Button', cookie_button)
        try:
            cookie_button.click()
            sleep(3)
        except Exception as ex:
            print(ex)
    except Exception as e:
        print("BUTTON EXCEPTION", e)

    # span.product-price-now

    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, "html.parser")

    results = soup.select(".content-block")
    print(len(results))

    for mobile in results:
        read_mobile_details(mobile)

    print("Data scarpped!")


def read_mobile_details(mobile):
    cell_phone = {}

    price = mobile.select(".product-price-now")
    price_string = ""

    for p in price:
        price_string = p.get_text()

    clean_price_str = price_string.split(",")[0].replace(".", "").strip()

    p_list = list(clean_price_str)
    price_final = -1

    if clean_price_str != "":
        price_final = int(clean_price_str)

    cell_phone["price"] = int(price_final)

    _name = "undefined"
    name = mobile.select(".text-content > h2")
    for n in name:
        _name = n.get_text()

    cell_phone["name"] = _name

    cellphones.append(cell_phone)
