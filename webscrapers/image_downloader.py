from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome, ChromeOptions
import time
import undetected_chromedriver as uc

class ImageDownloader:
    def __init__(self):
        
        self.options = ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--headless")
        self.driver = Chrome(options=self.options)
        self.driver.maximize_window()
        time.sleep(5)
        

    def download_image(self, url, path):
        self.driver.get(url)
        time.sleep(5)
        self.driver.save_screenshot(path)
        self.driver.quit()
        print("Image downloaded successfully")


obj =ImageDownloader()
obj.download_image("https://www.google.com", "google.png")


    
