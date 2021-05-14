from django.conf import settings

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from product.models import Product



class Scraper():

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    
    def get_html(self):
        url = self.url
        headers = self.headers
            
        response = requests.get(url, headers=headers)
        html = response.text
        return html


    def get_data(self):
        options = Options()
        options.page_load_strategy = 'normal'
        browser = webdriver.Chrome(options=options)
        browser.get(self.url)
        
        # marking the "html" anchor for scrolling the page
        html = browser.find_element_by_tag_name('html')
        i = 0
        while i<15:
            time.sleep(1)
            html.send_keys(Keys.PAGE_DOWN)
            i+=1
        
        names = browser.find_elements_by_xpath("//*[starts-with(@class, 'kcs0h5-0 diNcmV grid')]")
        prices = browser.find_elements_by_xpath("//*[starts-with(@data-qa, 'productPrice')]")
        link_list = browser.find_elements_by_xpath('//*[starts-with(@class, "productImage")]//img')
        product_links = browser.find_elements_by_xpath("//*[starts-with(@class, 'productContainer')]//a")
        
        # add product data to data dict
        data = dict()
        try:
            data['name'] = [i.get_attribute('title') for i in names]
        except Exception as e:
            data['name'] = '-name not found-'
        try:
            data['price'] = [i.text for i in prices]
        except Exception as e:
            data['price'] = '-price not found-'
        try:
            data['link'] = [i.get_attribute('href') for i in product_links]
        except Exception as e:
            data['link'] = '-link not found-'
        try:    
            data['image_link'] = [i.get_attribute('src') for i in link_list]
        except Exception as e:
            data['image_link'] = '-image link not found-'

        # closing browser
        browser.quit()

        # creating a dataframe with Pandas
        dataframe = pd.DataFrame(data)

        return dataframe



    def run(self):

        dataframe = self.get_data()
        dataframe.to_csv('dropship_django/productDetails.csv', index=False)




# HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# URL = 'https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905'
# headers = settings.HEADERS
# dataframe = Scraper(URL, HEADERS)
# dataframe.get_data()

# dataframe.write()
