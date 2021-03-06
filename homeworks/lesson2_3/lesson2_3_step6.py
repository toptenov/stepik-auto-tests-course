from selenium import webdriver
import time
import math

# Функция с уравнением
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Нажать на кнопку
	pressButton = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
	pressButton.click()

	# Переключиться на вторую вкладку
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	print (new_window)

	# Посчитать уравнение
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	# Ввести ответ
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
  
	# Проскроллить страницу вниз и нажать на кнопку Submit
	button = browser.find_element_by_css_selector("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

finally:
	# Ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(5)
	# Закрываем браузер после всех манипуляций
	browser.quit()

