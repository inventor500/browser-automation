#!/usr/bin/python3
# Isaac Ganoung
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
email = input("Enter your email: ")
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
driver.get("https://www.signupgenius.com/go/10c0d4fafaf2ba7ffc07-vespers")
WebDriverWait(driver, 8).until(ec.presence_of_element_located((By.ID, 'checkbox779317799')))
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.ID, 'checkbox779317799').click()
driver.find_element(By.CLASS_NAME, "giantsubmitbutton.rounded.link_cursor").click()
WebDriverWait(driver, 12).until(ec.presence_of_element_located((By.ID, 'firstname')))
driver.find_element(By.ID, 'firstname').send_keys(firstname + Keys.TAB)
driver.switch_to.active_element.send_keys(lastname + Keys.TAB)
driver.switch_to.active_element.send_keys(email)
confirmation = input("Do you wish to send this sign-up request? [y/n]: ")
if (confirmation[0]=='y' or confirmation[0]=='Y'):
        driver.find_element(By.NAME, 'btnSignUp').click()
        print("Submitted sign-up. Check your email for confirmation.")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.quit()
