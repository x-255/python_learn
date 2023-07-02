import pickle
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from os.path import exists


def rush():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    # 禁用 初始打印日志，自动化栏
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging', 'enable-automation'])
    # 屏蔽保存密码提示框
    options.add_experimental_option('prefs',
                                    {'credientials_enable_service': False, 'profile.password_manager_enabled': False})
    # 反爬虫特征处理
    options.add_argument('--disable-blink-features=AutomationControlled')

    wd = webdriver.Chrome(options=options)
    wd.maximize_window()

    login(wd)
    run(wd)
    wd.quit()


def login(wd: WebDriver):
    wd.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
    cachefile = 'cookies.pkl'

    _login = None
    if exists(cachefile):
        _login = login_by_cookies

    else:
        _login = login_by_action

    _login(wd, cachefile)


def login_by_cookies(wd: WebDriver, cachefile):
    with open(cachefile, 'rb') as file:
        for cookie in pickle.load(file):
            wd.add_cookie({
                'domain': '.damai.cn',
                'name': cookie['name'],
                'value': cookie['value']
            })


def login_by_action(wd: WebDriver, cachefile):
    wd.switch_to.frame('alibaba-login-box')
    ActionChains(wd).click(wd.find_element(
        By.CSS_SELECTOR, '.login-tabs-tab:last-child')).perform()
    wd.find_element(By.ID, 'fm-login-id').send_keys('17788886666')
    wd.find_element(By.ID, 'fm-login-password').send_keys('123321')

    sleep(10)
    with open(cachefile, 'wb') as file:
        cookies = wd.get_cookies()
        pickle.dump(cookies, file)


def run(wd: WebDriver):
    wd.get('https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.41354d15Nx8oHO&id=725478339651&clicktitle=%E3%80%8A%E5%85%89%E8%BE%89%E5%B2%81%E6%9C%88%E2%80%94%E8%87%B4%E6%95%ACBeyond%E9%87%91%E6%9B%B2%E6%BC%94%E5%94%B1%E4%BC%9A%E3%80%8B')


rush()
