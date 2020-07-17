from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

class PortalsData:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
    
    def get_teacher_list(self):
        options = Options()
        options.headless = True
        
        driver = webdriver.Firefox(options=options)
        driver.get('https://www.plusportals.com/sjhs')

        username_element = driver.find_element_by_id('UserName')
        password_element = driver.find_element_by_id('Password')

        username_element.send_keys(self.username)
        password_element.send_keys(self.password)

        driver.find_element_by_name('btnsumit').click()

        time.sleep(6)

        driver.find_element_by_xpath('//*[@id="top"]/nav/div/div/div/div/div/ul/li[5]/a').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="tabstripCommunication"]/ul/li[2]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="btnNewMessage"]').click()
        time.sleep(1)

        teacher_table = driver.find_element_by_xpath('//*[@id="gridMsgRecipient"]/div[2]/table/tbody')
        teacher_list = teacher_table.text.split('\n')
        driver.close()
        return teacher_list