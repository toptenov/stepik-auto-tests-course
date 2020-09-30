import pytest
from selenium import webdriver
import time
import math

# Фикстура для открытия и закрытия окна бразуера
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Параметры, тестовые данные
@pytest.mark.parametrize('par1, par2', [("236895", "95"), ("236896", "96"), ("236897", "97"), ("236898", "98"), ("236899", "99"), ("236903", "03"), ("236904", "04"), ("236905", "05")])
# Тестовый сценарий
def test_guest_should_see_login_link(browser, par1, par2):

	# Открыть ссылку
    link = f"https://stepik.org/lesson/{par1}/step/1"
    browser.get(link)
    time.sleep(3)
    
    # Посчитать формулу
    answer = str(math.log(int(time.time())))

    # Найти форму и вставить в неё ответ
    text_area = browser.find_element_by_css_selector("textarea[data-autogrow]")
    text_area.send_keys(answer)
    time.sleep(1)

    # Найти кнопку и нажать
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    time.sleep(2)

    # Вывести фразу в консоль
    correct = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    print("\n")
    print(correct)

    # Сделать проверку
    assert correct == "Correct!", f"{correct}"