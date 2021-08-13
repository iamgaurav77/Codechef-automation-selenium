from selenium import webdriver

browser=webdriver.Chrome()

browser.get("https://codechef.com")

#edit-name here is the id in web page
user_element=browser.find_element_by_id("edit-name")


#enter your codechef username 
user_element.send_keys("superstar77")

pass_element=browser.find_element_by_id("edit-pass")

#importing it for secure password
from getpass import getpass

pass_element.send_keys(getpass("Enter Password : "))

browser.find_element_by_id("edit-submit").click()


#enter the code of the problem
problem=input()

browser.get("https://www.codechef.com/submit/"+problem)

browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

browser.find_element_by_id("edit-program").click()


#you soln for the problem will be saved as soln.cpp
with open("soln.cpp",'r') as f:
    code=f.read()

code_element= browser.find_element_by_id('edit-program')

code_element.send_keys(code)

browser.find_element_by_id('edit-submit-1').click()