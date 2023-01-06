from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime
import concurrent.futures as threading
import time
import random
import os

class Scalper:
    def __init__(self, websites, products):
        self.websites = websites
        self.products = []
        self.driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), "chromedriver")) 
        for url in products:
            self.products.append( Product(url) )

    def _begin_human_setup(self):
        for website in self.websites:
            self.driver.execute_script("window.open('" + website + "');")
        input("Login to websites, open shopping carts, then press any key to continue:")

    def scalp(self):
        self._begin_human_setup()
        while True:
            time.sleep( random.randrange(1, 6) )
            t0 = time.time()
            in_cart_ready = False
            try:
                with threading.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(product.is_available) for product in self.products]
                    threading.wait(futures)
                for product in self.products:
                    if product.available:
                        in_cart_ready = product.add_to_cart(self.driver)
            except Exception as e:
                print(e)
            print("Product search time:", time.time()-t0)
            print("Current datetime:", datetime.now())
            #if in_cart_ready:
            #    playsound( os.path.join(os.getcwd(), "Ain't_No_Rest_For_The_Wicked.mp3") )

class Product:
    def __init__(self, url):
        self.url = url
        self.available = False
    
    def is_available(self):
        time.sleep( random.randrange(3, 16) )
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0"
        headers = {'User-Agent': user_agent}
        response = requests.get(self.url, headers=headers)
        print("Product ping response status_code:", response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        buttons = soup.find_all("button")
        self.available = False
        for button in buttons:
            if button.text.lower().strip() == "add to cart": 
                self.available = True
    
    def add_to_cart(self, driver):
        driver.get(self.url)
        buttons = driver.find_elements_by_tag_name("button")
        success = False
        for button in buttons:
            if button.text.lower().strip() == "add to cart":
                button.click()
                print("Product added to cart:", self.url)
                playsound( os.path.join(os.getcwd(), "notify.mp3") )
                success = True
        return success

def main():

    websites = ["https://www.bestbuy.com", "https://www.newegg.com"]
    products = []
    with open("products.txt") as fin:
        for line in fin.readlines():
            products.append( line.strip() )
    scalper = Scalper(websites, products)
    scalper.scalp()

if __name__ == "__main__":
    main()
