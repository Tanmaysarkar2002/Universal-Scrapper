import logging
from autoscraper import AutoScraper
import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
import re

def get_specific_data(url, wanted_list):
    scraper = AutoScraper()
    result = None
    try:
        print(scraper.build(url, wanted_list))
        result = scraper.get_result_similar(url, grouped=True)
    except Exception as e:
        logging.error(f"An error occurred while scraping {url}: {e}")
    return result

logging.basicConfig(level=logging.INFO)
main_url = "https://stackoverflow.com/questions/tagged/dsa"
wanted_list = ["Generate DSA Keys for OpenSSH in Golang"]


def get_filename_from_url(url):
    return re.sub(r'\W+', '_', url)

def download_images_from_site(driver, url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url and img_url.startswith('http'):
            img_name = get_filename_from_url(img_url)
            print(img_name)
            download_image(img_url, img_name)
        break
def download_image(img_url, filename):
    # Add .jpg extension if filename doesn't have an extension
    _, ext = os.path.splitext(filename)
    if not ext:
        filename += '.jpg'

    response = requests.get(img_url, stream=True)
    if response.status_code == 200:
        print(f"Downloading image: {filename}")
        with open(filename, 'wb') as out_file:
            out_file.write(response.content)
    else:
        print(f"Unable to download image. HTTP response code: {response.status_code}")

driver = webdriver.Chrome()  # or webdriver.Chrome(), etc.

# URL of the website you want to scrape images from
url = "https://unsplash.com/s/photos/sample"

# Call the function to download images
download_images_from_site(driver, url)

# Close the WebDriver instance
driver.quit()