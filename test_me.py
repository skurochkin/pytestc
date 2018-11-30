from selenium import webdriver

def test_quest():
    a = "test"
    b = "quest"
    assert a == b

def test_to_pass():
    a = "test"
    b = "test"
    assert a == b

def test_selenium():
    browser = webdriver.Chrome()
    browser.get("https://google.com")