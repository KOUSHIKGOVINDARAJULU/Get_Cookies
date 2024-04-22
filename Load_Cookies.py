import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    browser = uc.Chrome()
    browser.get('https://github.com/login')

    # Open the text file and read its contents
    with open("cookies.txt", "r") as file:
        cookies_data = file.read()

    # Convert the text data into a list of dictionaries
    cookies = []
    with open("cookies.txt", "r") as file:
        for line in file:
            # Split the line into attributes
            attributes = line.strip().split("\t")
            
            # Construct a dictionary for the cookie
            cookie_line = {
                "name": attributes[0],
                "value": attributes[1],
                "domain": attributes[2],
                "path": attributes[3],
                "expiration": attributes[4],
                "size": attributes[5],
                "http_only": attributes[6],
                "secure": attributes[7],
                "same_site": attributes[8],
                "priority": attributes[9]
            }
            
            cookies.append(cookie_line)
    # Set the domain for each cookie
    for cookie in cookies:
        cookie['domain'] = ".github.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)

    browser.get('https://github.com/KOUSHIKGOVINDARAJULU/PortfolioSite')

    time.sleep(120)
