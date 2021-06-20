import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException


def scroll(driver, timeout):
    scroll_pause_time = timeout

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def getHeadlessDriver():
    # headless chrome browser
    opts = webdriver.ChromeOptions()
    opts.headless = False
    # Install Driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    return driver


def scrape(driver, search_url):
    driver.get(search_url)
    scroll(driver, 10)
