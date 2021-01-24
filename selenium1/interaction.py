from selenium import webdriver
import time

chrome_drive_path = "G:\Some useful Sofwares\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id('cookie')
t = 60  # run while loop of 5 sec 60 times

def buy():
    store = [i for i in driver.find_elements_by_css_selector("#store div")]
    store_grayed = [i for i in driver.find_elements_by_css_selector(".grayed")]
    store[len(store) - len(store_grayed) - 1].click()
    run()


def run():
    global t
    timeout = 5  # [seconds]
    timeout_start = time.time()

    while time.time() < timeout_start + timeout:
        cookie.click()

    t -= 1
    if t == 0:
        cps = driver.find_element_by_id('cps').text
        print(cps)
        driver.close()
    else:
        buy()


if t > 0:
    run()
