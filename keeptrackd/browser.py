from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

from keeptrackd import (
        config
        )


class Browser:
    def __init__(self):
        options = Options()
        options.binary_location = config.get('chrome_binary_location')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def __del__(self):
        self.driver.quit()

    def get(self, url):
        self.driver.get(url)

    def wait_for(self, css_selector):
        elem = WebDriverWait(self.driver).until(lambda d: d.find_element_by_css_selector(css_selector))
        return elem

    def page_source(self):
        return self.driver.page_source

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def find_element_by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def find_element_by_id(self, id_):
        return self.driver.find_element_by_id(id_)