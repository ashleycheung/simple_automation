'''
This program is written by Ashley Cheung
12/9/2018

This is a very simple program that opens a browser and logs in to your facebook account for you
It requires you to have the chromedriver for selenium installed
'''


chromedriver_location = r"C:\Users\Username\location_of_chrome_driver"
user_email = "myemail@gmail.com"
user_password = "mypassword"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(chromedriver_location);
browser.implicitly_wait(20);
browser.get("https://facebook.com");

email = browser.find_element_by_id('email');
email.send_keys(user_email);

password = browser.find_element_by_id('pass');
password.send_keys(user_password);

login_button = browser.find_element_by_id('u_0_2');
login_button.click();
