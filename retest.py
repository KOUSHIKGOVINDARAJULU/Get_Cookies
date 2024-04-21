from selenium import webdriver
import undetected_chromedriver as uc

if __name__ == '__main__':
    email = "koushikkumar580@gmail.com"
    password = "Saikoushik@123"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    # Use undetected_chromedriver to load the Edge browser
    browser = uc.Chrome()(options=options)

    browser.get('https://github.com/login')

    browser.find_element_by_id('login_field').send_keys(email)

    password_selector = "#password"

    # Wait for the password field to become visible
    password_field = browser.find_element_by_css_selector(password_selector)
    
    password_field.send_keys(password)

    login_button = browser.find_element_by_css_selector('#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button')
    login_button.click()
