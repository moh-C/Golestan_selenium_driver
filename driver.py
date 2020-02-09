from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Aaron\\Desktop\\Webdriver\\chromedriver.exe")

driver.get("https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")

iframes = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(iframes[0])
sleep(2)
driver.switch_to.frame("Master")
sleep(2)
driver.switch_to.frame("Form_Body")
sleep(2)
print(driver.page_source)
print('\n\n')


driver.quit()
