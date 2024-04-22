import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    email = "Your_Email"
    password = "Your_Password"

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(
        options=options,
    )
    browser.get('https://github.com/login')

    browser.find_element(By.ID, 'login_field').send_keys(email)

    password_selector = "#password"

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    browser.find_element(
        By.CSS_SELECTOR, password_selector).send_keys(password)
    
    browser.find_element(
        By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button').click()
    time.sleep(5)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))
