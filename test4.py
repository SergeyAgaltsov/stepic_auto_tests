import os
from selenium import webdriver

driver = webdriver.Chrome()
url = "http://suninjuly.github.io/file_input.html"
driver.get(url)
driver.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("1")
driver.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("1")
driver.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("1")
driver.find_element_by_css_selector('[type="file"]').send_keys("C:/Users/RedHillBoy/PycharmProjects/stepic/file.txt")
driver.find_element_by_css_selector('[type="submit"]').click()
