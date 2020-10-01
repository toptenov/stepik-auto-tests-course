import time
from selenium import webdriver

def test_there_is_basket_button(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	time.sleep(3)
	button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
	assert button is not None, f"Button name is {button}"
