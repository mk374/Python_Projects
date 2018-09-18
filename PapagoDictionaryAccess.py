'''
Created on Sep 17, 2018

@author: minsookim
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re

class PapagoDictionaryAccess:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver= webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = options)
        
    def search_Word_and_Print(self):
        driver = self.driver
        driver.get("https://papago.naver.com/?sk=en&tk=ja")
        element = driver.find_element_by_xpath('//*[@id="txtSource"]')
        word_input = input("Word to translate? ")
        print("Search: " + word_input)
        #elementBtn = driver.find_element_by_xpath('//*[@id="btnTranslate"]')
        #elementBtn.click()
        #time.sleep(1)
        elementBtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div[1]/div[1]/div/div[2]/button')
    
        if(re.search('[a-zA-Z]', word_input) == None):
            elementBtn.click()
            element.send_keys(word_input + "\n")
            time.sleep(1)
            print(driver.find_element_by_xpath('//*[@id="txtTarget"]').text)
        else: 
            element.send_keys(word_input + "\n")
            time.sleep(1)
            (print(driver.find_element_by_xpath('//*[@id="txtTarget"]').text))
    
  
    
if __name__ == "__main__":
    PapagoDictionaryAccess().search_Word_and_Print()