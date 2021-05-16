from django.conf import settings
from django.db import transaction

import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine

from product.models import Product, Category



class Scraper():

    def __init__(self, url):
        self.url = url

    
    def get_data(self):
        options = Options()
        options.page_load_strategy = 'normal'
        browser = webdriver.Chrome(options=options)
        browser.get(self.url)
        
        # marking the "html" anchor for scrolling the page
        html = browser.find_element_by_tag_name('html')
        i = 0
        while i<11:
            time.sleep(1)
            html.send_keys(Keys.PAGE_DOWN)
            i+=1
        
        names = browser.find_elements_by_xpath("//*[starts-with(@class, 'kcs0h5-0 diNcmV grid')]")
        prices = browser.find_elements_by_xpath("//*[starts-with(@data-qa, 'productPrice')]")
        image_links = browser.find_elements_by_xpath('//*[starts-with(@class, "productImage")]//img')
        product_links = browser.find_elements_by_xpath("//*[starts-with(@class, 'productContainer')]//a")
        
        # add product data to data dict
        data = {}
        data['category_id'] = '1'
        try:
            data['name'] = [i.get_attribute('title') for i in names]
            data['slug'] = [i.get_attribute('title').strip().replace(' ', '-') for i in names]
        except Exception as e:
            data['name'] = '-name not found-'
        try:
            data['price'] = [float(i.text) for i in prices]
        except Exception as e:
            data['price'] = '-price not found-'
        try:
            data['link'] = [i.get_attribute('href').strip() for i in product_links]
        except Exception as e:
            data['link'] = '-link not found-'
        try:    
            data['image_link'] = [i.get_attribute('src').strip() for i in image_links]
        except Exception as e:
            data['image_link'] = '-image link not found-'

        # closing browser
        browser.quit()

        # creating a dataframe with Pandas
        dataframe = pd.DataFrame(data)

        print(f"=====>{len(data['name'])}")
        print(f"=====>{len(data['slug'])}")
        print(f"=====>{len(data['price'])}")
        print(f"=====>{len(data['link'])}")
        print(f"=====>{len(data['image_link'])}")
        
        return dataframe



    def run(self):
        user = settings.DATABASES['default']['USER']
        passwd = settings.DATABASES['default']['PASSWORD']
        dbname = settings.DATABASES['default']['NAME']
        
        conn = 'postgresql://{user}:{passwd}@localhost:5432/{dbname}'.format(
        user=user,
        passwd=passwd,
        dbname=dbname
        )

        connection = create_engine(conn, echo=False)
        dataframe = self.get_data()
        # dataframe['id'] = dataframe.index + 1
        # dataframe.to_csv('/hdd/sda1/Desktop/My_projects/dropshipping-python-vue/dropship_django/productDetails.csv')
        
        dataframe.to_sql('products', connection, if_exists='append', index=False, method="multi")


