from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Aaron\\Desktop\\Webdriver\\chromedriver.exe")

driver.get("https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")

seq = driver.find_elements_by_tag_name('iframe')
print("No of frames present in the web page are: ", len(seq))
# switching between the iframes based on index
for index in range(len(seq)):
    driver.switch_to.default_content
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(30)
    driver.save_screenshot("screenshot.png")
    # highlight the contents of the selected iframe
    something = driver.find_element_by_tag_name('frame')
    print(something)

driver.switch_to.default_content

driver.quit()
