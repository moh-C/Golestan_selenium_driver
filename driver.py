from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(
    executable_path="C:\\Users\\Aaron\\Desktop\\Webdriver\\chromedriver.exe")

# driver.maximize_window()
driver.get("https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")

seq = driver.find_elements_by_tag_name('iframe')

print("No of frames present in the web page are: ", len(seq))

driver.quit()
