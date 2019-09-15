from selenium import webdriver
import math

driver = webdriver.Chrome()
url = "http://suninjuly.github.io/alert_accept.html"
driver.get(url)
driver.find_element_by_xpath("//button").click()
driver.switch_to.alert.accept()
x = int(driver.find_element_by_id("input_value").text)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver.find_element_by_id("answer").send_keys(calc(x))
driver.find_element_by_css_selector("[type='submit']").click()
