from selenium import webdriver
import unittest
import time

def link_t(link):
	# Открываем ссылку
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # Определяем название вкладки
    tab_name = browser.window_handles[0]

    # Возвращаем текст из элемента welcome_text_elt и название вкладки, чтобы потом её закрыть
    return welcome_text, browser

class TestAbs(unittest.TestCase):
	def test_1(self):
	    welcome_text1, browser1 = link_t("http://suninjuly.github.io/registration1.html")

	    # закрываем браузер после всех манипуляций
	    browser1.quit()

	    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	    self.assertEqual(str(welcome_text1), "Congratulations! You have successfully registered!", "1st test went wrong")

	def test_2(self):
	    welcome_text1, browser1 = link_t("http://suninjuly.github.io/registration2.html")

	    # закрываем браузер после всех манипуляций
	    browser1.quit()

	    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	    self.assertEqual(str(welcome_text1), "Congratulations! You have successfully registered!", "2nd test went wrong")

if __name__ == "__main__":
    unittest.main()