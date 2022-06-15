from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_alert_text(driver):
    # Wait for the alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Get the text of the alert
    alert = driver.switch_to.alert

    return alert.text


def setup_page(url):
    # Set up Chrome Driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, service=Service("C:/SeleniumDrivers/chromedriver.exe"))

    # Go to page for testing
    driver.get(url)

    # Maximize window
    driver.maximize_window()

    return driver


def login(url, username, password, success=True):
    # Setup page
    driver = setup_page(url)        

    # Find the login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login2"]'))).click()

    # Enter username
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginusername"]'))).send_keys(username)

    # Enter password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginpassword"]'))).send_keys(password)

    # Click Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))).click()

    if success:
        # Return welcome text
        message_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nameofuser"]'))).text

        return message_text
    
    # If we are testing a failed login then return the alert message
    return get_alert_text(driver)

def signup(url, username, password):
    # Setup page
    driver = setup_page(url)

    # Find the signup
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin2"]'))).click()
     
    # Enter username
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sign-username"]'))).send_keys(username)

    # Enter password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sign-password"]'))).send_keys(password)

    # Click Sign Up
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]'))).click()

    return get_alert_text(driver)

