import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

try:
    # Open jobsearch.com
    driver.get("login page url")

    # Find the login link and click on it
    login_link = driver.find_element(By.XPATH, copy the xpath of login button)
    login_link.click()

    # Find the username and password fields, and input login credentials
    username_field = driver.find_element(By.ID, "usernameField")
    password_field = driver.find_element(By.ID, "passwordField")

    # Replace 'your_username' and 'your_password' with your actual jonsearch.com login credentials
    username_field.send_keys("gmail")
    password_field.send_keys("password")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete
    time.sleep(5)

    # Navigate to the resume update page (replace with the actual URL)
    driver.get("resume path url")

    # Locate the file input element and send the file path
    file_input = driver.find_element(By.XPATH, '//*[@id="attachCV"]')
    file_path = '/home/ubuntu/****.pdf'  # Replace with the actual path to your resume file
    file_input.send_keys(file_path)

    # Add a sleep time after sending the file path
    time.sleep(3)  # You can adjust the sleep time as needed

    # Now you can interact with the resume update form, fill in details, and save

finally:
    # Close the browser window
    driver.quit()


 # while runnig the code on ubuntu you need to install selinume-webdrive, chrome-browser, python and virtualenv  