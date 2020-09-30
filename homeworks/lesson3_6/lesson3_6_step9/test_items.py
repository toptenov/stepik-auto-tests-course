import time
from selenium import webdriver

def test_basket(browser, language):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	# time.sleep(1)
	if (str(language) == "ar"):
		button = browser.find_element_by_xpath("//button[text()='أضف الى سلة التسوق']").text
		assert button == "أضف الى سلة التسوق", f"Button name is {button}"

	elif (str(language) == "ca"):
		button = browser.find_element_by_xpath("//button[text()='Afegeix a la cistella']").text
		assert button == "Afegeix a la cistella", f"Button name is {button}"

	elif (str(language) == "cs"):
		button = browser.find_element_by_xpath("//button[text()='Vložit do košíku']").text
		assert button == "Vložit do košíku", f"Button name is {button}"

	elif (str(language) == "da"):
		button = browser.find_element_by_xpath("//button[text()='Læg i kurv']").text
		assert button == "Læg i kurv", f"Button name is {button}"
		
	elif (str(language) == "de"):
		button = browser.find_element_by_xpath("//button[text()='In Warenkorb legen']").text
		assert button == "In Warenkorb legen", f"Button name is {button}"
		
	elif (str(language) == "en"):
		button = browser.find_element_by_xpath("//button[text()='Add to basket']").text
		assert button == "Add to basket", f"Button name is {button}"
		
	elif (str(language) == "el"):
		button = browser.find_element_by_xpath("//button[text()='Προσθήκη στο καλάθι']").text
		assert button == "Προσθήκη στο καλάθι", f"Button name is {button}"
		
	elif (str(language) == "es"):
		button = browser.find_element_by_xpath("//button[text()='Añadir al carrito']").text
		assert button == "Añadir al carrito", f"Button name is {button}"
		
	elif (str(language) == "fi"):
		button = browser.find_element_by_xpath("//button[text()='Lisää koriin']").text
		assert button == "Lisää koriin", f"Button name is {button}"
		
	elif (str(language) == "fr"):
		button = browser.find_element_by_xpath("//button[text()='Ajouter au panier']").text
		assert button == "Ajouter au panier", f"Button name is {button}"
		
	elif (str(language) == "it"):
		button = browser.find_element_by_xpath("//button[text()='Aggiungi al carrello']").text
		assert button == "Aggiungi al carrello", f"Button name is {button}"
		
	elif (str(language) == "ko"):
		button = browser.find_element_by_xpath("//button[text()='장바구니 담기']").text
		assert button == "장바구니 담기", f"Button name is {button}"
		
	elif (str(language) == "nl"):
		button = browser.find_element_by_xpath("//button[text()='Voeg aan winkelmand toe']").text
		assert button == "Voeg aan winkelmand toe", f"Button name is {button}"
		
	elif (str(language) == "pl"):
		button = browser.find_element_by_xpath("//button[text()='Dodaj do koszyka']").text
		assert button == "Dodaj do koszyka", f"Button name is {button}"
		
	elif (str(language) == "pt"):
		button = browser.find_element_by_xpath("//button[text()='Adicionar ao carrinho']").text
		assert button == "Adicionar ao carrinho", f"Button name is {button}"
		
	elif (str(language) == "pt-br"):
		button = browser.find_element_by_xpath("//button[text()='Adicionar à cesta']").text
		assert button == "Adicionar à cesta", f"Button name is {button}"
		
	elif (str(language) == "ro"):
		button = browser.find_element_by_xpath("//button[text()='Adauga in cos']").text
		assert button == "Adauga in cos", f"Button name is {button}"
		
	elif (str(language) == "ru"):
		button = browser.find_element_by_xpath("//button[text()='Добавить в корзину']").text
		assert button == "Добавить в корзину", f"Button name is {button}"
		
	elif (str(language) == "sk"):
		button = browser.find_element_by_xpath("//button[text()='Pridať do košíka']").text
		assert button == "Pridať do košíka", f"Button name is {button}"
		
	elif (str(language) == "uk"):
		button = browser.find_element_by_xpath("//button[text()='Додати в кошик']").text
		assert button == "Додати в кошик", f"Button name is {button}"
		
	elif (str(language) == "zh-cn"):
		button = browser.find_element_by_xpath("//button[text()='Add to basket']").text
		assert button == "Add to basket", f"Button name is {button}"