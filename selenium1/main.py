from selenium import webdriver

chrome_drive_path = "G:\Some useful Sofwares\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("https://www.python.org/")

dict = {}
events = [i.text for i in  driver.find_elements_by_css_selector('.event-widget  .shrubbery .menu li a')]
year = [i.text for i in  driver.find_elements_by_css_selector('.event-widget  .shrubbery .menu time')]
for i in range(5):
    dict[year[i]] = events[i]

print(dict)
driver.close()