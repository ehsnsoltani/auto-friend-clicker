from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import time




# Facebook credentials for Tinder login
facebook_email = ""
facebook_password = ""

# Set up Chrome driver with options
tinder_url = "https://tinder.com/"
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Maximize browser window (optional)
driver.maximize_window()
# Open Tinder website
driver.get(tinder_url)

# Ignore specific exceptions for smoother handling
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
wait = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions)


# Click the "Log In" button on Tinder
wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in"))).click()
time.sleep(3)

# Click the "Log in with Facebook" button
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'))).click()

time.sleep(5)
# Switch to the Facebook login window
tinder_page = driver.window_handles[0]
facebook_popup = driver.window_handles[-1]
driver.switch_to.window(facebook_popup)

# clicking on agree to cookie
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]'))).click()

# filing text input in login page with email and password
wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(facebook_email)
wait.until(EC.visibility_of_element_located((By.ID, "pass"))).send_keys(facebook_password)

# clicking on login button on facebook window
facebook_login_btn = driver.find_element(By.NAME, "login")
facebook_login_btn.click()
# Handle potential Facebook login verification (pause script execution)
input("Please verify your Facebook login on your phone (if applicable) and press Enter to continue.")

time.sleep(3)
# Switch back to the Tinder window
driver.switch_to.window(driver.window_handles[0])


time.sleep(5)
# Accept cookies and location access on Tinder
cookie_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'))).click()

allow_location = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))).click()

allow_notify = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))).click()

# Wait for Tinder profile to load
time.sleep(10)
# Find the "Nope" button to swipe left on profiles
no_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')

# Loop to swipe left on 50 profiles
for round in range(50):
    no_btn.click()

    #wait time between swipes
    time.sleep(3)
