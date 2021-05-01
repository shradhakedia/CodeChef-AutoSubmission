from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to hit enter
from selenium.webdriver.common.alert import Alert
import time


#  firstly you need to choose path as chromedriver that you installed
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# driver.get helps you to search/automate through the given website as its field
driver.get('https://www.codechef.com/')

# finding the username, password input button by its id from CC page 
user_name = driver.find_element_by_id("edit-name")
password = driver.find_element_by_id("edit-pass")

#sending your username and password
user_name.send_keys("User_name")
password.send_keys("Password")

# for hitting enter
password.send_keys(Keys.RETURN)

time.sleep(2)
# loading the question page, update the link accordingly
driver.get("https://www.codechef.com/submit/HP18")

# finding the div of language selector
select = driver.find_element_by_class_name("language_selector")

# clicking it 
select.click()

# finding input button and input your preferred programming language
select = driver.find_element_by_xpath("//div[@class='chosen-search']//input")
select.send_keys("python") #put your preferred laguage here
 
# to hit enter
select.send_keys(Keys.RETURN)

time.sleep(5)

# to delete the already written code
text_area = driver.find_element_by_class_name("ace_text-input")
text_area.send_keys(Keys.CONTROL + "a")
text_area.send_keys(Keys.DELETE)

# goto settings on CC page and uncheck the autocomplete checkbox mannualy
f = open("solution.py")
for code in f:
    text_area.send_keys(code)
    text_area.send_keys(Keys.HOME)
f.close 
time.sleep(2)


buttons=driver.find_elements_by_class_name("ns-button")
# print(buttons)
buttons[2].click()


alert = Alert(driver)
  
# accept the alert
alert.accept()

# driver.quit()
