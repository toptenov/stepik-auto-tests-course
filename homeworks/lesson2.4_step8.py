from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Функция с уравнением
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Open link
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# Дождаться цены 100$ и нажать кнопку
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	buttonBook = browser.find_element_by_id("book")
	browser.execute_script("return arguments[0].scrollIntoView(true);", buttonBook)
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	buttonBook.click()
	print (buttonBook)
	time.sleep(1)

	# Посчитать уравнение
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	#Fill input with correct answer
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)

	# Нажать на кнопку
	pressButton = browser.find_element_by_css_selector("#solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", pressButton)
	time.sleep(1)
	pressButton.click()

finally:
	# Ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(5)
	# Закрываем браузер после всех манипуляций
	browser.quit()

