import pytest
from selenium import webdriver

def test_find_add_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")) > 0, 'нет кнопки добавления в корзину'

