from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from urllib.request import urlretrieve

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Aaron\\Desktop\\Webdriver\\chromedriver.exe")

driver.get("https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")
driver.maximize_window()

myUsername = "97242042"
myPassword = "00"

iframes = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(iframes[0])
sleep(2)
driver.switch_to.frame("Master")
sleep(2)
driver.switch_to.frame("Form_Body")
sleep(2)

username = driver.find_elements_by_id('F80351')[0]
password = driver.find_elements_by_id('F80401')[0]
btn = driver.find_elements_by_id('btnLog')[0]

username.send_keys(myUsername)
password.send_keys(myPassword)
btn.click()
sleep(10)

btn.click()

sleep(10)

print(driver.page_source)

driver.quit()
