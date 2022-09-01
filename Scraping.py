from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
import os

import chromedriver_binary


def report(loginid, password):
    
    options = Options()
    options.add_argument('--headless');
    
    path = "https://github.com/kibagon7/temperature_report/blob/89d6670d236adc824894b919d66c81ff767f00ea/chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path=path, options = options)
    sleep(3)

    driver.get("https://lib02.tmd.ac.jp/webclass/login.php")

    #ログイン
    driver.find_element_by_id("username").send_keys(loginid)

    driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_id("LoginBtn").click()

    sleep(1)

    #M5 臨床実習関係
    driver.get("https://lib02.tmd.ac.jp/webclass/course.php/11100202200FMS04100/?acs_=4abbf83e")

    sleep(1)

    #体温体調報告
    driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div/div[1]/div/section[1]/div[2]/section[1]/div/div[1]/h4/a").click()

    sleep(1)

    #開始
    driver.get("https://lib02.tmd.ac.jp/webclass/show_info.php?set_contents_id=bcb0dfd3bd86a9821b767f8fd88bdd58&language=JAPANESE&rnd=7023b&content_mode=i")

    driver.find_element_by_name("next").click()

    sleep(1)

    driver.get("https://lib02.tmd.ac.jp/webclass/dqstn_answer_all.php?rnd=35e2a&set_contents_id=bcb0dfd3bd86a9821b767f8fd88bdd58&language=JAPANESE&content_mode=i&start_from_show_info=true&content_mode=q&acs_=b880ed03")


    #設問1
    dropdown1 = driver.find_element_by_name("dropdown__1[]")
    select = Select(dropdown1) 
    select.select_by_index(1)

    #設問2
    dropdown2 = driver.find_element_by_name("dropdown__2[]")
    select = Select(dropdown2) 
    select.select_by_index(1)

    #設問3
    driver.find_element_by_name("radio__3").click()

    #設問4
    driver.find_element_by_name("checkbox__4[]").click()

    #設問5
    driver.find_element_by_name("radio__5").click()

    sleep(1)

    #終了
    driver.find_element_by_id("GradeBtn").click()

    #終了
    driver.execute_script("gradeAndClose()")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    