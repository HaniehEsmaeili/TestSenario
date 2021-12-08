from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get('https://www.digikala.com')

login_account = driver.find_element_by_xpath("//a[@class='c-header__btn-login o-tooltip']")
login_account.click()

try:
    enter_info= driver.find_element_by_name('login[email_phone]')
    enter_info.send_keys("hanieesmaeili324@gmail.com")
except ElementNotInteractableException:
    print("Incorrect Information")
    
        

enter=driver.find_element_by_xpath("//button[contains(@class,'o-btn o-btn--contained-red-lg')]")
enter.click()


try:
    enter_password= driver.find_element_by_id("")
    enter_password.send_keys("889900Mt")
except ElementNotInteractableException:
    print("Incorrect Information")



continueing=driver.find_element_by_xpath("//button[contains(@class,'o-btn o-btn--full-width')]")
continueing.click()

observing_info= driver.find_element_by_xpath("//a[@class='c-header__btn-profile js-dropdown-toggle']")
observing_info.click()

time.sleep(5)
driver.quit()