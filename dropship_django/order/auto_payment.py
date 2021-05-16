from selenium.webdriver import Chrome
from selenium.webdriver.chrome import Options
from selenium.webdriver.common.keys import Keys


class Payment:

    def __init__(self, url):
        self.url = url

    
    def get_data(self):
        options = Options()
        options.page_load_strategy = 'normal'
        browser = webdriver.Chrome(options=options)
        browser.get(self.url)