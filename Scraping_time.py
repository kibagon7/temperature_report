from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
from datetime import datetime, date
import os

def report_time(loginid, password):
    
    options = Options()
    options.add_argument('--headless');
    
    
    
    driver = webdriver.Chrome(options = options)
    sleep(3)

    driver.get("https://lib02.tmd.ac.jp/webclass/login.php")
    
    #ログイン
    driver.find_element_by_id("username").send_keys(loginid)

    driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_id("LoginBtn").click()

    sleep(1)

    #M5 医学教務係からのお知らせ
    driver.get("https://lib02.tmd.ac.jp/webclass/course.php/11100202200FMS04100/?acs_=4abbf83e")

    sleep(1)

    driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div/div[1]/div/section[1]/div[2]/section[1]/div/div[2]/div/div[1]/div/a").click()

    sleep(2)

    driver.find_element_by_xpath("/html/body/main/div/ul/li[2]/a").click()

    sleep(2)

    driver.find_element_by_xpath("/html/body/main/div/div/table/tbody/tr[1]/td[2]/a").click()

    sleep(1)

    time = driver.find_element_by_xpath("/html/body/div[1]/div[2]/h3/div[2]").text

    time = datetime.strptime(time, "%Y-%m-%d")
    
    today = date.today()
    
    if time.day == today.day:
        return 1
    else:
        return 0
    
    
    
    
    
    