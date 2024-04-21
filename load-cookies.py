import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':

    browser = uc.Chrome()
    browser.get('https://github.com/login')

    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
        cookie['domain'] = ".github.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)

    browser.get('https://github.com/KOUSHIKGOVINDARAJULU/PortfolioSite')

    time.sleep(120)