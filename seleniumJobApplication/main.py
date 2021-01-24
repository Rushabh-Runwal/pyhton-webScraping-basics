import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

driver = webdriver.Chrome(executable_path="G:\Some useful Sofwares\Development\chromedriver.exe")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")



id = '+91 7447312272'
password = ""

username_input = driver.find_element_by_id("username")
username_input.send_keys(id)
password_input = driver.find_element_by_id('password')
password_input.send_keys(password)

submit_button = driver.find_element_by_class_name('btn__primary--large')
submit_button.click()


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2330879467&f_LF=f_AL&geoId=92000001&keywords=python%20developer&location=Remote")
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print(listing)
    listing.click()
    time.sleep(2)
    try:
        easy_apply = driver.find_element_by_class_name('jobs-apply-button')
        easy_apply.click()
        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        pass


time.sleep(5)
driver.quit()