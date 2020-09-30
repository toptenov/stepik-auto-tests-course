import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en", help="Choose language: ar, ca, cs, da, de, en, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	browser = webdriver.Chrome(options=options)
	print("\nstart chrome browser for test..")
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.fixture()
def language(request):
	lang = request.config.getoption("language")
	return lang