from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to GeckoDriver executable
geckodriver_path = 'C:/geckodriver.exe'

# Create Firefox WebDriver
driver = webdriver.Firefox(executable_path=geckodriver_path)
options = FireoxOptions()
options.addArguments(user"C:\Users\lukel\AppData\Local\Mozilla\Firefox\Profiles\szpdxt9g.default")
# Load a webpage
driver.get("https://chat.openai.com")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

cookies = driver.get_cookies()
print(cookies)

with open("cookies.txt", "w") as f:
    f.write(cookies)

print("Fin")
# for cookie in cookies:
#     driver.add_cookie(cookie)


