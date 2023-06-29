from selenium import webdriver
import pickle

options = webdriver.ChromeOptions
options.add_experimental_option('detach', True)

wd = webdriver.Chrome(options=options)
wd.implicitly_wait(15)


wd.get('https://juejin.cn/')

cookies = wd.get_cookies()
for c in cookies:
    print(c)

wd.quit()