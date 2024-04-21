from selenium import webdriver

# Initialize Selenium webdriver for your default browser


driver = webdriver.Edge()  # or webdriver.Firefox(), webdriver.Edge(), etc. depending on your default browser

# List of websites to visit
websites = ['https://github.com']

# Retrieve cookies for each website
all_cookies = {}
for website in websites:
    driver.get(website)
    cookies = driver.get_cookies()
    all_cookies[website] = cookies

# Print cookies for each website
for website, cookies in all_cookies.items():
    print(f"Cookies for {website}:")
    for cookie in cookies:
        print(cookie)

# Close the browser
driver.quit()
