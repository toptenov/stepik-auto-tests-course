from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
  z = int(x) + int(y)
  return str(z)

try:
  link = "http://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element_by_id("num1")
  x = x_element.text
  y_element = browser.find_element_by_id("num2")
  y = y_element.text
  z = calc(x, y)
  # Просто печатаем ответ в консоль, чтобы убедится, что считается правильно
  print(z)
  
  # ищем элемент с цифрой равной сумме
  select = Select(browser.find_element_by_tag_name("select"))
  select.select_by_value(z)

  # Отправляем заполненную форму
  button = browser.find_element_by_css_selector("button")
  button.click()

  # Проверяем, что смогли зарегистрироваться
  # ждем загрузки страницы
  time.sleep(2)

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()

