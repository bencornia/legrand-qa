from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(url, username, password):
    # Set up Chrome Driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, service=Service("C:/SeleniumDrivers/chromedriver.exe"))
    wait = WebDriverWait(driver, 10)

    # Go to page for testing
    driver.get(url)

    # Maximize window
    driver.maximize_window()

    # Find the login
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login2"]'))).click()

    # Enter username
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginusername"]'))).send_keys(username)

    # Enter password
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginpassword"]'))).send_keys(password)

    # Click Login
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))).click()

    # Return welcome text
    message_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nameofuser"]'))).text
    driver.close()
    driver.quit()
    return message_text


