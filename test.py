from selenium import webdriver

wd = webdriver.Chrome()

wd.get('https://cart.taobao.com/cart.htm?from=btop')

wd.quit()
