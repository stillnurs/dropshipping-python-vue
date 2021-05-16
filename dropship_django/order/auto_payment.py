import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



from order.views import ClientData


class Payment:

    def __init__(self, url):
        self.url = url

    
    def get_data(self):
        options = Options()
        options.page_load_strategy = 'normal'
        driver = Chrome(options=options)
        driver.get(self.url)


        first_login_input = driver.find_element_by_xpath('//*[@id="__next"]/div/header/div[1]/div[2]/div[3]/div/button')
        email_input = driver.find_element_by_xpath('//*[@id="emailInput"]')
        pass_input = driver.find_element_by_xpath('//*[@id="passwordInput"]')
        order_item_click = driver.find_element_by_xpath('//*[@id="productBox-N41247213A"]/div')
        add_one_to_cart_click = driver.find_element_by_xpath('//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div')
        cart_detail_click = driver.find_element_by_xpath('//*[@id="__next"]/div/header/div[1]/div[2]/a[2]/span')
        cart_checkout_click = driver.find_element_by_xpath('//*[@id="__next"]/div/section/div/div/div[2]/div/div[1]/div[3]/button/span')
        address_search_input = driver.find_element_by_xpath('//*[@id="searchBox"]')
        confirm_location_click = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[4]/div[3]/div[1]/button')
        address_detail_input = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/form/div[1]/div[1]/div[3]/div/div/div/input')
        phone_number_code_select = Select(driver.find_element_by_xpath('//*[@id="react-select-2--value-item"]'))
        phone_number_code_select.select.select_by_value('phone code')
        phone_number_input = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/form/div[1]/div[2]/div[1]/div/div[2]/div/div/input')
        first_name_input = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/form/div[1]/div[2]/div[2]/div/div/div/input')
        last_name_input = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/form/div[1]/div[2]/div[3]/div/div/div/input')
        save_address_click = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/form/div[2]/div[2]/button')
        
