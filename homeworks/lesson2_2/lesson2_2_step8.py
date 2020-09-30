from selenium import webdriver
import time
import os

try:
    # Открыть страницу по ссылке
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivan")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Ivan")

    # Загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    browser.find_element_by_name("file").send_keys(file_path)
    
    # Проскроллить страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

